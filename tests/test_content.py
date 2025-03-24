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
