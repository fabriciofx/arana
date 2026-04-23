# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
import re

from arana.browser import Chromium, Firefox, Logged, Webkit
from arana.console import FakeConsole


def test_chromium() -> None:
    browser = Chromium()
    browser.open()
    browser.close()


def test_firefox() -> None:
    browser = Firefox()
    browser.open()
    browser.close()


def test_webkit() -> None:
    browser = Webkit()
    browser.open()
    browser.close()


def test_logged() -> None:
    console = FakeConsole()
    browser = Logged(Chromium(), console)
    browser.open()
    browser.close()
    assert re.search(
        r"\[[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}] Opening browser Chromium... "
        r"done.\n"
        r"\[[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}] Closing browser Chromium... "
        r"done.\n",
        console.stderr(),
    )
