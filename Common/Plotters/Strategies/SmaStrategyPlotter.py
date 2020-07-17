import matplotlib.pyplot as plt
import pandas as pd
from Common.Plotters.Strategies.AbstractStrategyPlotter import AbstractStrategyPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy


class SmaStrategyPlotter(AbstractStrategyPlotter):
    __dateTimeIndex: pd.core.indexes.datetimes.DatetimeIndex
    __smaStrategy: SmaStrategy

    def __init__(self, y_stock_option: YahooStockOption, sma_strategy: SmaStrategy):
        self.__FIG_SIZE = (y_stock_option.TimeSpan.MonthCount / 2, 4.5)
        self.__LEGEND_PLACE = 'upper left'
        self.__PLOT_STYLE = 'fivethirtyeight'
        self.__SOURCE = y_stock_option.Source
        self.__TICKER = y_stock_option.Ticker
        self.__TITLE = "{0}{1}_{2} {3} History {4} BUY & SELL Signals".format(y_stock_option.Source,
                                                                              y_stock_option.Ticker,
                                                                              sma_strategy._Label,
                                                                              sma_strategy._Col,
                                                                              sma_strategy._Label)
        self.__XLABEL = y_stock_option.TimeSpan.StartDateStr + ' - ' + y_stock_option.TimeSpan.EndDateStr
        self.__XTICKS_ANGLE = 45
        self.__YLABEL = sma_strategy._Col + ' in $USD'
        self.__dateTimeIndex = y_stock_option.HistoricalData.index
        self.__smaStrategy = sma_strategy
        self.__timeSpan = y_stock_option.TimeSpan
        self.__Label = y_stock_option.Source + y_stock_option.Ticker + "_" + sma_strategy._Label

    def Plot(self):
        #plt.style.use(self.__PLOT_STYLE)
        plt.figure(figsize=(self.__FIG_SIZE))
        plt.plot(self.__smaStrategy._DataFrame[self.__TICKER], label=self.__Label, alpha=0.7)
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '005'], label=self.__smaStrategy._Label + '005', alpha=0.50, color='lightblue')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '009'], label=self.__smaStrategy._Label + '009', alpha=0.50, color='lightgray')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '010'], label=self.__smaStrategy._Label + '010', alpha=0.50, color='green')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '020'], label=self.__smaStrategy._Label + '020', alpha=0.50, color='orange')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '030'], label=self.__smaStrategy._Label + '030', alpha=0.50, color='violet')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '050'], label=self.__smaStrategy._Label + '050', alpha=0.50, color='pink')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '100'], label=self.__smaStrategy._Label + '100', alpha=0.50, color='red')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '200'], label=self.__smaStrategy._Label + '200', alpha=0.50, color='yellow')
        plt.scatter(self.__dateTimeIndex, self.__smaStrategy._DataFrame[self.__smaStrategy._BuyLabel], label=self.__smaStrategy._BuyLabel, marker='^', color='green')
        plt.scatter(self.__dateTimeIndex, self.__smaStrategy._DataFrame[self.__smaStrategy._SellLabel], label=self.__smaStrategy._SellLabel, marker='v', color='red')
        plt.title(self.__TITLE)
        plt.xlabel(self.__XLABEL)
        plt.xticks(rotation=self.__XTICKS_ANGLE)
        plt.ylabel(self.__YLABEL)
        plt.legend(loc=self.__LEGEND_PLACE)
        return plt
