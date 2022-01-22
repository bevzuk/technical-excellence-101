setup:
	pip3 install --upgrade pip markdown2 pytest

clear:
	rm -rf ./build/*
	mkdir -p ./build

build: setup clear
	markdown2 Kolobok.md >> ./build/Kolobok.html
	cat ./build/Kolobok.html

test: build
	pytest