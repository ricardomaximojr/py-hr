.PHONY: default install test

default: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=.src python3 -m pytest
	# PYTHONPATH=./src pytest
