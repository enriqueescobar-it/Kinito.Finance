from abc import *
import json
import numpy as np
from pandas import DataFrame
from prettytable import PrettyTable


class AbstractStock(ABC):
    __class: str = 'NA'
    _header: list = ['Info', 'TypeInfo']
    _quote_type: str = 'NA'
    _name: str = 'NA'
    _stock_part_count: int = 0
    _bond_part_count: int = 0
    _cash_part_count: int = 0
    _price_to_book: float = np.nan
    _price_to_cash: float = np.nan
    _price_to_earn: float = np.nan
    _price_to_sale: float = np.nan
    _has_sectors: bool = False
    _has_holdings: bool = False
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()

    def __init__(self):
        self.__class = 'TypeInfo'

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['QuoteType', self._quote_type])
        pt.add_row(['Name', self._name])
        pt.add_row(['StockPercent', self._stock_part_count])
        pt.add_row(['BondPercent', self._bond_part_count])
        pt.add_row(['CashPercent', self._cash_part_count])
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
        pt.add_row(['HasSectors', self._has_sectors])
        pt.add_row(['HasHoldings', self._has_holdings])
        s = pt.__str__()
        if self._has_sectors:
            s += "\n\nSECTOR DATAFRAME\n" + self._sector_df.to_string(index=True)
        if self._has_holdings:
            s += "\n\nHOLDING DATAFRAME\n" + self._holding_df.to_string(index=True)
        return s

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "Info": self.__class,
            "quote_type": self._quote_type,
            "name": self._name,
            "stock_percent": self._stock_part_count,
            "bond_percent": self._bond_part_count,
            "cash_percent": self._cash_part_count,
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash,
            "has_sectors": self._has_sectors,
            "has_holdings": self._has_holdings
        }.items()

    def _set_sector_df(self, a_any: any):
        is_any: bool = any(a_any)
        if not is_any:
            self._sector_df = DataFrame()
        else:
            is_df: bool = isinstance(a_any, DataFrame)
            if is_df:
                self._sector_df = a_any.reset_index()
                self._sector_df.columns = ['Sector', 'Percent']
                self._has_sectors = True
            else:
                s: str = (list(a_any.values())[0]).split(' found ')[0]
                self._sector_df['Sector'] = s
                self._sector_df['Percent'] = 1.0
                self._sector_df.loc[0] = [s, 1.0]

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def Name(self):
        return self._name

    @property
    def StockPartCount(self):
        return self._stock_part_count

    @property
    def BondPartCount(self):
        return self._bond_part_count

    @property
    def CashPartCount(self):
        return self._cash_part_count

    @property
    def PriceToBook(self):
        return self._price_to_book

    @property
    def PriceToCashflow(self):
        return self._price_to_cash

    @property
    def PriceToEarnings(self):
        return self._price_to_earn

    @property
    def PriceToSales(self):
        return self._price_to_sale

    @property
    def HasSectors(self):
        return self._has_sectors

    @property
    def HasHoldings(self):
        return self._has_holdings

    @property
    def SectorDataFrame(self):
        return self._sector_df

    @property
    def HoldingDataFrame(self):
        return self._holding_df
