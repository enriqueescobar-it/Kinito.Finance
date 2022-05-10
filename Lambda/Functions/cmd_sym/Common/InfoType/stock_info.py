import json

import yfinance as yf
from prettytable import PrettyTable

from Common.InfoType.abstract_info import abstract_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency
from Common.StockType.Currencies.Regular.RegularCurrency import RegularCurrency
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity
from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund
from Common.StockType.Funds.Index.IndexFund import IndexFund
from Common.StockType.Funds.Mutual.MutualFund import MutualFund
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture


class stock_info(abstract_info):
    __ticker: str = 'NA'
    __yFinance: yf.ticker.Ticker
    __y_fin_dic: dict = {}
    __header: list = ['Info', 'StockInfo']
    _company_name: str = 'NA'
    _quote_type: str = 'NA'
    _stock_type: AbstractStock

    def __init__(self, a_ticker: str = 'AAPL'):
        self.__ticker = a_ticker
        self.__yFinance = yf.Ticker(a_ticker)
        if '_info' in self.__yFinance.__dict__ or hasattr(self.__yFinance, '_info'):
            # if self.__yFinance.__dict__['_info'] is not None:
            self.__y_fin_dic = self.__yFinance.info
            self.__get_info()

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self.__header
        pt.add_row(['Ticker', self.__ticker])
        pt.add_row(['CompanyName', self._company_name])
        pt.add_row(['QuoteType', self._quote_type])
        return pt.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            "company_name": self._company_name,
            "quote_type": self._quote_type
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __get_info(self):
        if any(self.__y_fin_dic):
            #print(self.__y_fin_dic)
            self._company_name = self.__get_str_from_key('shortName')
            self._quote_type = self.__get_str_from_key('quoteType')
            self.__get_stock_type(self._quote_type)

    def __get_str_from_key(self, a_key: str = 'NA') -> str:
        if a_key in self.__y_fin_dic:
            return 'None' if self.__y_fin_dic[a_key] is None else self.__y_fin_dic[a_key]
        else:
            return 'NA'

    def __get_stock_type(self, s: str = ''):
        if s == 'ETF':
            self._stock_type = ExchangeTradedFund(self._company_name, self.__ticker)
        if s == 'INDEX':
            self._stock_type = IndexFund(self._company_name, self.__ticker)
        if s == 'MUTUALFUND':
            self._stock_type = MutualFund(self._company_name, self.__ticker)
        if s == 'CRYPTOCURRENCY':
            self._stock_type = CryptoCurrency(self._company_name, self.__ticker)
        if s == 'CURRENCY':
            self._stock_type = RegularCurrency(self._company_name, self.__ticker)
        if s == 'FUTURE':
            self._stock_type = AbstractStockFuture(self._company_name, self.__ticker)
        if s == 'EQUITY':
            self._stock_type = AbstractStockEquity(self._company_name, self.__ticker)
        #else:
        #    self._stock_type = AbstractStockOption(self.CompanyName, self.__ticker)
        #    self._stock_type = AbstractStockBond(self.CompanyName, self.__ticker)

    @property
    def CompanyName(self):
        return self._company_name

    @property
    def QuoteType(self):
        return self._quote_type

    @property
    def StockType(self):
        return self._stock_type
