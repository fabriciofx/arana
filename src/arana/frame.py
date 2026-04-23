# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
from abc import ABC, abstractmethod
from re import Pattern
from typing import Any, cast

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
        return PwElement(
            self.__frame.get_by_role(role=cast("Any", role), name=name)
        )

    def by_test_id(self, test_id: str) -> Element:
        return PwElement(self.__frame.get_by_test_id(test_id))
