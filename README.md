# Arana

## Introduction

Arana is an abstraction layer for web scrapers. At the moment arana abstracts
Chromium, Firefox and WebKit browsers.

## Features

- Provide an abstraction layer for web scrapers
- Provide an abstraction for a browser (Chromium, Firefox or WebKit)
- Provide a strong OOP composition API usage
- Pass Cloudflare web scrap protection for sites

## How to use

Install it using `pip` command:

```bash
pip install arana
```

in your project folder.

## Usage

To access a web page using Chromium browser, you can use:

```python
# Create a new Chromium browser
browser = Chromium()
# Open the browser
browser.open()
# Create a new web page
page = browser.page(url)
# Open the web page
response = page.open()
# Get the html content
html = response.html().content()
# Close the web page
page.close()
# Close the browser
browser.close()
```

## License

The MIT License (MIT)

Copyright (C) 2025 Fabrício Barros Cabral

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
