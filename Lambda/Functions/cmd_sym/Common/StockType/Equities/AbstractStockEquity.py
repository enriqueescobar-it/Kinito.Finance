import numpy as np
from pandas import DataFrame
from yahooquery import Ticker

from Common.StockType.AbstractStock import AbstractStock
from Common.Readers.Engine.YahooFinStockInfo import YahooFinStockInfo


class AbstractStockEquity(AbstractStock):
    _info_labels: list = list()
    _info_list: list = list()
    _name: str = 'NA'
    __ticker: str = 'NA'
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
        self.__pretty_table.add_column('Labels', self.InfoLabels)
        self.__pretty_table.add_column(self.__class, self.InfoList)

    def __str__(self):
        return self.__pretty_table.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "type": self.__class,
            "name": self._name,
            "ticker": self.__ticker,
            "stock_percent": self._stock_part_count,
            "bond_percent": self._bond_part_count,
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash
        }.items()

    def _setInfo(self):
        self._stock_part_count = 100
        self._info_labels.append('StockPartCount')
        self._info_list.append(self._stock_part_count)
        self._bond_part_count = 0
        self.__setInfo()
        self._info_labels.append('BondPartCount')
        self._info_list.append(self._bond_part_count)
        self._info_labels.append('PriceToEarnings')
        self._info_list.append(self._price_to_earn)
        self._info_labels.append('PriceToBook')
        self._info_list.append(self._price_to_book)
        self._info_labels.append('PriceToSales')
        self._info_list.append(self._price_to_sale)
        self._info_labels.append('PriceToCashflow')
        self._info_list.append(self._price_to_cash)

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
    def InfoList(self):
        return self._info_list

    @property
    def InfoLabels(self):
        return self._info_labels

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
