import pandas as pd
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class MovingAverageIndicator(AbstractTechIndicator):
    _MA005: pd.core.series.Series
    _MA009: pd.core.series.Series
    _MA010: pd.core.series.Series
    _MA020: pd.core.series.Series
    _MA050: pd.core.series.Series
    _MA100: pd.core.series.Series
    _MA200: pd.core.series.Series

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._Label = 'MA'
        self._MA005 = self.__getMA(y_stock_option, 5)
        self._MA009 = self.__getMA(y_stock_option, 9)
        self._MA010 = self.__getMA(y_stock_option, 10)
        self._MA020 = self.__getMA(y_stock_option, 20)
        self._MA050 = self.__getMA(y_stock_option, 50)
        self._MA100 = self.__getMA(y_stock_option, 100)
        self._MA200 = self.__getMA(y_stock_option, 200)

    def __getMA(self, y_stock_option: YahooStockOption, a_int: int = 12):
        # return last column as .iloc[:,-1] spaning rollng mean
        return y_stock_option.HistoricalData[self._Col].rolling(window=a_int, min_periods=0).mean()