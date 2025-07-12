.PHONY: install lint test coverage gendiff check

# 1) Устанавливает проект и dev-зависимости через uv
install:
	uv tool install .[dev]

# 2) Линт
lint:
	uv run ruff check .

# 3) Запуск тестов
test:
	uv run pytest --maxfail=1 --disable-warnings -q

# 4) Отчёт покрытия
coverage:
	uv run pytest --maxfail=1 --disable-warnings -q --cov=gendiff --cov-report=xml

# 5) Демка CLI-утилиты
gendiff:
	uv run gendiff file1.json file2.json

# 6) Полная проверка: линт + тесты
check: lint test


