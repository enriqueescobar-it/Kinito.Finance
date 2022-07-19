import json

import numpy as np
import yahoo_fin.stock_info as si
from pandas import DataFrame
from prettytable import PrettyTable

from Common.Readers.Engine.AbstractEngine import AbstractEngine


class YahooFinEngine(AbstractEngine):
    _header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _df: DataFrame = DataFrame()
    _quote_dict: dict = {}
    _ticker: str = 'CNI'
    _ratio_pe: float = np.nan
    _ratio_fpe: float = np.nan
    _ratio_peg: float = np.nan
    _price_to_book: float = np.nan
    _price_to_earn: float = np.nan
    _price_to_sales: float = np.nan

    def __init__(self, a_ticker: str = 'CNI'):
        self._ticker = a_ticker
        self._quote_dict = si.get_quote_table(a_ticker)
        print(self._quote_dict)
        self._df = si.get_stats_valuation(a_ticker)
        self._df = self._df.iloc[:, :2]
        self._df.columns = ['Attribute', 'Recent']
        self._ratio_pe = float(self._df[self._df.Attribute.str.contains('Trailing P/E')].iloc[0, 1])
        self._ratio_fpe = float(self._df[self._df.Attribute.str.contains('Forward P/E')].iloc[0, 1])
        self._ratio_peg = float(self._df[self._df.Attribute.str.contains('PEG')].iloc[0, 1])
        self._price_to_book = float(self._df[self._df.Attribute.str.contains('Price/Book')].iloc[0, 1])
        self._price_to_earn = float(self._df[self._df.Attribute.str.contains('Trailing P/E')].iloc[0, 1])
        self._price_to_sales = float(self._df[self._df.Attribute.str.contains('Price/Sales')].iloc[0, 1])

    def __str__(self) -> str:
        self._pretty_table.field_names = self._header
        self._pretty_table.add_row(['Ticker', self._ticker])
        self._pretty_table.add_row(['RatioPE', self._ratio_pe])
        self._pretty_table.add_row(['RatioFPE', self._ratio_fpe])
        self._pretty_table.add_row(['RatioPEG', self._ratio_peg])
        self._pretty_table.add_row(['PriceToBook', self._price_to_book])
        self._pretty_table.add_row(['PriceToEarnings', self._price_to_earn])
        self._pretty_table.add_row(['PriceToSales', self._price_to_sales])
        return self._pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "ticker": self._ticker,
            "ratio_pe": self._ratio_pe,
            "ratio_fpe": self._ratio_fpe,
            "ratio_peg": self._ratio_peg,
            "price_to_book": self._price_to_book,
            "price_to_earn": self._price_to_earn,
            "price_to_sales": self._price_to_sales
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def ratio_pe(self):
        return self._ratio_pe

    @property
    def ratio_fpe(self):
        return self._ratio_fpe

    @property
    def ratio_peg(self):
        return self._ratio_peg

    @property
    def price_to_book(self):
        return self._price_to_book

    @property
    def price_to_earnings(self):
        return self._price_to_earn

    @property
    def price_to_sales(self):
        return self._price_to_sales
