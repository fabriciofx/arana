# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
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

    def stdout(self) -> str:
        return ""

    def stderr(self) -> str:
        return ""


class FakeConsole(Console):
    def __init__(self) -> None:
        self.__stdout: list[str] = []
        self.__stderr: list[str] = []

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
