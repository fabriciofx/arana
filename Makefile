# The MIT License (MIT)
#
# Copyright (C) 2025 Fabrício Barros Cabral
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

PYTHON=python
PIP=pip
RUFF=ruff
PLAYWRIGHT=playwright
PYTEST=pytest
ACTIVATE=. .venv/bin/activate
PLANTUML=plantuml

PLANTUML_OPTS = -tsvg

.PHONY: install tests lint format diagrams

install:
	$(PYTHON) -m venv .venv
	$(ACTIVATE) && $(PIP) install -r requirements.txt
	$(ACTIVATE) && $(PLAYWRIGHT) install
	$(ACTIVATE) && $(PLAYWRIGHT) install-deps

tests:
	$(ACTIVATE) && $(PYTEST)

lint:
	$(ACTIVATE) && $(RUFF) check .

format:
	$(ACTIVATE) && $(RUFF) format .

diagrams:
	$(PLANTUML) $(PLANTUML_OPTS) docs/*.puml
