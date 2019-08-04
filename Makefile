.PHONY: default install test

default: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=.src python -m pytest
	# PYTHONPATH=./src pytest