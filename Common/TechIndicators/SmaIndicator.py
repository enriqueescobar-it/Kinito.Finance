import pandas as pd

from Common.Plotters.TechIndicators.AbstractTechIndicatorPlotter import AbstractTechIndicatorPlotter
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class SmaIndicator(AbstractTechIndicator, AbstractTechIndicatorPlotter):

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._name = 'SMA'
        self._label += self._name
        self._setData(y_stock_option)

    def __getSma(self, y_stock_option: YahooStockOption, a_int: int = 12):
        # return last column as .iloc[:,-1] spaning rollng mean
        return y_stock_option.HistoricalData[self._col].rolling(window=a_int, min_periods=0).mean()

    def _setData(self, y_stock_option: YahooStockOption):
        self._data[self._name + '005'] = self.__getSma(y_stock_option, 5)
        self._data[self._name + '009'] = self.__getSma(y_stock_option, 9)
        self._data[self._name + '010'] = self.__getSma(y_stock_option, 10)
        self._data[self._name + '020'] = self.__getSma(y_stock_option, 20)
        self._data[self._name + '030'] = self.__getSma(y_stock_option, 30)
        self._data[self._name + '050'] = self.__getSma(y_stock_option, 50)
        self._data[self._name + '100'] = self.__getSma(y_stock_option, 100)
        self._data[self._name + '200'] = self.__getSma(y_stock_option, 200)
        print(self._data.tail())
