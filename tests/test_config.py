# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
from typing import Any

from arana.config import FakeConfig


def test_load() -> None:
    data: dict[str, Any] = {"code": 10, "pages": [5, 3, 7, 9, 2, 56, 8, 19]}
    config = FakeConfig(data)
    params = config.load()
    assert params == data


def test_save() -> None:
    config = FakeConfig({})
    config.save({"code": 10, "pages": [5, 3, 7, 9, 2, 56, 8, 19]})
    assert str(config) == "{'code': 10, 'pages': [5, 3, 7, 9, 2, 56, 8, 19]}"
