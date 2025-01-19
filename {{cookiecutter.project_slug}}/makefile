.PHONY: install format lint type-check test clean all

install:
	poetry install --with dev

format:
	poetry run ruff format .

lint:
	poetry run ruff check .

type-check:
	poetry run mypy {{ cookiecutter.project_slug }} tests

test:
	poetry run pytest

deptry:
	poetry run deptry {{ cookiecutter.project_slug }} tests

check: format lint type-check test deptry

all: install format lint check type-check test
