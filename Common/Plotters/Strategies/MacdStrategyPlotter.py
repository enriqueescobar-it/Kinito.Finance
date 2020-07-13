import matplotlib.pyplot as plt
from Common.Plotters.Strategies.AbstractStrategyPlotter import AbstractStrategyPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy


class MacdStrategyPlotter(AbstractStrategyPlotter):
    __macdStrategy: MacdStrategy

    def __init__(self, y_stock_option: YahooStockOption, macd_strategy: MacdStrategy):
        self.__dateTimeIndex = y_stock_option.HistoricalData.index
        self.__macdStrategy = macd_strategy
        self.__src = y_stock_option.Source
        self.__legendPlace = 'upper left'
        self.__ticker = y_stock_option.Ticker
        self.__timeSpan = y_stock_option.TimeSpan
        self.__Label = y_stock_option.Source + y_stock_option.Ticker + "_" + macd_strategy._Label

    def Plot(self):
        plt.figure(figsize=(self.__timeSpan.MonthCount / 2, 4.5))
        plt.plot(self.__macdStrategy._DataFrame[self.__ticker], label = self.__Label, alpha = 0.6)
        plt.scatter(self.__dateTimeIndex, self.__macdStrategy._DataFrame[self.__macdStrategy._BuyLabel], label = self.__macdStrategy._BuyLabel, marker = '^', color = 'green')
        plt.scatter(self.__dateTimeIndex, self.__macdStrategy._DataFrame[self.__macdStrategy._SellLabel], label = self.__macdStrategy._SellLabel, marker = 'v', color = 'red')
        plt.title(self.__Label + ' ' + self.__macdStrategy._Col + ' History ' + self.__macdStrategy._Label + ' BUY & SELL Signals')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.xticks(rotation=45)
        plt.ylabel(self.__macdStrategy._Col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        return plt
