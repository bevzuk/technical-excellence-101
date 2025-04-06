.PHONY: setup clear build lint test check-deps check clean-py

PYTHON := python3
PIP := pip3
BUILD_DIR := build
MD_FILE := Kolobok.md
HTML_FILE := $(BUILD_DIR)/Kolobok.html

# Установка зависимостей проекта
setup:
	$(PIP) install --upgrade pip 
	$(PIP) install -r requirements.txt

# Цель для проверки зависимостей
check-deps:
	@which $(PYTHON) > /dev/null || (echo "Error: Python not found"; exit 1)
	@which markdown2 > /dev/null || (echo "Error: markdown2 not found"; exit 1)
	@which pytest > /dev/null || (echo "Error: pytest not found"; exit 1)
	@which flake8 > /dev/null || (echo "Error: flake8 not found"; exit 1)

# Цель для очистки Python артефактов
clean-py:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +

# Очистка директории сборки
clear: clean-py
	@mkdir -p ./$(BUILD_DIR)
	rm -rf ./$(BUILD_DIR)/*

# Сборка HTML из Markdown
build: setup clear
	@if [ ! -f $(MD_FILE) ]; then \
		echo "Error: $(MD_FILE) not found"; \
		exit 1; \
	fi
	markdown2 $(MD_FILE) > $(HTML_FILE) || (echo "Error: Failed to convert markdown to HTML"; exit 1)
	@cat $(HTML_FILE)

# Проверка кода линтером
lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Запуск тестов
test: build
	pytest || (echo "Error: Tests failed"; exit 1)

# Цель для быстрой проверки
check: lint test

