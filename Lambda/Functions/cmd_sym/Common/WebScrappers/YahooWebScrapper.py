import json
import requests
import yarl

from prettytable import PrettyTable
from requests import Response

from Common.WebScrappers.AbstractWebScrapper import AbstractWebScrapper


class YahooWebScrapper(AbstractWebScrapper):
    _root_link: str = "https://finance.yahoo.com/quote/"
    _header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _ticker: str = 'NA'
    _linker: str = "http://localhost"
    _exists: bool = False
    _url: yarl.URL = yarl.URL(_linker)

    def __init__(self, a_ticker: str) -> None:
        self._ticker = a_ticker
        self._set_link()

    def __str__(self) -> str:
        self._pretty_table.field_names = self._header
        self._pretty_table.add_row(['Ticker', self._ticker])
        self._pretty_table.add_row(['Link', self._linker])
        self._pretty_table.add_row(['Exists', self._exists])
        self._pretty_table.add_row(['URL', self._url])
        return self._pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "ticker": str(self._ticker),
            "link": str(self._linker),
            "exists": self._exists,
            "url": str(self._url)
        }.items()

    def __url_exists(self, url_str: str) -> bool:
        boo: bool = False
        get_response: int = 0
        try:
            # Get Url
            get: Response = requests.get(url_str)
            get_response = get.status_code
            # if the request succeeds
            if get_response == 200:
                boo = True
                print(f"{url_str}: is reachable")
            else:
                boo = False
                print(f"{url_str}: is Not reachable, status_code: {get.status_code}")
        # Exception
        except requests.exceptions.RequestException as e:
            # print URL with Errs
            raise SystemExit(f"{url_str}: is Not reachable \nErr: {e}")
        finally:
            print('FINALLY', get_response, boo)
        return boo

    def _set_link(self):
        a_link: str = '{0}{1}'.format(self._root_link, self._ticker)
        self._exists = self.__url_exists(a_link)
        print(a_link, self._exists)
        if self._exists:
            self._linker = a_link
            self._url = yarl.URL(a_link)

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def parse_body(self):
        pass

    @property
    def ticker(self) -> str:
        return self._ticker

    @property
    def link(self) -> str:
        return self._linker

    @property
    def exists(self) -> bool:
        return self._exists

    @property
    def url(self) -> yarl.URL:
        return self._url
