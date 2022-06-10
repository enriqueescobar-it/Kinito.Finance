from abc import *
import json
import numpy as np
from matplotlib import pyplot as plt
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
    _other_part_count: int = 0
    _pref_part_count: int = 0
    _conv_part_count: int = 0
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
        pt.add_row(['Type', self.__class])
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
            "type": self.__class,
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

    def _set_info(self):
        pass

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

    def _set_holding_df(self, any_top: any, str_ticker: str, any_sector: any):
        is_ok: bool = any(any_top) and any(any_sector)
        if is_ok:
            is_df: bool = isinstance(any_top, DataFrame)
            if is_df:
                self._holding_df = any_top
                self._holding_df.set_index('symbol', inplace=True)
                self._holding_df.reset_index(inplace=True)
                self._has_holdings = True
            else:
                s: str = (list(any_sector.values())[0]).split(' found ')[0]
                self._holding_df['symbol'] = s
                self._holding_df['holdingName'] = 'a name'
                self._holding_df['holdingPercent'] = 1.0
                self._holding_df.loc[0] = [str_ticker, s, 1.0]

    def _set_part_count(self, any_top: any, any_category: any):
        is_df: bool = any(any_top) and isinstance(any_top, DataFrame)
        df: DataFrame = DataFrame()
        stock_int: int = 0
        bond_int: int = 0
        cash_int: int = 0
        other_int: int = 0
        pref_int: int = 0
        conv_int: int = 0
        if is_df and any(any_category) and isinstance(any_category, DataFrame):
            df = any_category.set_index('maxAge')
            df.reset_index(inplace=True)
            if 'stockPosition' in df.columns:
                stock_int = round(df['stockPosition'][0] * 100)
            if 'bondPosition' in df.columns:
                bond_int = round(df['bondPosition'][0] * 100)
            if 'cashPosition' in df.columns:
                cash_int = round(df['cashPosition'][0] * 100)
            if 'otherPosition' in df.columns:
                other_int = round(df['otherPosition'][0] * 100)
            if 'preferredPosition' in df.columns:
                pref_int = round(df['preferredPosition'][0] * 100)
            if 'convertiblePosition' in df.columns:
                conv_int = round(df['convertiblePosition'][0] * 100)
        else:
            df['maxAge'] = 1.0
            df['cashPosition'] = np.nan
            df['stockPosition'] = np.nan
            df['bondPosition'] = np.nan
            df['otherPosition'] = np.nan
            df['preferredPosition'] = np.nan
            df['convertiblePosition'] = np.nan
            df.loc[0] = [1.0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
            df = df.set_index('maxAge')
            df.reset_index(inplace=True)
            stock_int = round(np.nan_to_num(df['stockPosition'][0]) * 100)
            bond_int = round(np.nan_to_num(df['bondPosition'][0]) * 100)
            cash_int = round(np.nan_to_num(df['cashPosition'][0]) * 100)
            other_int = round(np.nan_to_num(df['otherPosition'][0]) * 100)
            pref_int = round(np.nan_to_num(df['preferredPosition'][0]) * 100)
            conv_int = round(np.nan_to_num(df['convertiblePosition'][0]) * 100)
        self._stock_part_count = stock_int
        self._bond_part_count = bond_int
        self._cash_part_count = cash_int
        self._other_part_count = other_int
        self._pref_part_count = pref_int
        self._conv_part_count = conv_int

    def _is_any_null(self, a_any: any, a_str: str) -> bool:
        boo: bool = any(a_any) and (len(a_any.get(a_str)) >= 38) and (not (("Quote not found for ticker symbol:" + a_str) in str(a_any)))
        if boo:
            print("+", self.__class__.__name__, 'dict:', a_str, type(a_any), 'size', len(a_any.get(a_str)))
        return boo

    def _set_fund_holding_info(self, holding_info_dict: dict, ticker_str: str):
        if not self._is_any_null(holding_info_dict, ticker_str):
            for key in holding_info_dict.get(ticker_str):
                if key == 'equityHoldings':
                    self._set_price_to(holding_info_dict.get(ticker_str)[key])

    def _set_price_to(self, a_dict: dict):
        self._price_to_earn = a_dict['priceToEarnings']
        self._price_to_book = a_dict['priceToBook']
        self._price_to_sale = a_dict['priceToSales']
        self._price_to_cash = a_dict['priceToCashflow']

    def _set_fund_performance(self, a_any: any, a_str: str):
        if not self._is_any_null(a_any, a_str):
            for key in a_any.get(a_str):
                print("+", self.__class__.__name__, ':', key)

    def _plot_sector_df(self, class_str: str, tick_str: str):
        if (self._sector_df['Percent'] != self._sector_df['Percent'][0]).all():
            self._sector_df.plot.pie(x='Sector', y='Percent', labels=self._sector_df['Sector'], subplots=True,
                                    autopct="%.1f%%", figsize=(10, 10), fontsize=9, legend=True,
                                    title='Sector Distribution ' + tick_str + ' ' + class_str)
            return plt

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
