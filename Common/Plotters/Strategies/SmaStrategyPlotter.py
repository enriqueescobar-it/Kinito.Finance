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
        plt.plot(self.__smaStrategy._DataFrame[self.__ticker], label=self.__Label, alpha=0.7)
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '005'], label=self.__smaStrategy._Label + '005', alpha=0.50, color='lightblue')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '009'], label=self.__smaStrategy._Label + '009', alpha=0.50, color='lightgray')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '010'], label=self.__smaStrategy._Label + '010', alpha=0.50, color='green')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '020'], label=self.__smaStrategy._Label + '020', alpha=0.50, color='orange')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '030'], label=self.__smaStrategy._Label + '030', alpha=0.50, color='yellow')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '050'], label=self.__smaStrategy._Label + '050', alpha=0.50, color='pink')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '100'], label=self.__smaStrategy._Label + '100', alpha=0.50, color='red')
        plt.plot(self.__smaStrategy._DataFrame[self.__smaStrategy._Label + '200'], label=self.__smaStrategy._Label + '200', alpha=0.50, color='violet')
        plt.scatter(self.__dateTimeIndex, self.__smaStrategy._DataFrame[self.__smaStrategy._BuyLabel], label=self.__smaStrategy._BuyLabel, marker='^', color='green')
        plt.scatter(self.__dateTimeIndex, self.__smaStrategy._DataFrame[self.__smaStrategy._SellLabel], label=self.__smaStrategy._SellLabel, marker='v', color='red')
        plt.title(self.__Label + ' ' + self.__smaStrategy._Col + ' History ' + self.__smaStrategy._Label + ' BUY & SELL Signals')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.xticks(rotation=45)
        plt.ylabel(self.__smaStrategy._Col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        return plt
