.PHONY: gendiff

gendiff:
	uv run gendiff file1.json file2.json

.PHONY: lint

lint:
	uv run ruff check .

.PHONY: install gendiff lint test test-coverage check


test:
	uv run pytest --maxfail=1 --disable-warnings -q

test-coverage:
	uv run pytest --maxfail=1 --disable-warnings -q --cov=gendiff --cov-report=xml

check: lint test
