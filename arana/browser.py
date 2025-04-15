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

from collections.abc import Generator
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from typing import Literal, Protocol

from playwright.sync_api import Browser as Rocket
from playwright.sync_api import sync_playwright

import arana.page
from arana.console import Console, StdConsole
from arana.page import Page, PwPage


class Browser(Protocol):
    def open(self, *, headless: bool = True) -> None: ...

    def close(self) -> None: ...

    def name(self) -> str: ...

    def page(self, url: str) -> Page: ...


BrowserType = Literal["chromium", "firefox", "webkit"]


class InvalidBrowserStateError(Exception):
    def __init__(self, message: str) -> None:
        self.__message = f"Invalid browser state: {message}"


class GenericBrowser(Browser):
    def __init__(self, name: str, browser_type: BrowserType) -> None:
        self._playwright = sync_playwright().start()
        self._pages: list[Page] = []
        self._name = name
        self._browser_type = browser_type
        self._rocket: Rocket | None = None
        self._browser_launcher = getattr(self._playwright, self._browser_type)

    def open(self, *, headless: bool = True) -> None:
        self._rocket = self._browser_launcher.launch(headless=headless)

    def close(self) -> None:
        for page in self._pages:
            page.close()
        if self._rocket:
            self._rocket.close()
        self._playwright.stop()

    def name(self) -> str:
        return self._name

    def page(self, url: str) -> Page:
        if self._rocket:
            page = PwPage(self._rocket, url)
            self._pages.append(page)
            return page
        error = "not opened"
        raise InvalidBrowserStateError(error)


class Chromium(GenericBrowser):

    def __init__(self) -> None:
        super().__init__("Chromium", "chromium")


class Firefox(GenericBrowser):

    def __init__(self) -> None:
        super().__init__("Firefox", "firefox")


class Webkit(GenericBrowser):

    def __init__(self) -> None:
        super().__init__("Webkit", "webkit")


class Logged(Browser):
    def __init__(self, browser: Browser, console: Console = StdConsole()) -> None:
        self.__origin = browser
        self.__console = console
        self.zone = timezone(
            timedelta(hours=-3)
        )  # A better solution would be to get the time zone from the configuration or use the local time

    def timestamp(self) -> str:
        return datetime.now(self.zone).strftime("%H:%M:%S.%f")

    @contextmanager
    def work(self, message: str) -> Generator:
        self.__console.log(f"[{self.timestamp()}] {message}... ")
        yield
        self.__console.logln("done.")

    def open(self, *, headless: bool = True) -> None:
        with self.work(f"Opening browser {self.name()}"):
            self.__origin.open(headless=headless)

    def close(self) -> None:
        with self.work(f"Closing browser {self.name()}"):
            self.__origin.close()

    def name(self) -> str:
        return self.__origin.name()

    def page(self, url: str) -> Page:
        with self.work("Creating a new page"):
            return arana.page.Logged(self.__origin.page(url), self.__console)


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
