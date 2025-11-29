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

from playwright.sync_api import FrameLocator

from arana.element import Element, PwElement


class Frame(ABC):
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


class PwFrame(Frame):
    def __init__(self, frame: FrameLocator) -> None:
        self.__frame = frame

    def element(
        self, selector: str, *, has_text: str | Pattern[str] | None = None
    ) -> Element:
        return PwElement(self.__frame.locator(selector, has_text=has_text))

    def by_role(
        self, role: str, *, name: str | Pattern[str] | None = None
    ) -> Element:
        return PwElement(self.__frame.get_by_role(role=role, name=name))

    def by_test_id(self, test_id: str) -> Element:
        return PwElement(self.__frame.get_by_test_id(test_id))
