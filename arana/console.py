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
"""Console: module to operate a console."""

import sys
from abc import ABC, abstractmethod


class Console(ABC):
    @abstractmethod
    def print(self, message: str) -> None:
        pass

    @abstractmethod
    def println(self, message: str) -> None:
        pass

    @abstractmethod
    def log(self, message: str) -> None:
        pass

    @abstractmethod
    def logln(self, message: str) -> None:
        pass

    @abstractmethod
    def stdout(self) -> str:
        pass

    @abstractmethod
    def stderr(self) -> str:
        pass


class StdConsole(Console):
    """Class to operate a console (stdout / stderr)."""

    def print(self, message: str) -> None:
        """Print a message flushed and without end in stdout.

        Args:
            message (str): a message

        """
        print(message, end="", flush=True)

    def println(self, message: str) -> None:
        """Print a message flushed in stdout.

        Args:
            message (str): a message

        """
        print(message, flush=True)

    def log(self, message: str) -> None:
        """Print a message flushed and without end in stderr.

        Args:
            message (str): a message

        """
        print(message, end="", flush=True, file=sys.stderr)

    def logln(self, message: str) -> None:
        """Print a message flushed and without end in stdout.

        Args:
            message (str): a message

        """
        print(message, flush=True, file=sys.stderr)

    def stdout() -> str:
        return ""

    def stderr() -> str:
        return ""


class FakeConsole(Console):
    def __init__(self) -> None:
        self.__stdout = []
        self.__stderr = []

    def print(self, message: str) -> None:
        self.__stdout.append(message)

    def println(self, message: str) -> None:
        self.__stdout.append(f"{message}\n")

    def log(self, message: str) -> None:
        self.__stderr.append(message)

    def logln(self, message: str) -> None:
        self.__stderr.append(f"{message}\n")

    def stdout(self) -> str:
        return "".join(self.__stdout)

    def stderr(self) -> str:
        return "".join(self.__stderr)
