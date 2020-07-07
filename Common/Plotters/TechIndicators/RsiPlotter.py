import pandas as pd
import matplotlib.pyplot as plt
from pandas import DatetimeIndex
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Plotters.TechIndicators.AbstractTechIndicatorsPlotter import AbstractTechIndicatorsPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.RsiIndicator import RsiIndicator


class RsiPlotter(AbstractTechIndicatorsPlotter):
    __dateTimeIndex: DatetimeIndex
    __rsiIndicator: RsiIndicator
    __src: str
    __ticker: str
    __timeSpan: TimeSpan

    def __init__(self, y_stock_option: YahooStockOption, rsi_indicator: RsiIndicator):
        self.__dateTimeIndex = y_stock_option.HistoricalData.index
        self.__rsiIndicator = rsi_indicator
        self.__src = y_stock_option.Source
        self.__legendPlace = 'upper left'
        self.__ticker = y_stock_option.Ticker
        self.__timeSpan = y_stock_option.TimeSpan
        self.__rsiLabel = y_stock_option.Source + y_stock_option.Ticker + "_" + rsi_indicator._Label

    def Plot(self):
        plt.figure(figsize=(self.__timeSpan.MonthCount / 2, 4.5))
        plt.plot(self.__dateTimeIndex, self.__rsiIndicator._rsi, label=self.__rsiLabel, alpha=0.7)
        plt.axhline(10, linestyle='--', label='10%', alpha=0.50, color='gray')
        plt.axhline(20, linestyle='--', label='20%', alpha=0.50, color='orange')
        plt.axhline(30, linestyle='--', label='30%', alpha=0.50, color='green')
        plt.axhline(40, linestyle='--', label='40%', alpha=0.50, color='red')
        plt.axhline(60, linestyle='--', label='60%', alpha=0.50, color='red')
        plt.axhline(70, linestyle='--', label='70%', alpha=0.50, color='green')
        plt.axhline(80, linestyle='--', label='80%', alpha=0.50, color='orange')
        plt.axhline(90, linestyle='--', label='90%', alpha=0.50, color='gray')
        plt.title(
            self.__rsiLabel + ' ' + self.__rsiIndicator._Col + ' History ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.xticks(rotation=45)
        plt.ylabel(self.__rsiIndicator._Col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        return plt
