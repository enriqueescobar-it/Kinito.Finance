from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from yahooquery import Ticker
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable


class ExchangeTradedFund(AbstractStockFund):
    __pretty_table: PrettyTable = PrettyTable()
    _info_labels: list = list()
    _info_list: list = list()
    _name: str = 'NA'
    __ticker: str = 'NA'
    __y_query: Ticker
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _price_to_earn: float = np.nan
    _price_to_book: float = np.nan
    _price_to_sale: float = np.nan
    _price_to_cash: float = np.nan

    def __init__(self, c_name: str, t_name: str):
        self.__class = 'Etf'
        self._name = c_name.replace(' ', '')
        self._info_labels.append('Name')
        self._info_list.append(self._name)
        self.__ticker = t_name
        self.__y_query = Ticker(t_name)
        self._setInfo()
        self.__pretty_table.add_column('Labels', self.InfoLabels)
        self.__pretty_table.add_column(self.__class, self.InfoList)

    def __str__(self) -> str:
        return self.__pretty_table.__str__()

    def _setInfo(self):
        self.__setSectorDf()
        self.__setHoldingDf()
        self._stock_part_count, self._bond_part_count = self.__setAllocation()
        self.__setInfo()
        self.__setPerformance()
        # print('1', self.__y_query.fund_bond_holdings)
        # print('2', self.__y_query.fund_bond_ratings)
        # print('4', self.__y_query.fund_equity_holdings)
        # print('7', self.__y_query.fund_ownership)
        self.__plotSectorDf().show()

    def __setSectorDf(self):
        self._sector_df = self.__y_query.fund_sector_weightings.reset_index()
        self._sector_df.columns = ['Sector', 'Percent']

    def __plotSectorDf(self) -> plt:
        self._sector_df.plot.pie(x='Sector', y='Percent', labels=self._sector_df['Sector'], subplots=True,
                                 autopct="%.1f%%", figsize=(10, 10), fontsize=9, legend=True,
                                 title='Sector Distribution ' + self.__ticker + ' ' + self.__class)
        return plt

    def __setHoldingDf(self):
        self._holding_df = self.__y_query.fund_top_holdings
        self._holding_df.set_index('symbol', inplace=True)
        self._holding_df.reset_index(inplace=True)

    def __setAllocation(self):
        df: DataFrame = self.__y_query.fund_category_holdings.set_index('maxAge')
        df.reset_index(inplace=True)
        stock_int: int = int(df['stockPosition'][0]*100)
        self._info_labels.append('StockPartCount')
        self._info_list.append(stock_int)
        bond_int: int = 100 - stock_int
        self._info_labels.append('BondPartCount')
        self._info_list.append(bond_int)
        return stock_int, bond_int

    def __setInfo(self):
        for key in self.__y_query.fund_holding_info.get(self.__ticker):
            if key == 'equityHoldings':
                self.__setPriceTo(self.__y_query.fund_holding_info.get(self.__ticker)[key])

    def __setPriceTo(self, a_dict: dict):
        self._price_to_earn = a_dict['priceToEarnings']
        self._info_labels.append('PriceToEarnings')
        self._info_list.append(self._price_to_earn)
        self._price_to_book = a_dict['priceToBook']
        self._info_labels.append('PriceToBook')
        self._info_list.append(self._price_to_book)
        self._price_to_sale = a_dict['priceToSales']
        self._info_labels.append('PriceToSales')
        self._info_list.append(self._price_to_sale)
        self._price_to_cash = a_dict['priceToCashflow']
        self._info_labels.append('PriceToCashflow')
        self._info_list.append(self._price_to_cash)

    def __setPerformance(self):
        print('Performance', self.__y_query.fund_performance)
        for key in self.__y_query.fund_performance.get(self.__ticker):
            print(key)

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
