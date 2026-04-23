# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
from abc import ABC, abstractmethod
from re import Pattern
from typing import Any, cast

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
        return PwElement(
            self.__pwpg.get_by_role(role=cast("Any", role), name=name)
        )

    def by_test_id(self, test_id: str) -> Element:
        return PwElement(self.__pwpg.get_by_test_id(test_id))

    def content(self) -> str:
        return self.__pwpg.content()

    def evaluate(self, expression: str) -> Any:
        return self.__pwpg.evaluate(expression)

    def frame(self, selector: str) -> Frame:
        return PwFrame(self.__pwpg.frame_locator(selector))


class PlainHtml(Html):
    def __init__(self, content: str) -> None:
        self.__content = content

    def element(
        self, selector: str, *, has_text: str | Pattern[str] | None = None
    ) -> Element:
        msg = "PlainHtml does not support element()"
        raise NotImplementedError(msg)

    def by_role(
        self, role: str, *, name: str | Pattern[str] | None = None
    ) -> Element:
        msg = "PlainHtml does not support by_role()"
        raise NotImplementedError(msg)

    def by_test_id(self, test_id: str) -> Element:
        msg = "PlainHtml does not support by_test_id()"
        raise NotImplementedError(msg)

    def content(self) -> str:
        return self.__content

    def evaluate(self, expression: str) -> Any:
        msg = "PlainHtml does not support evaluate()"
        raise NotImplementedError(msg)

    def frame(self, selector: str) -> Frame:
        msg = "PlainHtml does not support frame()"
        raise NotImplementedError(msg)
