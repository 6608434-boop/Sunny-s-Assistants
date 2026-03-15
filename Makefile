.PHONY: dev test build clean proto init install-dev install lint format typecheck run-admin run-telegram docker-up docker-down

# Переменные
PYTHON = python
PIP = pip
PROJECT_NAME = sunnys_assistants

# Запуск админки (мок-режим)
dev:
	$(PYTHON) run_admin.py

# Запуск Telegram бота
run-telegram:
	$(PYTHON) -m $(PROJECT_NAME).telegram_bot.bot

# Тесты
test:
	pytest tests/ -v --cov=$(PROJECT_NAME) --cov-report=html

test-unit:
	pytest tests/unit/ -v

test-integration:
	pytest tests/integration/ -v

test-performance:
	pytest tests/performance/ -v --benchmark-only

# Сборка
build:
	docker-compose -f infra/docker/docker-compose.yml build

# Очистка
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Протобуф (компиляция .proto файлов)
proto:
	cd go_modules && make proto

# Установка зависимостей
install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements-dev.txt

# Форматирование кода
format:
	black $(PROJECT_NAME) tests
	isort $(PROJECT_NAME) tests

lint:
	flake8 $(PROJECT_NAME) tests
	mypy $(PROJECT_NAME) tests
	ruff $(PROJECT_NAME) tests

typecheck:
	mypy $(PROJECT_NAME) tests --strict

# Инициализация проекта
init:
	cp .env.example .env
	make install-dev
	make proto

# Docker
docker-up:
	docker-compose -f infra/docker/docker-compose.yml up -d

docker-down:
	docker-compose -f infra/docker/docker-compose.yml down

docker-logs:
	docker-compose -f infra/docker/docker-compose.yml logs -f

# Админские скрипты
generate-demo-keys:
	$(PYTHON) scripts/generate_demo_keys.py

grant-vera-access:
	$(PYTHON) scripts/grant_vera_access.py

# Документация
docs-serve:
	mkdocs serve

docs-build:
	mkdocs build