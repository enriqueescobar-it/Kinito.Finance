import matplotlib.pyplot as plt
from Common.Plotters.TechIndicators.AbstractTechIndicatorPlotter import AbstractTechIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class SmaIndicatorPlotter(AbstractTechIndicatorPlotter):

    def __init__(self, y_stock_option: YahooStockOption, ma_indicator: AbstractTechIndicator):
        self.__FIG_SIZE = (y_stock_option.TimeSpan.MonthCount / 2, 4.5)
        self.__LEGEND_PLACE = 'upper left'
        self.__PLOT_STYLE = 'fivethirtyeight'
        self.__SOURCE = y_stock_option.Source
        self.__TICKER = y_stock_option.Ticker
        self.__dateTimeIndex = y_stock_option.HistoricalData.index
        self._Indicator = ma_indicator
        self.__timeSpan = y_stock_option.TimeSpan
        self.__Label = y_stock_option.Source + y_stock_option.Ticker + "_" + self._Indicator._Label
        self.__data = y_stock_option.HistoricalData[ma_indicator._Col]

    def Plot(self):
        plt.figure(figsize=self.__FIG_SIZE)
        plt.plot(self.__dateTimeIndex, self.__data, label=self.__Label, alpha=0.7)
        plt.plot(self.__dateTimeIndex, self._Indicator._SMA005, label=self.__Label + '005', alpha=0.50, color='lightblue')
        plt.plot(self.__dateTimeIndex, self._Indicator._SMA009, label=self.__Label + '009', alpha=0.50, color='lightgray')
        plt.plot(self.__dateTimeIndex, self._Indicator._SMA010, label=self.__Label + '010', alpha=0.50, color='green')
        plt.plot(self.__dateTimeIndex, self._Indicator._SMA020, label=self.__Label + '020', alpha=0.50, color='orange')
        plt.plot(self.__dateTimeIndex, self._Indicator._SMA030, label=self.__Label + '030', alpha=0.50, color='violet')
        plt.plot(self.__dateTimeIndex, self._Indicator._SMA050, label=self.__Label + '050', alpha=0.50, color='pink')
        plt.plot(self.__dateTimeIndex, self._Indicator._SMA100, label=self.__Label + '100', alpha=0.50, color='red')
        plt.plot(self.__dateTimeIndex, self._Indicator._SMA200, label=self.__Label + '200', alpha=0.50, color='yellow')
        plt.title(
            self.__Label + ' ' + self._Indicator._Col + ' History ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.xticks(rotation=45)
        plt.ylabel(self._Indicator._Col + ' in $USD')
        plt.legend(loc=self.__LEGEND_PLACE)
        return plt
