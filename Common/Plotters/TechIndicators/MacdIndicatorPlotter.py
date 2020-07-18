import matplotlib.pyplot as plt
from Common.Plotters.TechIndicators.AbstractTechIndicatorPlotter import AbstractTechIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class MacdIndicatorPlotter(AbstractTechIndicatorPlotter):

    def __init__(self, y_stock_option: YahooStockOption, macd_indicator: AbstractTechIndicator):
        self.__FIG_SIZE = (y_stock_option.TimeSpan.MonthCount / 2, 4.5)
        self.__LEGEND_PLACE = 'upper left'
        self.__PLOT_STYLE = 'fivethirtyeight'
        self.__SOURCE = y_stock_option.Source
        self.__TICKER = y_stock_option.Ticker
        self.__TITLE = "{0}{1}_{2} {3} History {4} months".format(y_stock_option.Source,
                                                                  y_stock_option.Ticker,
                                                                  macd_indicator._Label,
                                                                  macd_indicator._Col,
                                                                  str(y_stock_option.TimeSpan.MonthCount))
        self.__dateTimeIndex = y_stock_option.HistoricalData.index
        self._Indicator = macd_indicator
        self.__timeSpan = y_stock_option.TimeSpan
        self.__Label = y_stock_option.Source + y_stock_option.Ticker + "_" + macd_indicator._Label

    def Plot(self):
        plt.figure(figsize=self.__FIG_SIZE)
        plt.plot(self.__dateTimeIndex, self._Indicator._Macd, label=self._Indicator._Label, alpha=0.9)#, color='red'
        plt.plot(self.__dateTimeIndex, self._Indicator._SignalLine, label=self._Indicator._SignalLineLabel, color='lightblue', alpha=0.9)
        plt.title(self.__TITLE)
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.xticks(rotation=45)
        plt.ylabel(self._Indicator._Col + ' in $USD')
        plt.legend(loc=self.__LEGEND_PLACE)
        return plt
