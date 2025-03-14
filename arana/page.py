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

from browserforge.fingerprints import FingerprintGenerator
from browserforge.injectors.playwright import NewContext
from playwright.sync_api import Browser as Rocket

from arana.console import Console, StdConsole
from arana.html import PwHtml
from arana.response import PwResponse, Response
from arana.rndm import RandomInt, RandomWait


class Page(ABC):
    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def open(self) -> Response:
        pass

    @abstractmethod
    def pause(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def reload(self) -> Response:
        pass

    @abstractmethod
    def scroll(self, random_wait: RandomWait) -> bool:
        pass


class PwPage(Page):
    def __init__(self, rocket: Rocket, url: str) -> None:
        self.__fingerprints = FingerprintGenerator()
        self.__session = NewContext(
            rocket,
            fingerprint=self.__fingerprints.generate(
                browser=("chrome", "firefox", "safari", "edge"),
                os=("windows", "macos", "linux"),
            ),
            ignore_https_errors=True,
        )
        self.__pwpg = self.__session.new_page()
        # I don't know why need it to allow close() without do a goto() before
        self.__pwpg.emulate_media(color_scheme="dark")
        self.__url = url

    def url(self) -> str:
        return self.__url

    def open(self) -> Response:
        self.__pwpg.wait_for_load_state()
        resp = self.__pwpg.goto(self.__url)
        return PwResponse(resp.status, PwHtml(self.__pwpg), self.__url)

    def pause(self) -> None:
        self.__pwpg.wait_for_event("close", timeout=0)

    def close(self) -> None:
        self.__pwpg.close()
        self.__session.close()

    def reload(self) -> Response:
        resp = self.__pwpg.reload()
        return PwResponse(resp.status, PwHtml(self.__pwpg), self.__url)

    def scroll(self, random_wait: RandomWait) -> bool:
        random_int = RandomInt()
        scroll_height = self.__pwpg.evaluate(
            "window.document.documentElement.scrollHeight"
        )
        pixels = 0
        prev_scroll_height = 0
        while prev_scroll_height < scroll_height:
            while pixels <= scroll_height:
                pixels += random_int.value(200, 600)
                self.__pwpg.evaluate(
                    f"() => window.scrollTo(0, {pixels}, {{ behavior: 'smooth' }})"
                )
                random_wait.run()
            prev_scroll_height = scroll_height
            scroll_height = self.__pwpg.evaluate(
                "window.document.documentElement.scrollHeight"
            )
        return True


class Logged(Page):
    def __init__(self, page: Page, console: Console = StdConsole()) -> None:
        self.__origin = page
        self.__console = console

    def url(self) -> str:
        return self.__origin.url()

    def open(self) -> Response:
        zone = timezone(timedelta(hours=-3))
        timestamp = datetime.now(zone).strftime("%H:%M:%S.%f")
        self.__console.log(f"[{timestamp}] Opening '{self.url()}'... ")
        response = self.__origin.open()
        self.__console.logln("done.")
        return response

    def pause(self) -> None:
        zone = timezone(timedelta(hours=-3))
        timestamp = datetime.now(zone).strftime("%H:%M:%S.%f")
        self.__console.logln(f"[{timestamp}] Page paused!")
        self.__origin.pause()

    def close(self) -> None:
        zone = timezone(timedelta(hours=-3))
        timestamp = datetime.now(zone).strftime("%H:%M:%S.%f")
        self.__console.log(f"[{timestamp}] Closing '{self.url()}'... ")
        self.__origin.close()
        self.__console.logln("done.")

    def reload(self) -> Response:
        zone = timezone(timedelta(hours=-3))
        timestamp = datetime.now(zone).strftime("%H:%M:%S.%f")
        self.__console.log(f"[{timestamp}] Reloading '{self.url()}'... ")
        response = self.__origin.reload()
        self.__console.logln("done.")
        return response

    def scroll(self, random_wait: RandomWait) -> bool:
        zone = timezone(timedelta(hours=-3))
        timestamp = datetime.now(zone).strftime("%H:%M:%S.%f")
        self.__console.log(f"[{timestamp}] Scrolling '{self.url()}'... ")
        state = self.__origin.scroll(random_wait)
        self.__console.logln("done.")
        return state


class Retry(Page):
    def __init__(
        self,
        page: Page,
        random_wait: RandomWait = RandomWait(2, 3),
        max_retries: int = 10,
    ) -> None:
        self.__origin = page
        self.__random_wait = random_wait
        self.__max_retries = max_retries

    def url(self) -> str:
        return self.__origin.url()

    def open(self) -> Response:
        try:
            response = self.__origin.open()
        except Exception:
            response = None
            retries = 1
            while response is None and retries <= self.__max_retries:
                self.__random_wait.run()
                try:
                    response = self.__origin.reload()
                except Exception:
                    retries += 1
                    continue
                break
        return response

    def pause(self) -> None:
        self.__origin.pause()

    def close(self) -> None:
        self.__origin.close()

    def reload(self) -> Response:
        return self.__origin.reload()

    def scroll(self, random_wait: RandomWait) -> bool:
        return self.__origin.scroll(random_wait)
