# Modern Minimalistic Python

Bleeding edge [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) template to create new python packages.

## Purpose
This project is used to scaffold a `python` project structure. No third party dependency managers. Pure Python following PEP guidelines.

## Installation

Firstly, you will need to install dependencies:

```bash
pip install cookiecutter jinja2-git lice
```

Then, create a project itself:

```bash
cookiecutter git+ssh://git@github.com/mvp-projects/modern-minimalistic-py
```

## Getting started

```bash
# Create a virtual env
python -m venv .venv

# Activate it
source .venv/bin/activate

# Upgrade pip and install pip-tools

pip install -U pip pip-tools

# Refresh lockfiles

make refresh-lockfiles 

# Sync to dev environment

make sync-to-env env=dev
```
