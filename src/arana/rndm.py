# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
import random
import time

"""Generate random integer numbers."""


class RandomInt:
    def value(self, start: int, end: int) -> int:
        """Generate a random integer number between two integer numbers inclusive.

        Args:
            start (int): start number interval
            end (int): end number interval

        Returns:
            int: a random integer number between start and end inclusive

        """
        return random.randrange(start, end + 1)

    def values(self, start: int, end: int) -> list[int]:
        """Generate a list of integer random numbers between two integer numbers inclusive.

        Args:
            start (int): start number interval
            end (int): end number interval

        Returns:
            list[int]: a list of integer numbers between start and end inclusive

        """
        return random.sample(range(start, end + 1), end - start + 1)


class RandomWait:
    def __init__(self, min_secs: int = 1, max_secs: int = 10) -> None:
        self.__min_secs = min_secs
        self.__max_secs = max_secs

    def run(self) -> None:
        time.sleep(random.randrange(self.__min_secs, self.__max_secs + 1))
