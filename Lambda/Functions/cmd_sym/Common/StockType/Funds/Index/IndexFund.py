import json
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
import pandas
from prettytable import PrettyTable
from yahooquery import Ticker

from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


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
        #
        self._setInfo()

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['Info', 'StockInfo'])
        pt.add_row(['ticker', self.__ticker])
        pt.add_row(['type', self.__class])
        pt.add_row(['name', self._name])
        pt.add_row(['stock_percent', self._stock_part_count])
        pt.add_row(['bond_percent', self._bond_part_count])
        pt.add_row(['price_to_earnings', self._price_to_earn])
        pt.add_row(['price_to_book', self._price_to_book])
        pt.add_row(['price_to_sales', self._price_to_sale])
        pt.add_row(['price_to_cashflow', self._price_to_cash])
        return pt.__str__()

    def __iter__(self):
        yield from {
            "Info": "StockInfo",
            "ticker": self.__ticker,
            "type": self.__class,
            "name": self._name,
            "stock_percent": self._stock_part_count,
            "bond_percent": self._bond_part_count,
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash
        }.items()
    
    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
        #return super().to_json() self.__dict__ dict(self)

    def _setInfo(self):
        pass

    @property
    def SectorDataFrame(self):
        return self._sector_df

    @property
    def HoldingDataFrame(self):
        return self._holding_df

    @property
    def StockPartCount(self):
        return self._stock_part_count

    @property
    def BondPartCount(self):
        return self._bond_part_count

    @property
    def PriceToEarnings(self):
        return self._price_to_earn

    @property
    def PriceToSales(self):
        return self._price_to_sale

    @property
    def PriceToBook(self):
        return self._price_to_book

    @property
    def PriceToCashflow(self):
        return self._price_to_cash
