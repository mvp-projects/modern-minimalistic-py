# sample

[![Build Status](https://github.com/Tomperez98/modern-minimalistic-py/workflows/test/badge.svg?branch=main&event=push)](https://github.com/Tomperez98/modern-minimalistic-py/actions?query=workflow%3Atest)
![black-python-styleguide](https://img.shields.io/badge/code%20style-black-000000.svg)

-----

**Table of Contents**

- [sample](#sample)
  - [Inspiration](#inspiration)
  - [How to run?](#how-to-run)

## Inspiration
Nor Pydantic, FastAPI, Ruff, ... seem to use `Poetry` to manage dependencies. In fact, since Poetry's last update to `v1.20` I have encounter quite a few problems running different project. Another huge issue is that `Poetry` does not respect the [PEP 621](https://peps.python.org/pep-0621/) standard which may cause issue when the project interacts with libraries that expect an standard format for the `pyproject.toml` file.

This Template Project does not require any Package Manager, it runs purely with native Python solutions (`.venv`, for example) and sticks with `requirements.txt` files to manage dependencies (Which, btw, is the pythonic way to handle this).

## How to run?
- Create a virtual environment
- Activate the environment
- run `make install-dev `
