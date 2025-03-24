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
import re

from fake_https_server.request import ContentGet, Fail, FileContentGet
from fake_https_server.server import Daemon, FakeHttpsServer

import arana.browser
import arana.page
from arana.browser import Chromium
from arana.console import FakeConsole
from arana.rndm import RandomWait


def test_url() -> None:
    url = "https://www.example.com"
    browser = Chromium()
    browser.open()
    page = browser.page(url)
    assert page.url() == url
    browser.close()


def test_not_open() -> None:
    browser = Chromium()
    browser.open()
    page = browser.page("https://www.example.com")
    page.close()
    browser.close()


def test_scroll() -> None:
    success_ok = 200
    server = Daemon(
        FakeHttpsServer(
            FileContentGet(
                "tests/contents/galpoes-depositos-armazens-alugar-sp.html"
            )
        )
    )
    browser = Chromium()
    browser.open()
    server.start()
    url = (
        f"https://localhost:{server.port()}/aluguel/galpao-deposito-armazem/sp/"
    )
    page = browser.page(url)
    response = page.open()
    done = page.scroll(RandomWait(0, 0))
    assert response.status() == success_ok
    assert done
    page.close()
    browser.close()
    server.stop()


def test_logged() -> None:
    server = Daemon(
        FakeHttpsServer(
            FileContentGet("tests/contents/armazem-arpoador-sp.html"),
        )
    )
    console = FakeConsole()
    browser = Chromium()
    browser.open()
    server.start()
    port = server.port()
    url = (
        f"https://localhost:{port}/imovel/aluguel-galpao-deposito"
        f"-armazem-com-cozinha-jardim-arpoador-zona-oeste-zona-oeste"
        f"-sao-paulo-sp-250m2-id-2743779110/"
    )
    page = arana.page.Logged(browser.page(url), console)
    page.open()
    page.close()
    browser.close()
    server.stop()
    assert re.search(
        r"\[[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}] Opening "
        f"'https://localhost:{port}/imovel/aluguel-galpao-deposito-armazem-com-"
        r"cozinha-jardim-arpoador-zona-oeste-zona-oeste-sao-paulo-sp-250m2-id-"
        r"2743779110/'... done.\n"
        r"\[[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}] Closing "
        f"'https://localhost:{port}/imovel/aluguel-galpao-deposito-armazem-com-"
        r"cozinha-jardim-arpoador-zona-oeste-zona-oeste-sao-paulo-sp-250m2-id-"
        r"2743779110/'... done.\n",
        console.stderr(),
    )


def test_retry() -> None:
    success_ok = 200
    retries = 1
    msg = "Retry Page Test!"
    server = Daemon(
        FakeHttpsServer(
            Fail(
                ContentGet(msg),
                retries,
            )
        )
    )
    browser = Chromium()
    browser.open()
    server.start()
    url = f"https://localhost:{server.port()}/index.html"
    page = arana.page.Retry(browser.page(url))
    response = page.open()
    assert response.status() == success_ok
    assert (
        response.html().content()
        == f"<html><head></head><body>{msg}</body></html>"
    )
    page.close()
    browser.close()
    server.stop()


def test_retry_logged() -> None:
    success_ok = 200
    retries = 1
    msg = "Retry Page Test!"
    server = Daemon(
        FakeHttpsServer(
            Fail(
                ContentGet(msg),
                retries,
            )
        )
    )
    browser = arana.browser.Logged(Chromium())
    browser.open()
    server.start()
    url = f"https://localhost:{server.port()}/index.html"
    page = arana.page.Retry(browser.page(url))
    response = page.open()
    assert response.status() == success_ok
    assert (
        response.html().content()
        == f"<html><head></head><body>{msg}</body></html>"
    )
    page.close()
    browser.close()
    server.stop()
