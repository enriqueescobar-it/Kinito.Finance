from typing import Any, List

import bs4
import requests

from bs4.element import ResultSet

from Common.WebScrappers.YahooWebScrapper import YahooWebScrapper


class YahooSummaryWebScrapper(YahooWebScrapper):
    __request: str = 'NA'
    __html_parser: bs4.BeautifulSoup
    __html_body: ResultSet[Any]
    _market_cap: str = 'NA'
    _beta: str = 'NA'
    _pe_ratio: str = 'NA'
    _eps: str = 'NA'
    _earnings_date: str = 'NA'

    def __init__(self, a_ticker: str):
        super().__init__(a_ticker)
        if self.exists:
            self.__set_request()
            self.__set_html_parser()
            self.__set_html_body()

    def __has_dict_key(self, a_dict: dict, a_key: str = '') -> bool:
        return a_key in a_dict

    def __get_dict_key(self, a_dict: dict, a_key: str = '') -> str:
        return 'NA' if not self.__has_dict_key(a_dict, a_key) else str(a_dict[a_key])

    def __set_request(self):
        self.__request = requests.get(self.link).text

    def __set_html_parser(self):
        self.__html_parser = bs4.BeautifulSoup(self.__request, 'html.parser')

    def __set_html_body(self):
        self.__html_body = self.__html_parser.find_all("tbody")

    def parse_body(self):
        l: dict = {}
        u = list()
        try:
            table1 = self.__html_body[0].find_all("tr")
        except:
            table1 = None
        try:
            table2 = self.__html_body[1].find_all("tr")
        except:
            table2 = None
        for i in range(0, len(table1)):
            try:
                table1_td = table1[i].find_all("td")
            except:
                table1_td = None
            l[table1_td[0].text] = table1_td[1].text
            u.append(l)
            l = {}
        for i in range(0, len(table2)):
            try:
                table2_td = table2[i].find_all("td")
            except:
                table2_td = None
            l[table2_td[0].text] = table2_td[1].text
            u.append(l)
            l = {}
        self._market_cap = self.__get_dict_key(u[:][8], 'Market Cap')
        self._beta = self.__get_dict_key(u[:][9], 'Beta (5Y Monthly)')
        self._pe_ratio = self.__get_dict_key(u[:][10], 'PE Ratio (TTM)')
        self._eps = self.__get_dict_key(u[:][11], 'EPS (TTM)')
        self._earnings_date = self.__get_dict_key(u[:][12], 'Earnings Date')
