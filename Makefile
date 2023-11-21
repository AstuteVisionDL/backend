VENV := .venv

PROJECT := src
TESTS := tests

# Prepare

.venv:
	poetry install --no-root
	poetry check

setup: .venv

# Lint

black:
	poetry run black --check --diff $(PROJECT)

flake: .venv
	poetry run flake8 $(PROJECT)

pylint: .venv
	poetry run pylint $(PROJECT)

lint: black flake pylint


# Test

.pytest:
	poetry run pytest $(TESTS)

test: .venv .pytest
