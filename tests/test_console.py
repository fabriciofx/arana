# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
from arana.console import FakeConsole


def test_print() -> None:
    message = "The quick brown fox jumps over the lazy dog"
    console = FakeConsole()
    console.print(message)
    assert console.stdout() == message


def test_println() -> None:
    message = "The quick brown fox jumps over the lazy dog"
    console = FakeConsole()
    console.println(message)
    assert console.stdout() == f"{message}\n"


def test_log() -> None:
    message = "The quick brown fox jumps over the lazy dog"
    console = FakeConsole()
    console.log(message)
    assert console.stderr() == message


def test_logln() -> None:
    message = "The quick brown fox jumps over the lazy dog"
    console = FakeConsole()
    console.logln(message)
    assert console.stderr() == f"{message}\n"
