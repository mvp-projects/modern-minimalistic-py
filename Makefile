SHELL:=/usr/bin/env bash
OS = $(shell uname | tr A-Z a-z)

.PHONE: show-envs
show-envs: ## Show all different environments
	@hatch env show --ascii

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