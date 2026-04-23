# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT

PLANTUML=plantuml
PLANTUML_OPTS = -tsvg

.PHONY: install test check format diagrams dist upgrade clean

install:
	uv sync
	uv run playwright install-deps
	uv run playwright install

test:
	uv run pytest

check:
	uv run ruff check .
	uv run zuban check

format:
	uv run ruff format .

diagrams:
	$(PLANTUML) $(PLANTUML_OPTS) docs/*.puml

dist: check test
	uv build

upgrade:
	uv sync --upgrade

clean:
	rm -rf .venv dist *.egg-info
	find . -type d -name "*.pyc" -exec rm -r {} +
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".ruff_cache" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
