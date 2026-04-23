# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
from fake_https_server.request import ContentGet
from fake_https_server.server import Daemon, FakeHttpsServer

from arana.browser import Chromium
from arana.content import ContentText


def test_refine() -> None:
    success_ok = 200
    text = "It works!"
    browser = Chromium()
    browser.open()
    server = Daemon(FakeHttpsServer(ContentGet(text)))
    server.start()
    url = f"https://localhost:{server.port()}"
    page = browser.page(url)
    response = page.open()
    result = ContentText(url).refine(response)
    assert response.status() == success_ok
    assert result["text"] == text
    page.close()
    server.stop()
    browser.close()
