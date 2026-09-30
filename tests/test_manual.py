"""Tests against the built manual, served over HTTP.

Beyond a smoke check, these pin the chapter numbering: the toctree in
docs/index.rst is auto-numbered, so inserting or removing an entry silently
renumbers everything after it. Asserting the numbers here means such a change
fails the suite instead of shipping unnoticed.
"""

import urllib.request

import pytest

from warnings_baseline import WARNINGS_FILE, normalize_warnings, read_baseline


def fetch(base_url, path=""):
    with urllib.request.urlopen(base_url + path, timeout=10) as response:
        assert response.status == 200, f"{path or '/'} returned {response.status}"
        return response.read().decode("utf-8")


@pytest.fixture(scope="session")
def landing_page(base_url):
    return fetch(base_url)


def test_landing_page_serves(landing_page):
    assert "<title>" in landing_page
    assert "Cytoscape User Manual" in landing_page


def test_static_assets_were_collected(base_url):
    """A build can produce HTML but lose _static, leaving tables unstyled."""
    fetch(base_url, "_static/custom.css")


def test_agentic_integration_chapter_is_published(base_url):
    chapter = fetch(base_url, "Agentic_Integration.html")
    assert "Agentic Integration" in chapter


def test_agentic_integration_is_chapter_27(landing_page):
    assert "27. Agentic Integration" in landing_page


@pytest.mark.parametrize(
    "entry",
    [
        "26. Cytoscape Automation",
        "28. Cytoscape Privacy Policy",
        "29. Basic Expression Analysis Tutorial",
    ],
)
def test_surrounding_chapters_are_numbered_as_expected(landing_page, entry):
    assert entry in landing_page


def test_no_new_sphinx_warnings():
    """Assert the build introduced no warning that is not already recorded.

    `make build` writes Sphinx's warnings to a file so this can be a test
    rather than something a human is expected to spot in scrollback.

    The manual carries a long tail of pre-existing warnings -- see the header
    of sphinx_warnings_baseline.txt -- so -W (warnings as errors) is not
    usable and neither is asserting the list is empty. Comparing against a
    committed baseline still fails the build on anything new, such as a
    missing image or a mistyped toctree entry.
    """
    with open(WARNINGS_FILE, encoding="utf-8") as handle:
        produced = normalize_warnings(handle.read())
    baseline = read_baseline()

    new = sorted(produced - baseline)
    assert not new, (
        "Sphinx emitted warnings not present in tests/sphinx_warnings_baseline.txt:\n"
        + "\n".join(new)
        + "\n\nFix them, or -- if they are genuinely pre-existing -- regenerate "
        "the baseline as documented in that file's header."
    )
