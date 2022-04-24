from prettytable import PrettyTable

from Common.StockType.AbstractStock import AbstractStock
import numpy as np


class AbstractCurrency(AbstractStock):
    __ticker: str = 'NA'
    _name: str = 'NA'
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _price_to_earn: float = np.nan
    _price_to_book: float = np.nan
    _price_to_sale: float = np.nan
    _price_to_cash: float = np.nan

    def __init__(self, c_name: str):
        self._name = c_name.replace(' ', '')
        #
        self.__class = 'Currency'
        #
        self._setInfo()

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['ticker', self.__ticker])
        pt.add_row(['type', self.__class])
        pt.add_row(['name', self._name])
        pt.add_row(['StockPartCount', self._stock_part_count])
        pt.add_row(['BondPartCount', self._bond_part_count])
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
        return pt.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "Info": "StockInfo",
            "ticker": self.__ticker,
            "type": self.__class,
            "name": self._name
        }.items()

    def _setInfo(self):
        self._stock_part_count = 0
        self._bond_part_count = 0

    @property
    def Name(self):
        return self._name
