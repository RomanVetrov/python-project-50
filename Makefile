.PHONY: install lint test coverage gendiff check

# 1) Устанавливает venv и все зависимости
install:
	python3 -m venv .env
	. .env/bin/activate && pip install --upgrade pip
	. .env/bin/activate && pip install -e . pytest pytest-cov ruff

# 2) Линт
lint:
	.env/bin/ruff check .

# 3) Тесты
test:
	.env/bin/pytest --maxfail=1 --disable-warnings -q

# 4) Отчёт покрытия
coverage:
	.env/bin/pytest --maxfail=1 --disable-warnings -q --cov=gendiff --cov-report=xml

# 5) CLI-утилита
gendiff:
	.env/bin/gendiff file1.json file2.json

# 6) Полная проверка: линт + тесты
check: lint test


