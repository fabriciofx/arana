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
