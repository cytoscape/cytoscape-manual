"""Paths and normalization shared by the warnings test and its regeneration script.

Deliberately standard-library only: tests/regenerate_warnings_baseline.py is
documented as runnable with the system interpreter, which has no pytest.
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WARNINGS_FILE = os.path.join(REPO_ROOT, "docs", "_build", "sphinx-warnings.txt")
BASELINE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "sphinx_warnings_baseline.txt")


def normalize_warnings(text):
    """Strip the absolute path prefix and line numbers from warning lines.

    Line numbers move whenever a chapter is edited, so comparing them would
    make the baseline fail on unrelated changes.
    """
    normalized = set()
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        line = line.replace(REPO_ROOT + os.sep, "")
        line = re.sub(r"^(\S+?):\d+:", r"\1:", line)
        normalized.add(line)
    return normalized


def read_baseline():
    """The baseline set, with its explanatory comment header stripped."""
    with open(BASELINE_FILE, encoding="utf-8") as handle:
        return normalize_warnings(
            "".join(line for line in handle if not line.startswith("#"))
        )
