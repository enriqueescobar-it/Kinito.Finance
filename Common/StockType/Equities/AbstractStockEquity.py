from prettytable import PrettyTable

from Common.StockType.AbstractStock import AbstractStock
import numpy as np
from pandas import DataFrame


class AbstractStockEquity(AbstractStock):
    _info_labels: list = list()
    _info_list: list = list()
    _name: str = 'NA'
    _pretty_table: PrettyTable = PrettyTable()
    __ticker: str = 'NA'
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _price_to_earn: float = np.nan
    _price_to_book: float = np.nan
    _price_to_sale: float = np.nan
    _price_to_cash: float = np.nan

    def __init__(self, c_name: str):
        self.__class = 'Equity'
        self._name = c_name.replace(' ', '')
        self._info_labels.append('Name')
        self._info_list.append(self._name)
        self._pretty_table.add_column('Labels', self.InfoLabels)
        self._pretty_table.add_column(self.__class, self.InfoList)

    def __str__(self):
        return self._pretty_table.__str__()

    @property
    def InfoList(self):
        return self._info_list

    @property
    def InfoLabels(self):
        return self._info_labels

    @property
    def Name(self):
        return self._name
