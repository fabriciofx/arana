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
from abc import ABC, abstractmethod
from re import Pattern
from typing import Any

from playwright.sync_api import Page as Pwpg

from arana.element import Element, PwElement
from arana.frame import Frame, PwFrame


class Html(ABC):
    @abstractmethod
    def element(
        self, selector: str, *, has_text: str | Pattern[str] | None = None
    ) -> Element:
        pass

    @abstractmethod
    def by_role(
        self, role: str, *, name: str | Pattern[str] | None = None
    ) -> Element:
        pass

    @abstractmethod
    def by_test_id(self, test_id: str) -> Element:
        pass

    @abstractmethod
    def content(self) -> str:
        pass

    @abstractmethod
    def evaluate(self, expression: str) -> Any:
        pass

    @abstractmethod
    def frame(self, selector: str) -> Frame:
        pass


class PwHtml(Html):
    def __init__(self, pwpg: Pwpg) -> None:
        self.__pwpg = pwpg

    def element(
        self, selector: str, *, has_text: str | Pattern[str] | None = None
    ) -> Element:
        return PwElement(self.__pwpg.locator(selector, has_text=has_text))

    def by_role(
        self, role: str, *, name: str | Pattern[str] | None = None
    ) -> Element:
        return PwElement(self.__pwpg.get_by_role(role=role, name=name))

    def by_test_id(self, test_id: str) -> Element:
        return PwElement(self.__pwpg.get_by_test_id(test_id))

    def content(self) -> str:
        return self.__pwpg.content()

    def evaluate(self, expression: str) -> Any:
        return self.__pwpg.evaluate(expression)

    def frame(self, selector: str) -> Frame:
        return PwFrame(self.__pwpg.frame_locator(selector))
