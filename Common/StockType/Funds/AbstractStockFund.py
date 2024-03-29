import numpy as np
from pandas import DataFrame
from prettytable import PrettyTable

from Common.StockType.AbstractStock import AbstractStock


class AbstractStockFund(AbstractStock):
    __ticker: str = 'NA'
    _name: str = 'NA'
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _price_to_earn: float = np.nan
    _price_to_book: float = np.nan
    _price_to_sale: float = np.nan
    _price_to_cash: float = np.nan

    def __init__(self, c_name: str):
        self.__class = 'Fund'
        #
        self._name = c_name.replace(' ', '')
        self._stock_part_count = 0
        self._bond_part_count = 0
        self._sector_df = DataFrame(columns=['S'])
        self._holding_df = DataFrame(columns=['H'])

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

    def __repr__(self):
        return self.__str__()

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

    @property
    def Name(self):
        return self._name

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
