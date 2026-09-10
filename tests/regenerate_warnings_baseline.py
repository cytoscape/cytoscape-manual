#!/usr/bin/env python3
"""Rewrite sphinx_warnings_baseline.txt from the current build.

Run `make build` first. Review the diff before committing -- the point of the
baseline is that new warnings are noticed, so regenerating it to make a test
pass defeats it.
"""

import os
import pathlib
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from test_manual import BASELINE_FILE, WARNINGS_FILE, normalize_warnings

def main():
    if not os.path.exists(WARNINGS_FILE):
        sys.exit(f"{WARNINGS_FILE} not found -- run `make build` first")

    produced = normalize_warnings(pathlib.Path(WARNINGS_FILE).read_text())
    existing = pathlib.Path(BASELINE_FILE).read_text().splitlines()
    header = [line for line in existing if line.startswith("#")]

    pathlib.Path(BASELINE_FILE).write_text(
        "\n".join(header) + "\n" + "\n".join(sorted(produced)) + "\n"
    )
    print(f"wrote {len(produced)} entries to {BASELINE_FILE}")


if __name__ == "__main__":
    main()
