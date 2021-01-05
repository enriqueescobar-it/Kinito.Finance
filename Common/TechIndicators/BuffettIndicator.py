import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pandas import DataFrame
import pandas as pd
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
        self._label = self._name + self._label
        self._main_label += ' ' + self._label
        self._setData(y_stock_option.DataFrame)

    def GetData(self) -> DataFrame:
        return self._data

    def PlotAx(self, ax: object) -> object:
        an_alpha: float = 1.0
        self._data[self._label].plot(alpha=an_alpha, ax=ax)
        return ax

    def PlotData(self) -> plt:
        plt.figure(figsize=self._fig_size)
        plt.style.use(self._plot_style)
        colors = cm.coolwarm
        an_alpha: float = 1.0
        self._data[self._label].plot(alpha=an_alpha)
        #for a_ind, col in enumerate(self._data.columns[-2:self._data.columns.size]):
        #    an_alpha: float = 0.5 if a_ind != 0 else 1.0
        #    self._data[col].plot(alpha=an_alpha)
        plt.title(self._main_label)
        plt.xlabel(self._x_label)
        plt.xticks(rotation=self._x_ticks_angle)
        plt.ylabel(self._y_label)
        plt.legend(loc=self._legend_place)
        plt.grid(True)
        plt.tight_layout()
        return plt

    def _setData(self, a_df: DataFrame):
        self.__setIndex()
        wilshire_quarterly: DataFrame = self.__setIndexQuarterly()
        self.__setGdp()
        self._data = pd.merge(wilshire_quarterly, self._us_gdp, left_index=True, right_index=True)
        # Multiply the Wilshire 5000 Full Cap index by $1.19 billion to set it to 1980's USD per Wilshire's notes.
        self._data['WIL5000'] = self._data['WIL5000'] * 1190000000
        # Calculate the indicator as market cap / GDP
        self._data[self._label] = self._data['WIL5000'] / self._data["GDP"]
        print(self._data.columns)

    def __setIndex(self):
        self._wilshire_index = Wilshire5kIndex('yahoo', "^W5000", self._time_span)
        #self._wilshire_index.Data.dropna(inplace=True)
        self._wilshire_index.Data.fillna(method='ffill', inplace=True)
        self._wilshire_index.Data.fillna(method='bfill', inplace=True)
        self._wilshire_index.Data.columns = ['WIL5000']
        print('WIL', self._wilshire_index.Data.columns)

    def __setIndexQuarterly(self) -> DataFrame:
        df: DataFrame = self._wilshire_index.Data.copy()
        #df.resample('3M').last()
        print('3M', df.columns)
        return df

    def __setGdp(self):
        self._us_gdp = pdr.DataReader('GDP', 'fred', self._time_span.StartDate, self._time_span.EndDate)
        #self._us_gdp.dropna(inplace=True)
        self._us_gdp.fillna(method='ffill', inplace=True)
        self._us_gdp.fillna(method='bfill', inplace=True)
        print('GDP', self._us_gdp.columns)
