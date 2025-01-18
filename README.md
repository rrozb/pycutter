# pycutter
A heavily opinionated cookiecutter template built around my toolchain of choice, featuring optional setup for Cursor.


## Project Structure
cookiecutter-python-template/
├── cookiecutter.json
├── hooks/
│   └── post_gen_project.py
└── {{cookiecutter.project_slug}}/
    ├── .github/
    │   └── workflows/
    │       ├── ci.yml
    │       └── release.yml
    ├── src/
    │   └── {{cookiecutter.project_slug}}/
    │       ├── __init__.py
    │       └── main.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_main.py
    ├── .gitignore
    ├── .cursor
    ├── .ruff.toml
    ├── mypy.ini
    ├── pyproject.toml
    └── README.md

## Features
- Python 3.12
- Poetry
- Ruff
- Pytest
- Pytest-cov

## Usage
Install cookiecutter
```
pip install -U cookiecutter
```
Then run the following command to create a new project:
```bash
cookiecutter https://github.com/rrozb/pycutter.git
```

