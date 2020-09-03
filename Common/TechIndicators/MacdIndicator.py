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
        self._name = 'MACD'
        self._label += self._name
        self.__ShortExponentialMovingAverage = self.__getEMA(y_stock_option, 12)
        self.__LongExponentialMovingAverage = self.__getEMA(y_stock_option, 26)
        self._macd = self.__ShortExponentialMovingAverage - self.__LongExponentialMovingAverage
        self._signal_line = self._macd.ewm(span=9, adjust=False).mean()
        self._data['EMA' + str(12)] = self.__ShortExponentialMovingAverage
        self._data['EMA' + str(26)] = self.__LongExponentialMovingAverage
        self._data[self._name] = self._macd
        self._data[self._SignalLineLabel] = self._signal_line
        print(self._data.tail())

    def __getEMA(self, y_stock_option: YahooStockOption, a_int: int = 12):
        return y_stock_option.HistoricalData[self._col].ewm(span=a_int, adjust=False).mean()
