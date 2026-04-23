# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
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

    @abstractmethod
    def attribute(self, name: str) -> str:
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

    def attribute(self, name: str) -> str:
        attribute: str | None = self.__locator.get_attribute(name)
        if attribute is None:
            attribute = ""
        return attribute
