import matplotlib.pyplot as plt
from Common.Plotters.TechIndicators.AbstractTechIndicatorPlotter import AbstractTechIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class MovingAveragePlotter(AbstractTechIndicatorPlotter):

    def __init__(self, y_stock_option: YahooStockOption, ma_indicator: AbstractTechIndicator):
        self.__dateTimeIndex = y_stock_option.HistoricalData.index
        self._Indicator = ma_indicator
        self.__src = y_stock_option.Source
        self.__legendPlace = 'upper left'
        self.__ticker = y_stock_option.Ticker
        self.__timeSpan = y_stock_option.TimeSpan
        self.__Label = y_stock_option.Source + y_stock_option.Ticker + "_" + self._Indicator._Label
        self.__data = y_stock_option.HistoricalData[ma_indicator._Col]

    def Plot(self):
        plt.figure(figsize=(self.__timeSpan.MonthCount / 2, 4.5))
        plt.plot(self.__dateTimeIndex, self.__data, label=self.__Label, alpha=0.7)
        plt.plot(self.__dateTimeIndex, self._Indicator._MA005, label=self.__Label + '5', alpha=0.50, color='gray')
        plt.plot(self.__dateTimeIndex, self._Indicator._MA009, label=self.__Label + '9', alpha=0.50, color='orange')
        plt.plot(self.__dateTimeIndex, self._Indicator._MA010, label=self.__Label + '10', alpha=0.50, color='green')
        plt.plot(self.__dateTimeIndex, self._Indicator._MA020, label=self.__Label + '20', alpha=0.50, color='red')
        plt.plot(self.__dateTimeIndex, self._Indicator._MA100, label=self.__Label + '100', alpha=0.50)
        plt.plot(self.__dateTimeIndex, self._Indicator._MA200, label=self.__Label + '200', alpha=0.50)
        plt.title(
            self.__Label + ' ' + self._Indicator._Col + ' History ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.xticks(rotation=45)
        plt.ylabel(self._Indicator._Col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        return plt
