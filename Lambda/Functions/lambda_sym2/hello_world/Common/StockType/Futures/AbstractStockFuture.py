import numpy as np
from pandas import DataFrame

from Common.StockType.AbstractStock import AbstractStock


class AbstractStockFuture(AbstractStock):
    _info_labels: list = list()
    _info_list: list = list()
    _name: str = 'NA'
    __ticker: str = 'NA'
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _price_to_earn: float = np.nan
    _price_to_book: float = np.nan
    _price_to_sale: float = np.nan
    _price_to_cash: float = np.nan

    def __init__(self, c_name: str, t_name: str):
        self._name = c_name.replace(' ', '')
        self.__ticker = t_name
        self.__class = 'Future'
        #
        self._info_labels.append('Name')
        self._info_list.append(self._name)
        #
        self._setInfo()
        self._pretty_table.add_column('Labels', self.InfoLabels)
        self._pretty_table.add_column(self.__class, self.InfoList)

    def __str__(self):
        return self._pretty_table.__str__()

    def _setInfo(self):
        self._info_labels.append('StockPartCount')
        self._stock_part_count = 0
        self._info_list.append(self._stock_part_count)
        self._info_labels.append('BondPartCount')
        self._bond_part_count = 0
        self._info_list.append(self._bond_part_count)
        self._info_labels.append('PriceToEarnings')
        self._info_list.append(self._price_to_earn)
        self._info_labels.append('PriceToBook')
        self._info_list.append(self._price_to_book)
        self._info_labels.append('PriceToSales')
        self._info_list.append(self._price_to_sale)
        self._info_labels.append('PriceToCashflow')
        self._info_list.append(self._price_to_cash)

    @property
    def InfoList(self):
        return self._info_list

    @property
    def InfoLabels(self):
        return self._info_labels

    @property
    def Name(self):
        return self._name
