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
