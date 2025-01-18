.PHONY: install format lint type-check test clean all

install:
	poetry install

format:
	poetry run ruff format .

lint:
	poetry run ruff check .

type-check:
	poetry run mypy {{ cookiecutter.project_slug }} tests

test:
	poetry run pytest

check: format lint type-check test

all: install check
