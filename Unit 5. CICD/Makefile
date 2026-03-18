VENV = ../venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r ../requirements.txt

clear:
	rm -rf ./build/*
	mkdir -p ./build

build: setup clear
	$(VENV)/bin/markdown2 Kolobok.md > ./build/Kolobok.html
	cat ./build/Kolobok.html

lint:
	$(VENV)/bin/flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	$(VENV)/bin/flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test: build
	$(VENV)/bin/pytest
