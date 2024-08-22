#!/bin/sh

# pytest .
flake8 ./app
black ./app ./tests --check
python -m isort ./app/**/*.py ./tests/**/*.py --check-only


