import numpy as np
from pandas import DataFrame
from prettytable import PrettyTable
from yahooquery import Ticker

from Common.StockType.AbstractStock import AbstractStock
from Common.Readers.Engine.YahooFinStockInfo import YahooFinStockInfo


class AbstractStockEquity(AbstractStock):
    __ticker: str = 'NA'
    _name: str = 'NA'
    __y_query: Ticker
    __yfsi: YahooFinStockInfo
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _price_to_book: float = np.nan
    _price_to_cash: float = np.nan
    _price_to_earn: float = np.nan
    _price_to_sale: float = np.nan

    def __init__(self, c_name: str, t_name: str):
        self._name = c_name.replace(' ', '')
        self.__ticker = t_name
        self.__class = 'Equity'
        #
        self._info_labels.append('Name')
        self._info_list.append(self._name)
        self.__y_query = Ticker(t_name)
        self.__yfsi = YahooFinStockInfo(t_name)
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
            "name": self._name,
            "stock_percent": self._stock_part_count,
            "bond_percent": self._bond_part_count,
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash
        }.items()

    def _setInfo(self):
        self._stock_part_count = 100
        self._bond_part_count = 0
        self.__setInfo()

    def __setInfo(self):
        self._price_to_book = self.__yfsi.PriceToBook
        self._price_to_earn = self.__yfsi.PriceToEarnings
        self._price_to_sale = self.__yfsi.PriceToSales
        '''
        "maxAge": 1,
        "priceHint": 2,
        "enterpriseValue": 1672450801664,
        "forwardPE": 25.70207,
        "profitMargins": 0.21350001,
        "floatShares": 4329740605,
        "sharesOutstanding": 4334329856,
        "sharesShort": 35234606,
        "sharesShortPriorMonth": 34828293,
        "sharesShortPreviousMonthDate": "2020-06-15 00:00:00",
        "dateShortInterest": "2020-07-15 00:00:00",
        "sharesPercentSharesOut": 0.0081,
        "heldPercentInsiders": 0.00066,
        "heldPercentInstitutions": 0.62115,
        "shortRatio": 0.96,
        "shortPercentOfFloat": 0.0081,
        "beta": 1.182072,
        "category": null,
        "bookValue": 18.137,
        "priceToBook": 21.214094,
        "fundFamily": null,
        "legalType": null,
        "lastFiscalYearEnd": "2019-09-28 00:00:00",
        "nextFiscalYearEnd": "2021-09-28 00:00:00",
        "mostRecentQuarter": "2020-03-28 00:00:00",
        "earningsQuarterlyGrowth": -0.027,
        "netIncomeToCommon": 57215000576,
        "trailingEps": 12.728,
        "forwardEps": 14.97,
        "pegRatio": 2.78,
        "lastSplitFactor": "7:1",
        "lastSplitDate": "2014-06-09 00:00:00",
        "enterpriseToRevenue": 6.241,
        "enterpriseToEbitda": 21.634,
        "52WeekChange": 0.8239218,
        "SandP52WeekChange": 0.103224516
        '''

    @property
    def Name(self):
        return self._name

    @property
    def HoldingDataFrame(self):
        return self._holding_df

    @property
    def SectorDataFrame(self):
        return self._sector_df

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
