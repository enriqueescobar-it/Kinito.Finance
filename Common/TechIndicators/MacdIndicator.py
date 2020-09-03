import pandas as pd
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class MacdIndicator(AbstractTechIndicator):
    _macd: pd.core.series.Series
    _signal_line: pd.core.series.Series
    _SignalLineLabel: str = 'SignalLine'
    __ShortExponentialMovingAverage: pd.core.series.Series
    __LongExponentialMovingAverage: pd.core.series.Series

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._label += 'MACD'
        self.__ShortExponentialMovingAverage = self.__getEMA(y_stock_option, 12)
        self.__LongExponentialMovingAverage = self.__getEMA(y_stock_option, 26)
        self._macd = self.__ShortExponentialMovingAverage - self.__LongExponentialMovingAverage
        self._signal_line = self._macd.ewm(span=9, adjust=False).mean()

    def __getEMA(self, y_stock_option: YahooStockOption, a_int: int = 12):
        return y_stock_option.HistoricalData[self._col].ewm(span=a_int, adjust=False).mean()
