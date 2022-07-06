import bs4
import requests

from Common.WebScrappers.YahooWebScrapper import YahooWebScrapper


class YahooSummaryWebScrapper(YahooWebScrapper):
    _request: str = 'NA'
    _html_parser: bs4.BeautifulSoup
    _html_body: bs4.ResultSet
    _range_1d: str = 'NA'
    _range_52w: str = 'NA'
    _market_cap: str = 'NA'
    _beta: str = 'NA'
    _pe_ratio: str = 'NA'
    _eps: str = 'NA'
    _earnings_date: str = 'NA'
    _f_dividend_yield: str = 'NA'
    _ex_dividend_date: str = 'NA'

    def __init__(self, a_ticker: str):
        super().__init__(a_ticker)
        if self.exists:
            self.__set_request()
            self.__set_html_parser()
            self.__set_html_body()
            self.parse_body()

    def __str__(self) -> str:
        self._pretty_table.field_names = self._header
        self._pretty_table.add_row(['Ticker', self._ticker])
        self._pretty_table.add_row(['URL', self._url])
        self._pretty_table.add_row(['Range1Day', self._range_1d])
        self._pretty_table.add_row(['Range52Week', self._range_52w])
        self._pretty_table.add_row(['MarketCap', self._market_cap])
        self._pretty_table.add_row(['Beta', self._beta])
        self._pretty_table.add_row(['RatioPE', self._pe_ratio])
        self._pretty_table.add_row(['EPS', self._eps])
        self._pretty_table.add_row(['EarningsDate', self._earnings_date])
        self._pretty_table.add_row(['ForwardDividend&Yield', self._f_dividend_yield])
        self._pretty_table.add_row(['ExDividendDate', self._ex_dividend_date])
        return self._pretty_table.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "ticker": str(self._ticker),
            "url": str(self._url),
            "range_1d": self._range_1d,
            "range_52w": self._range_52w,
            "market_cap": self._market_cap,
            "beta": self._beta,
            "pe_ratio": self._pe_ratio,
            "eps": self._eps,
            "earnings_date": self._earnings_date,
            "f_dividend_yield": self._f_dividend_yield,
            "ex_dividend_date": self._ex_dividend_date
        }.items()

    def __has_dict_key(self, a_dict: dict, a_key: str = '') -> bool:
        return a_key in a_dict

    def __get_dict_key(self, a_dict: dict, a_key: str = '') -> str:
        return 'NA' if not self.__has_dict_key(a_dict, a_key) else str(a_dict[a_key])

    def __set_request(self):
        self._request = requests.get(self.link).text

    def __set_html_parser(self):
        self._html_parser = bs4.BeautifulSoup(self._request, 'html.parser')

    def __set_html_body(self):
        self._html_body = self._html_parser.find_all("tbody")

    def parse_body(self):
        l = {}
        u = list()
        try:
            table1 = self._html_body[0].find_all("tr")
        except:
            table1 = None
        try:
            table2 = self._html_body[1].find_all("tr")
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
        self._range_1d = self.__get_dict_key(u[:][4], "Day's Range")
        self._range_52w = self.__get_dict_key(u[:][5], '52 Week Range')
        self._market_cap = self.__get_dict_key(u[:][8], 'Market Cap')
        self._beta = self.__get_dict_key(u[:][9], 'Beta (5Y Monthly)')
        self._pe_ratio = self.__get_dict_key(u[:][10], 'PE Ratio (TTM)')
        self._eps = self.__get_dict_key(u[:][11], 'EPS (TTM)')
        self._earnings_date = self.__get_dict_key(u[:][12], 'Earnings Date')
        self._f_dividend_yield = self.__get_dict_key(u[:][13], 'Forward Dividend & Yield')
        self._ex_dividend_date = self.__get_dict_key(u[:][14], 'Ex-Dividend Date')

    @property
    def beta(self) -> str:
        return self._beta

    @property
    def eps(self) -> str:
        return self._eps

    @property
    def earnings_date(self) -> str:
        return self._earnings_date

    @property
    def market_cap(self) -> str:
        return self._market_cap

    @property
    def pe_ratio(self) -> str:
        return self._pe_ratio
