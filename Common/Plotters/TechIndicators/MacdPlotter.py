import matplotlib.pyplot as plt
from pandas import DatetimeIndex
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Plotters.TechIndicators.AbstractTechIndicatorsPlotter import AbstractTechIndicatorsPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.MacdIndicator import MacdIndicator


class MacdPlotter(AbstractTechIndicatorsPlotter):
    __dateTimeIndex: DatetimeIndex
    _Indicator: MacdIndicator
    __Label: str
    __src: str
    __ticker: str
    __timeSpan: TimeSpan

    def __init__(self, y_stock_option: YahooStockOption, macd_indicator: MacdIndicator):
        self.__dateTimeIndex = y_stock_option.HistoricalData.index
        self._Indicator = macd_indicator
        self.__src = y_stock_option.Source
        self.__legendPlace = 'upper left'
        self.__ticker = y_stock_option.Ticker
        self.__timeSpan = y_stock_option.TimeSpan
        self.__Label = y_stock_option.Source + y_stock_option.Ticker + "_" + self._Indicator._Label

    def Plot(self):
        plt.figure(figsize=(self.__timeSpan.MonthCount / 2, 4.5))
        plt.plot(self.__dateTimeIndex, self._Indicator._Macd, label=self._Indicator._Label, color='red', alpha=0.7)
        plt.plot(self.__dateTimeIndex, self._Indicator._SignalLine, label=self._Indicator._SignalLineLabel, color='blue', alpha=0.7)
        plt.title(self.__Label + ' ' + self._Indicator._Col + ' History ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.xticks(rotation=45)
        plt.ylabel(self._Indicator._Col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        return plt
