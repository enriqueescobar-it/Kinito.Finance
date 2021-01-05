import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pandas import DataFrame
import pandas_datareader as pdr

from Common.Measures.Time.TimeSpan import TimeSpan
from Common.StockMarketIndex.Yahoo.Wilshire5kIndex import Wilshire5kIndex
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class BuffettIndicator(AbstractTechIndicator):
    _data: DataFrame = DataFrame()
    _us_gdp: DataFrame = DataFrame()
    _wilshire_index: Wilshire5kIndex
    _time_span: TimeSpan = TimeSpan()

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._time_span = y_stock_option.TimeSpan
        self._name = 'Buffett'
        self._label += self._name
        self._main_label += ' ' + self._label
        self._setData(y_stock_option.DataFrame)

    def GetData(self) -> DataFrame:
        pass

    def PlotAx(self, ax: object) -> object:
        pass

    def PlotData(self) -> plt:
        pass

    def _setData(self, a_df: DataFrame):
        self.__setIndex()
        wilshire_quarterly: DataFrame = self.__setIndexQuarterly()
        self.__setGdp()

    def __setIndex(self):
        self._wilshire_index = Wilshire5kIndex('yahoo', "^W5000", self._time_span)
        self._wilshire_index.Data.fillna(method='ffill', inplace=True)
        self._wilshire_index.Data.fillna(method='bfill', inplace=True)
        self._wilshire_index.Data.columns = ['WIL5000']
        print('WIL', self._wilshire_index.Data.columns)

    def __setIndexQuarterly(self) -> DataFrame:
        df: DataFrame = self._wilshire_index.Data.copy()
        df.resample('3M').last()
        print('3M', df.columns)
        return df

    def __setGdp(self):
        self._us_gdp = pdr.DataReader('GDP', 'fred', self._time_span.StartDate, self._time_span.EndDate)
        self._us_gdp.fillna(method='ffill', inplace=True)
        self._us_gdp.fillna(method='bfill', inplace=True)
        print('GDP', self._us_gdp.columns)
