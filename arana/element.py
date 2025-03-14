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
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import Locator


class Element(ABC):
    @abstractmethod
    def text(self) -> str:
        pass

    @abstractmethod
    def texts(self) -> list[str]:
        pass

    @abstractmethod
    def visible(self) -> bool:
        pass

    @abstractmethod
    def click(self) -> None:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def nth(self, index: int) -> Element:
        pass


class PwElement(Element):
    def __init__(self, locator: Locator) -> None:
        self.__locator = locator

    def text(self) -> str:
        txt = ""
        if self.__locator.count() > 1:
            txt = self.__locator.nth(0).inner_text()
        else:
            txt = self.__locator.inner_text()
        return txt

    def texts(self) -> list[str]:
        return self.__locator.all_inner_texts()

    def visible(self) -> bool:
        return self.__locator.is_visible()

    def click(self) -> None:
        self.__locator.click()

    def count(self) -> int:
        return self.__locator.count()

    def nth(self, index: int) -> Element:
        return PwElement(self.__locator.nth(index))
