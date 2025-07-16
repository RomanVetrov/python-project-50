.PHONY: install lint lint-fix test coverage gendiff check

# 1) Устанавливает dev-зависимости
install:
	pip install -e .[dev]

# 2) Линт
lint:
	ruff check .

# 3) Запуск тестов
test:
	pytest --maxfail=1 --disable-warnings -q

# 4) Отчёт покрытия
coverage:
	pytest --maxfail=1 --disable-warnings -q --cov=gendiff --cov-report=xml

# 5) Демка CLI-утилиты
gendiff:
	gendiff file1.json file2.json

# 6) Полная проверка: линт + тесты
check: lint test

lint-fix:
	ruff check . --fix

