from pandas import DatetimeIndex
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Plotters.TechIndicators.AbstractTechIndicatorsPlotter import AbstractTechIndicatorsPlotter
from Common.TechIndicators.RsiManager import RsiManager
from pyarrow.lib import null
import pandas as pd
import matplotlib.pyplot as plt


class RsiPlotter(AbstractTechIndicatorsPlotter):
    __dateTimeIndex: DatetimeIndex
    __rsiManager: RsiManager
    __src: str
    __ticker: str
    __timeSpan: TimeSpan

    def __init__(self, date_time_index: pd.DatetimeIndex, rsi_manager: RsiManager, src: str = 'yahoo', tick: str = 'CNI', ts: TimeSpan = null):
        self.__dateTimeIndex = date_time_index
        self.__rsiManager = rsi_manager
        self.__src = src
        self.__legendPlace = 'upper left'
        self.__ticker = tick
        self.__timeSpan = ts
        self.__rsiLabel = src + tick + "_" + rsi_manager._RsiLabel

    def __draw(self):
        plt.figure(figsize=(self.__timeSpan.MonthCount / 2, 4.5))
        plt.plot(self.__dateTimeIndex, self.__rsiManager.__rsi, label=self.__rsiLabel, alpha=0.7)
        plt.axhline(10, linestyle='--', label='10%', alpha=0.50, color='gray')
        plt.axhline(20, linestyle='--', label='20%', alpha=0.50, color='orange')
        plt.axhline(30, linestyle='--', label='30%', alpha=0.50, color='green')
        plt.axhline(40, linestyle='--', label='40%', alpha=0.50, color='red')
        plt.axhline(60, linestyle='--', label='60%', alpha=0.50, color='red')
        plt.axhline(70, linestyle='--', label='70%', alpha=0.50, color='green')
        plt.axhline(80, linestyle='--', label='80%', alpha=0.50, color='orange')
        plt.axhline(90, linestyle='--', label='90%', alpha=0.50, color='gray')
        plt.title(
            self.__rsiLabel + ' ' + self.__rsiManager.__col + ' History ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.xticks(rotation=45)
        plt.ylabel(self.__rsiManager.__col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        plt.show()
