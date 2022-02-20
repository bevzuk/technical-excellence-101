setup:
	pip3 install --upgrade pip 
	pip3 install markdown2 pytest flake8

clear:
	rm -rf ./build/*
	mkdir -p ./build

build: setup clear
	markdown2 Kolobok.md > ./build/Kolobok.html
	cat ./build/Kolobok.html

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test: build
	pytest

