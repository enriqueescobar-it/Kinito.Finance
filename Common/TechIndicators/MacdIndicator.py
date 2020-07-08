import pandas as pd
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class MacdIndicator(AbstractTechIndicator):
    _Label: str
    _Col: str
    __src: str

    __ShortExponentialMovingAverage: pd.core.series.Series
    __LongExponentialMovingAverage: pd.core.series.Series
    _Macd: pd.core.series.Series
    _SignalLine: pd.core.series.Series
    _SignalLineLabel: str

    def __init__(self, y_stock_option: YahooStockOption):
        self.__src = y_stock_option.Source
        self._Label = 'MACD'
        self._Col = 'Adj Close' if self.__src == 'yahoo' else 'Close'
        self.__ShortExponentialMovingAverage = self.__getEMA(y_stock_option, 12)
        self.__LongExponentialMovingAverage = self.__getEMA(y_stock_option, 26)
        self._Macd = self.__ShortExponentialMovingAverage - self.__LongExponentialMovingAverage
        self._SignalLine = self._Macd.ewm(span=9, adjust=False).mean()
        self._SignalLineLabel = 'SignalLine'

    def __getEMA(self, y_stock_option: YahooStockOption, a_int: int = 12):
        return y_stock_option.HistoricalData[self._Col].ewm(span=a_int, adjust=False).mean()
