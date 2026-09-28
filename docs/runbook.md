# AAA Runbook

## Prerequisites
- Python 3.x
- Git
- VS Code

## Setup

### Clone Repository
git clone <repository-url>

### Create Virtual Environment
python -m venv .venv

### Activate Virtual Environment
.venv\Scripts\Activate.ps1

### Install Packages
pip install pytest

## Environment Variables

### .env
Used to store configuration values.

## Run Practice Files

### SQLite Practice
python docs/sqlite_practice.py

### Pydantic Practice
python docs/pydantic_practice.py

## Run Tests
pytest docs/test_sample.py

## Modules

- pydantic_practice.py : Pydantic learning examples
- sqlite_practice.py : SQLite database practice
- transaction_practice.py : Transaction examples
- test_sample.py : Pytest examples
- glossary.md : Project terms
- runbook.md : Setup instructions