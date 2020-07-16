import matplotlib.pyplot as plt
from Common.Plotters.Strategies.AbstractStrategyPlotter import AbstractStrategyPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy


class SmaStrategyPlotter(AbstractStrategyPlotter):
    __smaStrategy: SmaStrategy

    def __init__(self, y_stock_option: YahooStockOption, sma_strategy: SmaStrategy):
        self.__dateTimeIndex = y_stock_option.HistoricalData.index
        self.__smaStrategy = sma_strategy
        self.__src = y_stock_option.Source
        self.__legendPlace = 'upper left'
        self.__ticker = y_stock_option.Ticker
        self.__timeSpan = y_stock_option.TimeSpan
        self.__Label = y_stock_option.Source + y_stock_option.Ticker + "_" + sma_strategy._Label

    def Plot(self):
        plt.figure(figsize=(self.__timeSpan.MonthCount / 2, 4.5))
        plt.title(self.__Label + ' ' + self.__smaStrategy._Col + ' History ' + self.__smaStrategy._Label + ' BUY & SELL Signals')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.xticks(rotation=45)
        plt.ylabel(self.__smaStrategy._Col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        return plt
