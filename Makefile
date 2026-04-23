# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT

PLANTUML=plantuml
PLANTUML_OPTS = -tsvg

.PHONY: install tests lint format diagrams build clean

install:
	uv sync
	uv run playwright install-deps
	uv run playwright install

tests:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

diagrams:
	$(PLANTUML) $(PLANTUML_OPTS) docs/*.puml

build:
	uv build

clean:
	rm -rf .venv dist *.egg-info
	find . -type d -name "*.pyc" -exec rm -r {} +
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".ruff_cache" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
