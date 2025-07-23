# Gendiff — Difference Calculator

[![Hexlet Tests and Linter Status](https://github.com/RomanVetrov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/RomanVetrov/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=RomanVetrov_python-project-50&metric=alert_status)](https://sonarcloud.io/dashboard?id=RomanVetrov_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=RomanVetrov_python-project-50&metric=coverage)](https://sonarcloud.io/dashboard?id=RomanVetrov_python-project-50)

---

## Description

**Gendiff** is a command-line tool for finding differences between configuration files (`.json`, `.yaml`, `.yml`).  
Supports nested structures, several output formats, and is fully CI-ready.

---

## Requirements

- [Python 3.12+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/) or [uv](https://astral.sh)
- [make](https://www.gnu.org/software/make/) (for convenient project commands)

---

## Installation

```bash
git clone https://github.com/RomanVetrov/python-project-50.git
cd python-project-50

# With pip (default)
make install

# Or with uv (faster, optional)
uv pip install -e .[dev]
```

## Supported File Formats

- **JSON** (`.json`)
- **YAML** (`.yaml`, `.yml`)

## Makefile Commands

- `make install` — install dependencies
- `make lint` — check style (ruff)
- `make lint-fix` — auto-fix style
- `make test` — run tests (pytest)
- `make coverage` — generate coverage.xml
- `make gendiff` — sample CLI run
- `make check` — lint + tests

## Usage (CLI)

```bash
gendiff -h
gendiff --help

# Compare two flat JSON files

gendiff tests/test_data/file1.json tests/test_data/file2.json

# Compare two flat YAML files

gendiff tests/test_data/file1.yaml tests/test_data/file2.yaml

# Compare two nested JSON files

gendiff tests/test_data/nested1.json tests/test_data/nested2.json

# Use 'stylish' format (default and explicitly)

gendiff --format stylish tests/test_data/nested1.json tests/test_data/nested2.json
gendiff --format stylish tests/test_data/file1.yaml tests/test_data/file2.yaml

# Use 'plain' format

gendiff --format plain tests/test_data/nested1.json tests/test_data/nested2.json
gendiff --format plain tests/test_data/file1.yaml tests/test_data/file2.yaml

# Use 'json' format (machine-readable)

gendiff --format json tests/test_data/nested1.json tests/test_data/nested2.json
gendiff --format json tests/test_data/file1.yaml tests/test_data/file2.yaml
```


## Demo

[![asciicast](https://asciinema.org/a/cUshoqvzf3eB7iaYoZzhQO6eK.svg)](https://asciinema.org/a/cUshoqvzf3eB7iaYoZzhQO6eK)

## License

MIT License

## Contacts

- Telegram: [@ZZyngZZ](https://t.me/ZZyngZZ)
- Email: romanvikernes@gmail.com

## Credits

Project developed as part of the [Hexlet Python Course](https://ru.hexlet.io/programs/python)