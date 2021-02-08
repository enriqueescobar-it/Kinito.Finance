from typing import Optional

import yahoo_fin.stock_info as si
import numpy as np
from pandas import DataFrame

from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinStockInfo(AbstractEngine):
    _val: Optional[DataFrame]
    _quote: dict
    _ticker: str = 'CNI'
    _pe_ratio: float = np.nan
    _price_to_sales: float = np.nan
    _price_to_book: float = np.nan

    def __init__(self, a_ticker: str = 'CNI'):
        self._ticker = a_ticker
        self._quote = si.get_quote_table(a_ticker)
        self._val = si.get_stats_valuation('TSLA')
        self._val = self._val.iloc[:, :2]
        self._val.columns = ['Attribute', 'Recent']
        self._pe_ratio = float(self._val[self._val.Attribute.str.contains('Trailing P/E')].iloc[0, 1])
        self._price_to_sales = float(self._val[self._val.Attribute.str.contains('Price/Sales')].iloc[0, 1])
        self._price_to_book = float(self._val[self._val.Attribute.str.contains('Price/Book')].iloc[0, 1])
