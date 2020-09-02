import math
import matplotlib.pyplot as plt
from Common.Plotters.TechIndicators.AbstractTechIndicatorPlotter import AbstractTechIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class RsiIndicatorPlotter(AbstractTechIndicatorPlotter):

    def __init__(self, y_stock_option: YahooStockOption, rsi_indicator: AbstractTechIndicator):
        self.__ABSTRACT_INDICATOR = rsi_indicator
        self.__DATE_TIME_INDEX = y_stock_option.HistoricalData.index
        self.__FIG_SIZE = (3 * math.log(y_stock_option.TimeSpan.MonthCount), 4.5)
        self.__INDICATOR_DATA_FRAME = y_stock_option.HistoricalData
        self.__LEGEND_PLACE = 'upper left'
        self.__PLOT_STYLE = 'fivethirtyeight'
        self.__SOURCE = y_stock_option.Source
        self.__TICKER = y_stock_option.Ticker
        self.__TICKER_LABEL = y_stock_option.Source + y_stock_option.Ticker + "_" + rsi_indicator._Label
        self.__TITLE = "{0}{1}_{2} {3} History {4} months".format(y_stock_option.Source,
                                                                  y_stock_option.Ticker,
                                                                  rsi_indicator._Label,
                                                                  rsi_indicator._Col,
                                                                  str(y_stock_option.TimeSpan.MonthCount))
        self.__XLABEL = y_stock_option.TimeSpan.StartDateStr + ' - ' + y_stock_option.TimeSpan.EndDateStr
        self.__XTICKS_ANGLE = 45
        self.__YLABEL = rsi_indicator._Col + ' in $USD'

    def Plot(self):
        plt.figure(figsize=self.__FIG_SIZE)
        plt.plot(self.__DATE_TIME_INDEX, self.__ABSTRACT_INDICATOR._rsi, label=self.__TICKER_LABEL, alpha=0.7)
        plt.axhline(10, linestyle='--', label='10%', alpha=0.50, color='gray')
        plt.axhline(20, linestyle='--', label='20%', alpha=0.50, color='orange')
        plt.axhline(30, linestyle='--', label='30%', alpha=0.50, color='green')
        plt.axhline(40, linestyle='--', label='40%', alpha=0.50, color='red')
        plt.axhline(60, linestyle='--', label='60%', alpha=0.50, color='red')
        plt.axhline(70, linestyle='--', label='70%', alpha=0.50, color='green')
        plt.axhline(80, linestyle='--', label='80%', alpha=0.50, color='orange')
        plt.axhline(90, linestyle='--', label='90%', alpha=0.50, color='gray')
        plt.title(self.__TITLE)
        plt.xlabel(self.__XLABEL)
        plt.xticks(rotation=self.__XTICKS_ANGLE)
        plt.ylabel(self.__YLABEL)
        plt.legend(loc=self.__LEGEND_PLACE)
        return plt
