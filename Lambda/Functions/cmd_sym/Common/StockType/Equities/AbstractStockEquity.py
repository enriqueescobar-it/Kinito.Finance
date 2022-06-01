from matplotlib import pyplot as plt
import numpy as np
from pandas import DataFrame
import pandas
from prettytable import PrettyTable
from yahooquery import Ticker

from Common.StockType.AbstractStock import AbstractStock
from Common.Readers.Engine.YahooFinStockInfo import YahooFinStockInfo


class AbstractStockEquity(AbstractStock):
    __ticker: str = 'NA'
    __y_query: Ticker
    __yfsi: YahooFinStockInfo
    _name: str = 'NA'
    _has_sectors: bool = False
    _has_holdings: bool = False
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _cash_part_count: int = -1
    _price_to_book: float = np.nan
    _price_to_cash: float = np.nan
    _price_to_earn: float = np.nan
    _price_to_sale: float = np.nan

    def __init__(self, c_name: str, t_name: str, q_type: str):
        self._name = c_name.replace(' ', '')
        self.__ticker = t_name
        self.__class = 'Equity'
        self._quote_type = q_type
        #
        self.__y_query = Ticker(t_name)
        self.__yfsi = YahooFinStockInfo(t_name)
        self._setInfo()

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['Info', 'StockInfo'])
        pt.add_row(['Ticker', self.__ticker])
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
            "Info": "StockInfo",
            "ticker": self.__ticker,
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

    def _setInfo(self):
        self.__setSectorDf()
        self.__setHoldingDf()
        self._stock_part_count = 0
        self._bond_part_count = 0
        self._stock_part_count, self._bond_part_count, self._cash_part_count = self.__setAllocation()
        self.__setInfo()
        self.__setPerformance()
        self.__plotSectorDf()#.show()

    def __setSectorDf(self):
        is_df: bool = isinstance(self.__y_query.fund_sector_weightings, pandas.DataFrame)

        if is_df:
            self._sector_df = self.__y_query.fund_sector_weightings.reset_index()
            self._sector_df.columns = ['Sector', 'Percent']
            self._has_sectors = True
        else:
            s: str = (list(self.__y_query.fund_sector_weightings.values())[0]).split(' found ')[0]
            self._sector_df['Sector'] = s
            self._sector_df['Percent'] = 1.0
            self._sector_df.loc[0] = [s, 1.0]

    def __plotSectorDf(self) -> plt:
        if (self._sector_df['Percent'] != self._sector_df['Percent'][0]).all():
            self._sector_df.plot.pie(x='Sector', y='Percent', labels=self._sector_df['Sector'], subplots=True,
                                    autopct="%.1f%%", figsize=(10, 10), fontsize=9, legend=True,
                                    title='Sector Distribution ' + self.__ticker + ' ' + self.__class)
            return plt

    def __setHoldingDf(self):
        is_df: bool = isinstance(self.__y_query.fund_top_holdings, pandas.DataFrame)

        if is_df:
            self._holding_df = self.__y_query.fund_top_holdings
            self._holding_df.set_index('symbol', inplace=True)
            self._holding_df.reset_index(inplace=True)
            self._has_holdings = True
        else:
            s: str = (list(self.__y_query.fund_sector_weightings.values())[0]).split(' found ')[0]
            self._holding_df['symbol'] = s
            self._holding_df['holdingName'] = 'a name'
            self._holding_df['holdingPercent'] = 1.0
            self._holding_df.loc[0] = [self.__ticker, s, 1.0]

    def __setAllocation(self):
        is_df: bool = isinstance(self.__y_query.fund_top_holdings, pandas.DataFrame)
        df: DataFrame = DataFrame()
        stock_int: int = 0
        bond_int: int = 0
        cash_int: int = 0

        if is_df:
            df = self.__y_query.fund_category_holdings.set_index('maxAge')
            df.reset_index(inplace=True)
            stock_int = int(df['stockPosition'][0] * 100)
            bond_int = int(df['bondPosition'][0] * 100)
            if 'cashPosition' in df.columns:
                cash_int = int(df['cashPosition'][0] * 100)
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
            stock_int = int(np.nan_to_num(df['stockPosition'][0]) * 100)
            bond_int = int(np.nan_to_num(df['bondPosition'][0]) * 100)
            cash_int = int(np.nan_to_num(df['cashPosition'][0]) * 100)
        return stock_int, bond_int, cash_int

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

    def __setPerformance(self):
        is_null: bool = len(self.__y_query.fund_performance.get(self.__ticker)) >= 50

        if is_null:
            print("+", self.__class__.__name__, ':', self.__ticker + ' size', len(self.__y_query.fund_performance.get(self.__ticker)))
        else:
            for key in self.__y_query.fund_performance.get(self.__ticker):
                print("+", self.__class__.__name__, ':', key)

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
    def CashPartCount(self):
        return self._cash_part_count

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

    @property
    def HasSectors(self):
        return self._has_sectors

    @property
    def HasHoldings(self):
        return self._has_holdings
