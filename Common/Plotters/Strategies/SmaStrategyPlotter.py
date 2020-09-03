import math
import matplotlib.pyplot as plt
from Common.Plotters.Strategies.AbstractStrategyPlotter import AbstractStrategyPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy


class SmaStrategyPlotter(AbstractStrategyPlotter):

    def __init__(self, y_stock_option: YahooStockOption, sma_strategy: SmaStrategy):
        self._FIG_SIZE = (3 * math.log(y_stock_option.TimeSpan.MonthCount), 4.5)
        self.__SOURCE = y_stock_option.Source
        self.__TICKER = y_stock_option.Ticker
        self.__TICKER_LABEL = y_stock_option.Source + y_stock_option.Ticker + "_" + sma_strategy._Col
        self.__TITLE = "{0}{1}_{2} {3} History {4} BUY & SELL Signals".format(y_stock_option.Source,
                                                                              y_stock_option.Ticker,
                                                                              sma_strategy._Label,
                                                                              sma_strategy._Col,
                                                                              sma_strategy._Label)
        self.__XLABEL = y_stock_option.TimeSpan.StartDateStr + ' - ' + y_stock_option.TimeSpan.EndDateStr
        self.__YLABEL = sma_strategy._Col + ' in $USD'
        self.__DATE_TIME_INDEX = y_stock_option.HistoricalData.index
        self.__STRATEGY_DATA_FRAME = sma_strategy._DataFrame
        self.__STRATEGY_LABEL = sma_strategy._Label
        self.__STRATEGY_LABEL_BUY = sma_strategy._BuyLabel
        self.__STRATEGY_DATA_BUY = sma_strategy._DataFrame[sma_strategy._BuyLabel]
        self.__STRATEGY_LABEL_SELL = sma_strategy._SellLabel
        self.__STRATEGY_DATA_SELL = sma_strategy._DataFrame[sma_strategy._SellLabel]

    def Plot(self):
        #plt.style.use(self.__PLOT_STYLE)
        plt.figure(figsize=self._FIG_SIZE)
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__TICKER], label=self.__TICKER_LABEL, alpha=0.7)
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__STRATEGY_LABEL + '005'], label=self.__STRATEGY_LABEL + '005', alpha=0.50, color='lightblue')
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__STRATEGY_LABEL + '009'], label=self.__STRATEGY_LABEL + '009', alpha=0.50, color='lightgray')
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__STRATEGY_LABEL + '010'], label=self.__STRATEGY_LABEL + '010', alpha=0.50, color='green')
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__STRATEGY_LABEL + '020'], label=self.__STRATEGY_LABEL + '020', alpha=0.50, color='orange')
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__STRATEGY_LABEL + '030'], label=self.__STRATEGY_LABEL + '030', alpha=0.50, color='violet')
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__STRATEGY_LABEL + '050'], label=self.__STRATEGY_LABEL + '050', alpha=0.50, color='pink')
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__STRATEGY_LABEL + '100'], label=self.__STRATEGY_LABEL + '100', alpha=0.50, color='red')
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__STRATEGY_LABEL + '200'], label=self.__STRATEGY_LABEL + '200', alpha=0.50, color='yellow')
        plt.scatter(self.__DATE_TIME_INDEX, self.__STRATEGY_DATA_BUY, label=self.__STRATEGY_LABEL_BUY, marker='^', color='green')
        plt.scatter(self.__DATE_TIME_INDEX, self.__STRATEGY_DATA_SELL, label=self.__STRATEGY_LABEL_SELL, marker='v', color='red')
        plt.title(self.__TITLE)
        plt.xlabel(self.__XLABEL)
        plt.xticks(rotation=self._XTICKS_ANGLE)
        plt.ylabel(self.__YLABEL)
        plt.legend(loc=self._LEGEND_PLACE)
        return plt
