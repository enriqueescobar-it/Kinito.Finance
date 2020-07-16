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
