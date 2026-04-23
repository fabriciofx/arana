# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
from abc import ABC, abstractmethod

from arana.html import Html, PlainHtml


class Response(ABC):
    @abstractmethod
    def status(self) -> int:
        pass

    @abstractmethod
    def html(self) -> Html:
        pass

    @abstractmethod
    def url(self) -> str:
        pass


class PwResponse(Response):
    def __init__(self, status: int, html: Html, url: str) -> None:
        self.__status = status
        self.__html = html
        self.__url = url

    def status(self) -> int:
        return self.__status

    def html(self) -> Html:
        return self.__html

    def url(self) -> str:
        return self.__url


class NotFoundResponse(Response):
    def __init__(self, url: str) -> None:
        self.__url = url

    def status(self) -> int:
        return 404

    def html(self) -> Html:
        return PlainHtml("<html><body><h1>Not Found</h1></body></html>")

    def url(self) -> str:
        return self.__url
