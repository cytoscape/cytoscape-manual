"""Shared fixtures for the manual's test suite.

The tests assert on what the built manual actually serves over HTTP, so they
need a real server in front of docs/_build/html. This module owns that
server's whole lifecycle -- the Makefile deliberately does not spawn or kill
it, because only the fixture can guarantee cleanup when a test aborts.
"""

import atexit
import os
import signal
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_DIR = os.path.join(REPO_ROOT, "docs", "_build", "html")
WARNINGS_FILE = os.path.join(REPO_ROOT, "docs", "_build", "sphinx-warnings.txt")

STARTUP_TIMEOUT = 15.0
SHUTDOWN_TIMEOUT = 5.0
PORT_ATTEMPTS = 5


def _free_port():
    """Grab a port the OS is willing to hand out, then let go of it.

    Avoids colliding with a `make dev` left running on 8000, and with other
    jobs on a shared CI runner.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _kill(process):
    """Terminate the server, escalating to SIGKILL, bounded at every step."""
    if process.poll() is not None:
        return
    for send, wait in ((process.terminate, SHUTDOWN_TIMEOUT), (process.kill, SHUTDOWN_TIMEOUT)):
        try:
            send()
        except ProcessLookupError:
            return
        try:
            process.wait(timeout=wait)
            return
        except subprocess.TimeoutExpired:
            continue
    # Last resort: signal the whole process group we started.
    try:
        os.killpg(os.getpgid(process.pid), signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        pass


class PortTaken(Exception):
    """Another process grabbed the port between allocation and bind."""


def _wait_until_serving(base_url, process):
    deadline = time.monotonic() + STARTUP_TIMEOUT
    while time.monotonic() < deadline:
        if process.poll() is not None:
            output = process.stdout.read() if process.stdout else ""
            # _free_port lets go of the port before http.server binds it, so a
            # racing process can take it in between. That is worth retrying;
            # any other startup failure is not.
            if "address already in use" in output.lower():
                raise PortTaken(output)
            raise RuntimeError(
                f"http.server exited with {process.returncode} before serving:\n{output}"
            )
        try:
            with urllib.request.urlopen(base_url, timeout=1):
                return
        except (urllib.error.URLError, ConnectionError, OSError):
            time.sleep(0.1)
    raise RuntimeError(f"http.server did not start serving {base_url} within {STARTUP_TIMEOUT}s")


def _start_server():
    """Start http.server on a free port, retrying only if the port was taken."""
    for attempt in range(1, PORT_ATTEMPTS + 1):
        port = _free_port()
        url = f"http://127.0.0.1:{port}/"
        process = subprocess.Popen(
            [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
            cwd=BUILD_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            # Own process group, so teardown can signal the whole group and
            # never orphan a child.
            start_new_session=True,
        )
        atexit.register(_kill, process)
        try:
            _wait_until_serving(url, process)
            return process, url
        except PortTaken:
            _kill(process)
            atexit.unregister(_kill)
            if attempt == PORT_ATTEMPTS:
                raise RuntimeError(
                    f"could not get a free port after {PORT_ATTEMPTS} attempts"
                )
        except BaseException:
            _kill(process)
            atexit.unregister(_kill)
            raise


@pytest.fixture(scope="session")
def base_url():
    """Serve docs/_build/html on localhost and yield its base URL."""
    if not os.path.isdir(BUILD_DIR):
        pytest.fail(f"{BUILD_DIR} does not exist -- run `make build` first")

    # _start_server registers the atexit kill as belt and braces: pytest's own
    # teardown is skipped on an internal error or a crash in another fixture,
    # but atexit still runs.
    process, url = _start_server()
    try:
        yield url
    finally:
        _kill(process)
        atexit.unregister(_kill)
