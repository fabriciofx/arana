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
