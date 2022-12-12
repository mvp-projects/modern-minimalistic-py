SHELL:=/usr/bin/env bash
OS = $(shell uname | tr A-Z a-z)

.PHONY: refresh-lockfiles
refresh-lockfiles: ## Rewrite requirements lockfiles
	@echo "Updating requirements/*.txt files using `pip-compile`"
	find requirements/ -name '*.txt' ! -name 'all.txt' -type f -delete
	mkdir -p requirements
	pip-compile -q --resolver backtracking --extra dev -o requirements/dev-requirements.txt pyproject.toml
	pip-compile -q --resolver backtracking -o requirements/docs.txt requirements/docs.in
	pip-compile -q --resolver backtracking -o requirements/core-requirements.txt pyproject.toml

.PHONY: sync-dev-environment
sync-dev-environment: ## sync dev virtualenv with requirements/dev-requirements.txt
	@pip-sync requirements/dev-requirements.txt

.PHONE: show-envs
show-envs: ## Show all different environments
	@hatch env show

.PHONE: prune-envs
prune-envs: ## Prune project related envs. May require to deactivate venv and reload terminal.
	@hatch env prune

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
	@find tests sample -empty -type d -delete

.PHONY: help
.DEFAULT_GOAL := help
help:
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'