from prettytable import PrettyTable

from Common.StockType.AbstractStock import AbstractStock
import numpy as np


class AbstractCurrency(AbstractStock):
    __ticker: str = 'NA'
    _name: str = 'NA'

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
