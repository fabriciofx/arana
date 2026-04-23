# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone

from playwright.sync_api import sync_playwright

import arana.page
from arana.console import Console, StdConsole
from arana.page import Page, PwPage


class Browser(ABC):
    @abstractmethod
    def open(self, *, headless: bool = True) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def page(self, url: str) -> Page:
        pass


class Chromium(Browser):
    def __init__(self) -> None:
        self.__playwright = sync_playwright().start()
        self.__pages: list[Page] = []

    def open(self, *, headless: bool = True) -> None:
        self.__rocket = self.__playwright.chromium.launch(headless=headless)

    def close(self) -> None:
        for page in self.__pages:
            page.close()
        self.__rocket.close()
        self.__playwright.stop()

    def name(self) -> str:
        return "Chromium"

    def page(self, url: str) -> Page:
        page = PwPage(self.__rocket, url)
        self.__pages.append(page)
        return page


class Firefox(Browser):
    def __init__(self) -> None:
        self.__playwright = sync_playwright().start()
        self.__pages: list[Page] = []

    def open(self, *, headless: bool = True) -> None:
        self.__rocket = self.__playwright.firefox.launch(headless=headless)

    def close(self) -> None:
        for page in self.__pages:
            page.close()
        self.__rocket.close()
        self.__playwright.stop()

    def name(self) -> str:
        return "Firefox"

    def page(self, url: str) -> Page:
        page = PwPage(self.__rocket, url)
        self.__pages.append(page)
        return page


class Webkit(Browser):
    def __init__(self) -> None:
        self.__playwright = sync_playwright().start()
        self.__pages: list[Page] = []

    def open(self, *, headless: bool = True) -> None:
        self.__rocket = self.__playwright.webkit.launch(headless=headless)

    def close(self) -> None:
        for page in self.__pages:
            page.close()
        self.__rocket.close()
        self.__playwright.stop()

    def name(self) -> str:
        return "Webkit"

    def page(self, url: str) -> Page:
        page = PwPage(self.__rocket, url)
        self.__pages.append(page)
        return page


class Logged(Browser):
    def __init__(
        self, browser: Browser, console: Console = StdConsole()
    ) -> None:
        self.__origin = browser
        self.__console = console

    def open(self, *, headless: bool = True) -> None:
        zone = timezone(timedelta(hours=-3))
        timestamp = datetime.now(zone).strftime("%H:%M:%S.%f")
        self.__console.log(f"[{timestamp}] Opening browser {self.name()}... ")
        self.__origin.open(headless=headless)
        self.__console.logln("done.")

    def close(self) -> None:
        zone = timezone(timedelta(hours=-3))
        timestamp = datetime.now(zone).strftime("%H:%M:%S.%f")
        self.__console.log(f"[{timestamp}] Closing browser {self.name()}... ")
        self.__origin.close()
        self.__console.logln("done.")

    def name(self) -> str:
        return self.__origin.name()

    def page(self, url: str) -> Page:
        zone = timezone(timedelta(hours=-3))
        timestamp = datetime.now(zone).strftime("%H:%M:%S.%f")
        self.__console.log(f"[{timestamp}] Creating a new page... ")
        page = arana.page.Logged(self.__origin.page(url), self.__console)
        self.__console.logln("done.")
        return page


class Headed(Browser):
    def __init__(self, browser: Browser) -> None:
        self.__origin = browser

    def open(self, *, headless: bool = True) -> None:
        self.__origin.open(headless=False)

    def close(self) -> None:
        self.__origin.close()

    def name(self) -> str:
        return self.__origin.name()

    def page(self, url: str) -> Page:
        return self.__origin.page(url)
