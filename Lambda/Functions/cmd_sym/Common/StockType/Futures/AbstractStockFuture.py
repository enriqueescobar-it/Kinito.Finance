from matplotlib import pyplot as plt
import numpy as np
from pandas import DataFrame
import pandas
from prettytable import PrettyTable
from yahooquery import Ticker

from Common.StockType.AbstractStock import AbstractStock


class AbstractStockFuture(AbstractStock):
    __y_query: Ticker
    __ticker: str = 'NA'
    _name: str = 'NA'
    #
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _price_to_earn: float = np.nan
    _price_to_book: float = np.nan
    _price_to_sale: float = np.nan
    _price_to_cash: float = np.nan

    def __init__(self, c_name: str, t_name: str, q_type: str):
        self._name = c_name.replace(' ', '')
        self.__ticker = t_name
        self.__class = 'Future'
        self._quote_type = q_type
        #
        self.__y_query = Ticker(t_name)
        #
        self._setInfo()

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        pt.add_row(['Ticker', self.__ticker])
        pt.add_row(['Type', self.__class])
        pt.add_row(['QuoteType', self._quote_type])
        pt.add_row(['Name', self._name])
        pt.add_row(['StockPartCount', self._stock_part_count])
        pt.add_row(['BondPartCount', self._bond_part_count])
        pt.add_row(['PriceToEarnings', self._price_to_earn])
        pt.add_row(['PriceToBook', self._price_to_book])
        pt.add_row(['PriceToSales', self._price_to_sale])
        pt.add_row(['PriceToCashflow', self._price_to_cash])
        s = pt.__str__() + "\n\nSECTOR DATAFRAME\n" + self._sector_df.head().to_string(index=True)
        s += "\n\nHOLDING DATAFRAME\n" + self._holding_df.head().to_string(index=True)
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
            "price_to_earnings": self._price_to_earn,
            "price_to_book": self._price_to_book,
            "price_to_sales": self._price_to_sale,
            "price_to_cashflow": self._price_to_cash
        }.items()

    def _setInfo(self):
        self.__setSectorDf()
        self.__setHoldingDf()
        self._stock_part_count, self._bond_part_count = self.__setAllocation()
        self.__setInfo()
        self.__setPerformance()
        self.__plotSectorDf()#.show()

    def __setSectorDf(self):
        is_df : bool = isinstance(self.__y_query.fund_sector_weightings, pandas.DataFrame)

        if is_df:
            self._sector_df = self.__y_query.fund_sector_weightings.reset_index()
            self._sector_df.columns = ['Sector', 'Percent']
        else:
            s: str = (list(self.__y_query.fund_sector_weightings.values())[0]).split(' found ')[0]
            self._sector_df['Sector'] = s
            self._sector_df['Percent'] = 1.0
            self._sector_df.loc[0] = [s, 1.0]
        print(self._sector_df)

    def __plotSectorDf(self) -> plt:
        self._sector_df.plot.pie(x='Sector', y='Percent', labels=self._sector_df['Sector'], subplots=True,
                                 autopct="%.1f%%", figsize=(10, 10), fontsize=9, legend=True,
                                 title='Sector Distribution ' + self.__ticker + ' ' + self.__class)
        return plt

    def __setHoldingDf(self):
        is_df : bool = isinstance(self.__y_query.fund_top_holdings, pandas.DataFrame)

        if is_df:
            self._holding_df = self.__y_query.fund_top_holdings
            self._holding_df.set_index('symbol', inplace=True)
            self._holding_df.reset_index(inplace=True)
        else:
            s: str = (list(self.__y_query.fund_sector_weightings.values())[0]).split(' found ')[0]
            self._holding_df['symbol'] = s
            self._holding_df['holdingName'] = 'a name'
            self._holding_df['holdingPercent'] = 1.0
            self._holding_df.loc[0] = [self.__ticker, s, 1.0]
        print(self._holding_df)

    def __setAllocation(self):
        is_df : bool = isinstance(self.__y_query.fund_top_holdings, pandas.DataFrame)
        df: DataFrame = DataFrame()

        if is_df:
            df = self.__y_query.fund_category_holdings.set_index('maxAge')
            df.reset_index(inplace=True)
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
        stock_int: int = int(np.nan_to_num(df['stockPosition'][0]) *100) if np.isnan(df['stockPosition'][0]) else int(df['stockPosition'][0]*100)
        #stock_int: int = int(df['stockPosition'][0]*100)
        bond_int: int = 100 - stock_int
        return stock_int, bond_int

    def __setInfo(self):
        print("SET_INFO", self.__y_query.fund_holding_info)
        is_null: bool = len(self.__y_query.fund_holding_info.get(self.__ticker)) >= 50
        if is_null:
            print(self.__ticker + ' size', len(self.__y_query.fund_holding_info.get(self.__ticker)))
        else:
            for key in self.__y_query.fund_holding_info.get(self.__ticker):
                if key == 'equityHoldings':
                    self.__setPriceTo(self.__y_query.fund_holding_info.get(self.__ticker)[key])

    def __setPriceTo(self, a_dict: dict):
        self._price_to_earn = a_dict['priceToEarnings']
        self._price_to_book = a_dict['priceToBook']
        self._price_to_sale = a_dict['priceToSales']
        self._price_to_cash = a_dict['priceToCashflow']

    def __setPerformance(self):
        print('Performance', self.__y_query.fund_performance)
        is_null: bool = len(self.__y_query.fund_performance.get(self.__ticker)) >= 50
        if is_null:
            print(self.__ticker + ' size', len(self.__y_query.fund_performance.get(self.__ticker)))
        else:
            for key in self.__y_query.fund_performance.get(self.__ticker):
                print(key)

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
