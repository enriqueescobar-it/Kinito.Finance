import matplotlib.pyplot as plt
from Common.Plotters.TechIndicators.AbstractTechIndicatorPlotter import AbstractTechIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class EmaIndicatorPlotter(AbstractTechIndicatorPlotter):

    def __init__(self, y_stock_option: YahooStockOption, ema_indicator: AbstractTechIndicator):
        self.__ABSTRACT_INDICATOR = ema_indicator
        self.__DATE_TIME_INDEX = y_stock_option.HistoricalData.index
        self.__FIG_SIZE = (y_stock_option.TimeSpan.MonthCount / 2, 4.5)
        self.__INDICATOR_DATA_FRAME = y_stock_option.HistoricalData
        self.__LEGEND_PLACE = 'upper left'
        self.__PLOT_STYLE = 'fivethirtyeight'
        self.__SOURCE = y_stock_option.Source
        self.__TICKER = y_stock_option.Ticker
        self.__TICKER_LABEL = ema_indicator._Label # y_stock_option.Source + y_stock_option.Ticker + "_" +
        self.__TITLE = "{0}{1}_{2} {3} History {4} months".format(y_stock_option.Source,
                                                                  y_stock_option.Ticker,
                                                                  ema_indicator._Label,
                                                                  ema_indicator._Col,
                                                                  str(y_stock_option.TimeSpan.MonthCount))
        self.__XLABEL = y_stock_option.TimeSpan.StartDateStr + ' - ' + y_stock_option.TimeSpan.EndDateStr
        self.__XTICKS_ANGLE = 45
        self.__YLABEL = ema_indicator._Col + ' in $USD'

    def Plot(self):
        plt.figure(figsize=self.__FIG_SIZE)
        plt.plot(self.__DATE_TIME_INDEX, self.__INDICATOR_DATA_FRAME[self.__ABSTRACT_INDICATOR._Col], label=self.__TICKER_LABEL, alpha=0.7)
        plt.plot(self.__DATE_TIME_INDEX, self.__ABSTRACT_INDICATOR._EMA05, label=self.__TICKER_LABEL + '05', alpha=0.50, color='cyan')
        plt.plot(self.__DATE_TIME_INDEX, self.__ABSTRACT_INDICATOR._EMA21, label=self.__TICKER_LABEL + '21', alpha=0.50, color='orange')
        plt.plot(self.__DATE_TIME_INDEX, self.__ABSTRACT_INDICATOR._EMA63, label=self.__TICKER_LABEL + '63', alpha=0.50, color='violet')
        plt.title(self.__TITLE)
        plt.xlabel(self.__XLABEL)
        plt.xticks(rotation=self.__XTICKS_ANGLE)
        plt.ylabel(self.__YLABEL)
        plt.legend(loc=self.__LEGEND_PLACE)
        return plt
