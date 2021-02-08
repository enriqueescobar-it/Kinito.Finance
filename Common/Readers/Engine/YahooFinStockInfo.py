import numpy as np
import yahoo_fin.stock_info as si
from pandas import DataFrame

from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinStockInfo(AbstractEngine):
    __val: DataFrame = DataFrame()
    __quote: dict
    __ticker: str = 'CNI'
    __pe_ratio: float = np.nan
    __fpe_ratio: float = np.nan
    __peg_ratio: float = np.nan
    __price_to_book: float = np.nan
    __price_to_earn: float = np.nan
    __price_to_sales: float = np.nan

    def __init__(self, a_ticker: str = 'CNI'):
        self.__ticker = a_ticker
        self.__quote = si.get_quote_table(a_ticker)
        self.__val = si.get_stats_valuation(a_ticker)
        self.__val = self.__val.iloc[:, :2]
        self.__val.columns = ['Attribute', 'Recent']
        self.__pe_ratio = float(self.__val[self.__val.Attribute.str.contains('Trailing P/E')].iloc[0, 1])
        self.__fpe_ratio = float(self.__val[self.__val.Attribute.str.contains('Forward P/E')].iloc[0, 1])
        self.__peg_ratio = float(self.__val[self.__val.Attribute.str.contains('PEG')].iloc[0, 1])
        self.__price_to_book = float(self.__val[self.__val.Attribute.str.contains('Price/Book')].iloc[0, 1])
        self.__price_to_earn = float(self.__val[self.__val.Attribute.str.contains('Trailing P/E')].iloc[0, 1])
        self.__price_to_sales = float(self.__val[self.__val.Attribute.str.contains('Price/Sales')].iloc[0, 1])

    @property
    def PeRatio(self):
        return self.__pe_ratio

    @property
    def FpeRatio(self):
        return self.__fpe_ratio

    @property
    def PegRatio(self):
        return self.__peg_ratio

    @property
    def PriceToBook(self):
        return self.__price_to_book

    @property
    def PriceToEarnings(self):
        return self.__price_to_earn

    @property
    def PriceToSales(self):
        return self.__price_to_sales
