VENV = ../venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r ../requirements.txt

test: setup
	$(PYTHON) -m pytest
