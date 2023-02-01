.DEFAULT_GOAL := help
SHELL:=/usr/bin/env bash
OS = $(shell uname | tr A-Z a-z)
sources = {{cookiecutter.project_name.lower().replace('-', '_')}} tests scripts

.PHONY: install
install: ## Install dev dependencies (MAKE SURE YOU ARE WITHIN A VENV).
	python -m pip install -U pip
	pip install -r requirements/$(env).txt
	pip install -e .

.PHONY: new-release
new-release: ## Prepare new release for github.
	python scripts/release_github.py

.PHONY: refresh-lockfiles
refresh-lockfiles: ## Rewrite requirements lockfiles
	@echo "Updating requirements/*.txt files using `pip-compile`"
	find requirements/ -name '*.txt' ! -name 'all.txt' -type f -delete
	mkdir -p requirements
	# https://github.com/dependabot/dependabot-core/issues/3940
	pip-compile -q --upgrade --resolver backtracking --no-emit-trusted-host -o requirements/core.txt pyproject.toml
	pip-compile -q --upgrade --extra dev --resolver backtracking --no-emit-trusted-host -o requirements/dev.txt pyproject.toml

.PHONY: sync-to-env
sync-to-env: ## sync dev virtualenv
	@pip-sync requirements/$(env).txt
	@pip install -e .

.PHONY: lint
lint: ## Lint code.
	mypy $(sources)
	ruff $(sources)
	black $(sources)

.PHONY: unit
unit: ## Run code unittest
	pytest .

.PHONY: test
test:
	make lint
	make unit

.PHONY: clean
clean: ## Cleans project folder mainly cache
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .ruff_cache
	@rm -rf .mypy_cache
	@rm -rf htmlcov
	@rm -rf *.egg-info
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -f coverage.xml
	@rm -rf build
	@find tests {{cookiecutter.project_name.lower().replace('-', '_')}} -empty -type d -delete

.PHONY: serve-docs
serve-docs: ## Serve project documentation
	@mkdocs serve

.PHONY: build-docs
build-docs:
	@mkdocs build

.PHONY: help
help:
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'
