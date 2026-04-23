# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
"""Config: load and save config parameters from a config file.

Returns:
    Config: a Config

"""

import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Config(ABC):
    """Interface that represents a Config.

    Returns:
        Config: a Config

    """

    @abstractmethod
    def load(self) -> dict[str, Any]:
        """Load the config params.

        Returns:
            dict[str, Any]: a dictionary with code and pages

        """
        pass

    @abstractmethod
    def save(self, data: dict[str, Any]) -> None:
        """Save the config params in a file.

        Args:
            data: a dictionary with code and pages

        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Convert the object in a string.

        Returns:
            str: the config file content as a string

        """
        pass


class FileConfig(Config):
    """A class that represents a Config.

    Returns:
        Config: a Config

    """

    def __init__(self, filename: str = ".zapspiderrc") -> None:
        """Initialize a Config.

        Args:
            filename (str, optional): The config filename. Defaults to
            '.zapspcodeerrc'.

        """
        self.__filename = filename

    def load(self) -> dict[str, Any]:
        """Load the config params.

        Returns:
            dict[str, Any]: a dictionary with code and pages

        """
        return json.loads(Path(self.__filename).read_text(encoding="utf-8"))

    def save(self, data: dict[str, Any]) -> None:
        """Save the config params in a file.

        Args:
            data: a dictionary with code and pages

        """
        Path(self.__filename).write_text(
            json.dumps(data, ensure_ascii=False), encoding="utf-8"
        )

    def __str__(self) -> str:
        """Convert the object in a string.

        Returns:
            str: the config file content as a string

        """
        return self.__filename


class FakeConfig(Config):
    """A class that represents a Config.

    Returns:
        Config: a Config

    """

    def __init__(self, data: dict[str, Any]) -> None:
        self.__data = data

    def load(self) -> dict[str, Any]:
        """Load the config params.

        Returns:
            dict[str, Any]: a dictionary with code and pages

        """
        return self.__data

    def save(self, data: dict[str, Any]) -> None:
        """Save the config params in a file.

        Args:
            data: a dictionary with code and pages

        """
        self.__data = data

    def __str__(self) -> str:
        """Convert the object in a string.

        Returns:
            str: the config file content as a string

        """
        return str(self.__data)
