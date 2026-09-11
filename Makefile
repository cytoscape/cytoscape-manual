# Cytoscape User Manual -- local build tooling.
#
# This repo produces no deployable artifact. The manual is published by
# ReadTheDocs, which clones the repo and runs its own Sphinx build from
# .readthedocs.yaml -- nothing is ever uploaded from a developer machine.
# `make build` runs the same Sphinx invocation against the same
# docs/requirements.txt purely as a local rehearsal, so docs/_build/html is a
# preview, never a release artifact.

PYTHON ?= python3
VENV   ?= .venv
PORT   ?= 8000

DOCS     := docs
BUILD    := $(DOCS)/_build/html
WARNINGS := $(DOCS)/_build/sphinx-warnings.txt
STAMP    := $(VENV)/.install-stamp

.DEFAULT_GOAL := help

help:  ## Show available targets
	@echo "Cytoscape User Manual"
	@echo
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*?## "} {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'
	@echo

$(STAMP): $(DOCS)/requirements.txt $(DOCS)/requirements-dev.txt
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --quiet --upgrade pip
	$(VENV)/bin/pip install --quiet -r $(DOCS)/requirements.txt -r $(DOCS)/requirements-dev.txt
	@touch $(STAMP)

install: $(STAMP)  ## Create .venv and install docs/requirements{,-dev}.txt

# Not listed in help: nothing should need to run this by hand, it exists only
# as a prerequisite of build.
clean:
	rm -rf $(DOCS)/_build .pytest_cache

# Cleans first on purpose. Sphinx's incremental mode skips unchanged files, and
# a skipped file emits no warnings -- the warnings assertion in the test suite
# is only meaningful against a full build where every source file is re-read.
#
# -w writes the warnings to a file so tests/test_manual.py can assert on them.
# (-n adds nothing for this Markdown manual, whose warnings MyST emits either
# way, but costs nothing and would catch nitpicks in any future .rst.)
build: clean install  ## Build the HTML manual into docs/_build/html (local preview, not a release artifact)
	$(VENV)/bin/python -m sphinx -b html -n -w $(WARNINGS) $(DOCS) $(BUILD)

test: build  ## Build, then run the test suite against the built HTML
	$(VENV)/bin/python -m pytest tests -q

# Depends on install rather than build: sphinx-autobuild's value is incremental
# rebuilds, and cleaning on every start would throw that away.
dev: install  ## Live-reloading preview at http://localhost:8000 (override with PORT=), rebuilds on save
	$(VENV)/bin/sphinx-autobuild -n -b html --port $(PORT) $(DOCS) $(BUILD)

.PHONY: help install clean build test dev
