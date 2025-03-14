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
