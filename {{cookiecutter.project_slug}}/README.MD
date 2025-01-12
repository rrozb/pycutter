# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Prerequisites

- Python {{ cookiecutter.python_version }}
- Poetry (2.0 or higher)

## Installation

1. Install pipx using this [guide](https://github.com/pypa/pipx)
2. Install Poetry using pipx
```bash
pipx install poetry
```
3. Install the dependencies
```bash
poetry install
```

## Ruff

Run ruff to check the code

```bash
ruff check .
```

Run ruff to format the code

```bash
ruff format .
```

## Pytest

Run pytest to run the tests

```bash
poetry run pytest
```

