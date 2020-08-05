import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy.core._multiarray_umath import ndarray

from Common.Plotters.AbstractPlotter import AbstractPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class HistoricalPlotter(AbstractPlotter):
    __mean: ndarray
    __median: ndarray
    __yeAverage200: float
    __yeAverage50: float
    __yeHigh52: float
    __yeLow52: float

    def __init__(self, y_stockOption: YahooStockOption):
        self.__yeHigh52 = np.round(y_stockOption.YeHigh52, 2)
        self.__yeLow52 = np.round(y_stockOption.YeLow52, 2)
        self.__yeAverage50 = np.round(y_stockOption.YeAverage50, 2)
        self.__yeAverage200 = np.round(y_stockOption.YeAverage200, 2)
        if y_stockOption.Source == 'yahoo':
            self.__Col = "Adj Close"
        self.__dataFrame = y_stockOption.HistoricalData
        self.__mean = np.mean(y_stockOption.HistoricalData[self.__Col])
        self.__mean = np.round(self.__mean, 2)
        self.__median = np.median(y_stockOption.HistoricalData[self.__Col])
        self.__median = np.round(self.__median, 2)
        self.__src = y_stockOption.Source
        self.__legendPlace = 'upper left'
        self.__ticker = y_stockOption.Ticker
        self.__timeSpan = y_stockOption.TimeSpan
        print('yyyy:', y_stockOption.TimeSpan.YearCount)
        print('MM:', y_stockOption.TimeSpan.MonthCount)
        print('ww:', y_stockOption.TimeSpan.WeekCount)
        print('dd:', y_stockOption.TimeSpan.DayCount)

    def Plot(self):
        '''
        fig, ax = plt.subplots()
        -ax.plot(x, y)
        -ax.hlines(y=0.2, xmin=4, xmax=20, linewidth=2, color='r')
        -plt.hlines(y=40, xmin=0, xmax=len(self._dataFrame[self._draw_col]), colors='r', linestyles='--', lw=2)
        fig.set_size_inches(3, 1.5)
        plt.savefig(file.jpeg, edgecolor='black', dpi=400, facecolor='black', transparent=True)
        '''
        # visualize data
        plt.style.use('fivethirtyeight')
        # self._monthCount
        plt.figure(figsize=(self.__timeSpan.MonthCount / 2, 4.5))
        # Plot the grid lines
        plt.plot(self.__dataFrame[self.__Col], label=self.__Col)
        plt.axhline(self.__median, linestyle='--', label=self.__Col + '_Median=' + str(self.__median), color='red')
        plt.axhline(self.__mean, linestyle='--', label=self.__Col + '_Mean=' + str(self.__mean), color='blue')
        plt.axhline(self.__yeHigh52, linestyle='--', label='yeHigh52=' + str(self.__yeHigh52), alpha=0.50, color='red')
        plt.axhline(self.__yeLow52, linestyle='--', label='yeLow52=' + str(self.__yeLow52), alpha=0.50, color='green')
        plt.axhline(self.__yeAverage200, linestyle='-.', label='yeAverage200=' + str(self.__yeAverage200), alpha=0.50,
                    color='yellow')
        plt.axhline(self.__yeAverage50, linestyle='-.', label='yeAverage50=' + str(self.__yeAverage50), alpha=0.50,
                    color='orange')
        plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
        plt.title(self.__ticker + ' ' + self.__Col + ' History ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.ylabel(self.__Col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        return plt

    def Distro(self):
        plt.figure(figsize=(self.__timeSpan.MonthCount / 2, 4.5))
        plt.tight_layout()
        sns.distplot(self.__dataFrame[self.__Col], vertical=True, rug=True)
        plt.axhline(self.__median, color='red', linestyle='--', label=self.__Col + '_Mean=' + str(self.__median))
        plt.axhline(self.__mean, color='blue', linestyle='--', label=self.__Col + '_Median=' + str(self.__mean))
        #plt.axhline(self.__dataFrame[self.__Col].mode(numeric_only=True), color='g', linestyle='--')
        plt.title(self.__ticker + ' ' + self.__Col + ' History ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.ylabel(self.__Col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        return plt
