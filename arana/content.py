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
from typing import Any

from arana.browser import Browser
from arana.console import Console, StdConsole
from arana.response import Response
from arana.rndm import RandomWait


class Content(ABC):
    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def refine(self, response: Response) -> dict[str, Any]:
        pass


class ContentText(Content):
    def __init__(self, url: str) -> None:
        self.__url = url

    def url(self) -> str:
        return self.__url

    def refine(self, response: Response) -> dict[str, Any]:
        html = response.html()
        text = html.evaluate("document.body.innerText")
        return {"html": html, "text": text}


class Logged(Content):
    def __init__(
        self, content: Content, console: Console = StdConsole()
    ) -> None:
        self.__origin = content
        self.__console = console

    def url(self) -> str:
        return self.__origin.url()

    def refine(self, response: Response) -> dict[str, Any]:
        zone = timezone(timedelta(hours=-3))
        timestamp = datetime.now(zone).strftime("%H:%M:%S.%f")
        self.__console.log(f"[{timestamp}] Refining '{self.url()}'... ")
        data = self.__origin.refine(response)
        self.__console.logln("done.")
        return data


class Retry(Content):
    def __init__(
        self,
        content: Content,
        browser: Browser,
        random_wait: RandomWait = RandomWait(2, 3),
        max_retries: int = 10,
    ) -> None:
        self.__origin = content
        self.__browser = browser
        self.__random_wait = random_wait
        self.__max_retries = max_retries

    def url(self) -> str:
        return self.__origin.url()

    def refine(self, response: Response) -> dict[str, Any]:
        data = None
        try:
            data = self.__origin.refine(response)
        except Exception:
            retries = 1
            while data is None and retries <= self.__max_retries:
                self.__random_wait.run()
                try:
                    url = self.__origin.url()
                    page = self.__browser.page(url)
                    resp = page.open()
                    data = self.__origin.refine(resp)
                    page.close()
                except Exception:
                    retries += 1
                    continue
                break
        return data
