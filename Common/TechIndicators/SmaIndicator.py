import pandas as pd
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class SmaIndicator(AbstractTechIndicator):
    _SMA005: pd.core.series.Series
    _SMA009: pd.core.series.Series
    _SMA010: pd.core.series.Series
    _SMA020: pd.core.series.Series
    _SMA030: pd.core.series.Series
    _SMA050: pd.core.series.Series
    _SMA100: pd.core.series.Series
    _SMA200: pd.core.series.Series

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._label += 'SMA'
        self._SMA005 = self.__getSma(y_stock_option, 5)
        self._SMA009 = self.__getSma(y_stock_option, 9)
        self._SMA010 = self.__getSma(y_stock_option, 10)
        self._SMA020 = self.__getSma(y_stock_option, 20)
        self._SMA030 = self.__getSma(y_stock_option, 30)
        self._SMA050 = self.__getSma(y_stock_option, 50)
        self._SMA100 = self.__getSma(y_stock_option, 100)
        self._SMA200 = self.__getSma(y_stock_option, 200)

    def __getSma(self, y_stock_option: YahooStockOption, a_int: int = 12):
        # return last column as .iloc[:,-1] spaning rollng mean
        return y_stock_option.HistoricalData[self._col].rolling(window=a_int, min_periods=0).mean()
