from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
import numpy as np
from pandas import DataFrame


class IndexFund(AbstractStockFund):
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
        super().__init__(c_name.replace(' ', ''))
        self.__ticker = t_name
        self.__class = 'Index'
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
        self._info_labels.append('PriceToEarnings')
        self._info_list.append(self._price_to_earn)
        self._info_labels.append('PriceToBook')
        self._info_list.append(self._price_to_book)
        self._info_labels.append('PriceToSales')
        self._info_list.append(self._price_to_sale)
        self._info_labels.append('PriceToCashflow')
        self._info_list.append(self._price_to_cash)
