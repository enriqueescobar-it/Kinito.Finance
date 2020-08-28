import math

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scs
import seaborn as sns
import statsmodels.api as sm
from numpy.core._multiarray_umath import ndarray
from pandas import DataFrame
from pandas import Series
from arch import arch_model
from Common.Plotters.AbstractPlotter import AbstractPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class HistoricalPlotter(AbstractPlotter):
    __dataSimpleReturns: DataFrame
    __dataLogReturns: DataFrame
    __dataDaily: DataFrame
    __dataDailyCum: Series
    __dataMonthly: DataFrame
    __dataMonthlyCum: Series
    __mean: ndarray
    __median: ndarray
    __std: ndarray
    __price: float
    __yeAverage200: float
    __yeAverage50: float
    __yeHigh52: float
    __yeLow52: float

    def __init__(self, y_stockOption: YahooStockOption):
        self.__price = np.round(y_stockOption.FvPrice, 2)
        self.__yeHigh52 = np.round(y_stockOption.YeHigh52, 2)
        self.__yeLow52 = np.round(y_stockOption.YeLow52, 2)
        self.__yeAverage50 = np.round(y_stockOption.YeAverage50, 2)
        self.__yeAverage200 = np.round(y_stockOption.YeAverage200, 2)
        if y_stockOption.Source == 'yahoo':
            self.__Col = "Adj Close"
        self.__dataFrame = y_stockOption.HistoricalData
        self.__dataSimpleReturns = y_stockOption.HistoricalSimpleReturns
        self.__dataLogReturns = y_stockOption.HistoricalLogReturns
        self.__dataDaily = y_stockOption.HistoricalDaily
        self.__dataDailyCum = y_stockOption.HistoricalDailyCum
        self.__dataMonthly = y_stockOption.HistoricalMonthly
        self.__dataMonthlyCum = y_stockOption.HistoricalMonthlyCum
        self.__mean = np.mean(y_stockOption.HistoricalData[self.__Col])
        self.__mean = np.round(self.__mean, 2)
        self.__median = np.median(y_stockOption.HistoricalData[self.__Col])
        self.__median = np.round(self.__median, 2)
        self.__std = np.std(y_stockOption.HistoricalData[self.__Col])
        self.__std = np.round(self.__std, 2)
        self.__src = y_stockOption.Source
        self.__legendPlace = 'upper left'
        self.__ticker = y_stockOption.Ticker
        self.__timeSpan = y_stockOption.TimeSpan
        print('yyyy:', y_stockOption.TimeSpan.YearCount)
        print('MM:', y_stockOption.TimeSpan.MonthCount)
        print('ww:', y_stockOption.TimeSpan.WeekCount)
        print('dd:', y_stockOption.TimeSpan.DayCount)
        self.__stockOption = y_stockOption

    def __GetRankRange(self, a_df: DataFrame):
        return np.linspace(min(a_df[self.__Col]), max(a_df[self.__Col]), num=1000)

    def __GetProbabilityDensityFunction(self, nd_array: ndarray, mu_float: float, sigma_float: float):
        return scs.norm.pdf(nd_array, loc=mu_float, scale=sigma_float)

    def __plot(self, ax: object):
        '''
        fig, ax = plt.subplots()
        -ax.plot(x, y)
        -ax.hlines(y=0.2, xmin=4, xmax=20, linewidth=2, color='r')
        -plt.hlines(y=40, xmin=0, xmax=len(self._dataFrame[self._draw_col]), colors='r', linestyles='--', lw=2)
        fig.set_size_inches(3, 1.5)
        plt.savefig(file.jpeg, edgecolor='black', dpi=400, facecolor='black', transparent=True)
        '''
        # visualize data
        # plt.style.use('fivethirtyeight')
        # self._monthCount #3 * math.log(self.__stockOption.TimeSpan.MonthCount)
        # plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        # plt.tight_layout()
        # Plot the grid lines
        ax.plot(self.__dataFrame[self.__Col], label=self.__Col)
        ax.axhline(self.__price, linestyle='--', label=self.__Col + '_Price=' + str(self.__price), color='cyan',
                   alpha=0.50)
        ax.axhline(self.__median, linestyle='--', label=self.__Col + '_Median=' + str(self.__median), color='blue',
                   alpha=0.50)
        ax.axhline(self.__mean, linestyle='--', label=self.__Col + '_Mean=' + str(self.__mean), color='orange')
        ax.axhline(self.__yeHigh52, linestyle='--', label='yeHigh52=' + str(self.__yeHigh52), color='red', alpha=0.50)
        ax.axhline(self.__yeLow52, linestyle='--', label='yeLow52=' + str(self.__yeLow52), color='green', alpha=0.50)
        ax.axhline(self.__yeAverage200, linestyle='-.', label='yeAverage200=' + str(self.__yeAverage200),
                   color='yellow', alpha=0.50)
        ax.axhline(self.__yeAverage50, linestyle='-.', label='yeAverage50=' + str(self.__yeAverage50), color='orange',
                   alpha=0.50)
        ax.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
        ax.legend(loc='upper left', fontsize=8)
        # ax.axis('tight')
        return ax

    def __plotDistro(self, ax: object):
        ax = sns.distplot(self.__dataFrame[self.__Col], vertical=True, rug=True)
        ax.axhline(self.__price, linestyle='--', label=self.__Col + '_Price=' + str(self.__price), color='cyan',
                   alpha=0.50)
        ax.axhline(self.__median, linestyle='--', label=self.__Col + '_Mean=' + str(self.__median), color='blue',
                   alpha=0.50)
        ax.axhline(self.__mean, linestyle='--', label=self.__Col + '_Median=' + str(self.__mean), color='orange')
        ax.axhline((self.__mean + self.__std), linestyle='--',
                   label=self.__Col + '_+Std=' + str(self.__mean + self.__std), color='grey', alpha=0.50)
        ax.axhline((self.__mean - self.__std), linestyle='--',
                   label=self.__Col + '_-Std=' + str(self.__mean - self.__std), color='grey', alpha=0.50)
        ax.axhline(self.__yeHigh52, linestyle='--', label='yeHigh52=' + str(self.__yeHigh52), color='red', alpha=0.50)
        ax.axhline(self.__yeLow52, linestyle='--', label='yeLow52=' + str(self.__yeLow52), color='green', alpha=0.50)
        ax.axhline(self.__yeAverage200, linestyle='-.', label='yeAverage200=' + str(self.__yeAverage200),
                   color='yellow', alpha=0.50)
        ax.axhline(self.__yeAverage50, linestyle='-.', label='yeAverage50=' + str(self.__yeAverage50), color='orange',
                   alpha=0.50)
        ax.legend(loc='upper left', fontsize=8)
        # ax.axis('tight')
        return ax

    def __plotHist(self, a_df: DataFrame, timely: str = 'Daily'):
        r_range: ndarray = self.__GetRankRange(a_df)
        mu: float = a_df[self.__Col].mean()
        sigma: float = a_df[self.__Col].std()
        norm_pdf: ndarray = self.__GetProbabilityDensityFunction(r_range, mu, sigma)
        # plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        # plt.tight_layout()
        fig, ax = plt.subplots(1, 2, figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        # histogram
        # sns.distplot(self.__dataMonthly, vertical=False, rug=True)
        # plt.title(self.__ticker + ' ' + self.__Col + ' Monthly Returns ' + str(self.__timeSpan.MonthCount) + ' mts')
        # plt.ylabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        # plt.xlabel(self.__Col + ' Percent Base=1')
        # plt.legend(loc=self.__legendPlace)
        sns.distplot(a_df, vertical=False, rug=True, kde=True, norm_hist=True, ax=ax[0])
        ax[0].set_title('Distribution of ' + self.__ticker + ' ' + self.__Col + ' ' + timely + ' Returns', fontsize=16)
        ax[0].plot(r_range, norm_pdf, 'g', lw=2, label=f'N({mu:.2f}, {sigma ** 2:.4f})')
        ax[0].legend(loc=self.__legendPlace)
        # Q-Q plot
        qq = sm.qqplot(a_df[self.__Col].values, line='q', ax=ax[1])
        ax[1].set_title('Q-Q plot of ' + self.__ticker + ' ' + self.__Col + ' ' + timely + ' Returns', fontsize=16)
        return plt

    def Plot(self):
        fig, ax = plt.subplots(4, 1, figsize=(3 * math.log(self.__stockOption.TimeSpan.MonthCount), 7), sharex=True)
        plt.style.use('fivethirtyeight')
        # ax0
        self.__dataFrame[self.__Col].plot(ax=ax[0])
        ax[0].set(ylabel='Stock price ($)',
                  title=self.__ticker + ' ' + self.__Col + ' Flat ' + str(self.__timeSpan.MonthCount) + ' months')
        # ax1
        self.__dataSimpleReturns[self.__Col].plot(ax=ax[1], label='Normal')
        ax[1].scatter(self.__dataSimpleReturns.index, self.__dataSimpleReturns['Outliers'], color='red',
                      label='Anomaly')
        ax[1].set(ylabel='Simple returns (%)\n&\nOutliers')
        ax[1].legend(loc=self.__legendPlace)
        # ax2
        self.__dataLogReturns[self.__Col].plot(ax=ax[2])
        ax[2].set(ylabel='Log returns (%)')
        # ax3
        self.__dataLogReturns['MovingStd252'].plot(ax=ax[3], color='r', label='Moving Volatility 252 Day')
        self.__dataLogReturns['MovingStd21'].plot(ax=ax[3], color='g', label='Moving Volatility 21 Day')
        ax[3].set(ylabel='Moving Volatility', xlabel=self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        ax[3].legend(loc=self.__legendPlace)
        return plt

    def GraphPlot(self):
        fig1L2C = plt.figure(constrained_layout=True, figsize=(3 * math.log(self.__stockOption.TimeSpan.MonthCount), 7))
        gs1L2C = gridspec.GridSpec(ncols=2, nrows=1, width_ratios=[3, 2], figure=fig1L2C)
        plt.style.use('fivethirtyeight')
        ax1 = fig1L2C.add_subplot(gs1L2C[0, 0])
        ax1 = self.__plot(ax1)
        ax2 = fig1L2C.add_subplot(gs1L2C[0, 1])
        ax2 = self.__plotDistro(ax2)
        plt.tight_layout()
        return plt

    def __plotPeriod(self, a_df: DataFrame, period_str: str = 'Daily'):
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.plot(a_df, label=self.__Col)
        plt.title(self.__ticker + ' ' + self.__Col + ' ' + period_str + ' Returns ' + str(self.__timeSpan.MonthCount) + ' mtonths')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.ylabel(self.__Col + ' Percent Base=1')
        plt.legend(loc=self.__legendPlace)
        return plt

    def Daily(self):
        return self.__plotPeriod(self.__dataDaily, 'Daily')

    def Monthly(self):
        return self.__plotPeriod(self.__dataMonthly, 'Monthly')

    def DailyCum(self):
        modelDailyDrop = self.__dataDailyCum[self.__Col].dropna()
        modelDailyModel = arch_model(modelDailyDrop, mean='Zero', vol='ARCH', p=1, o=0, q=0)
        modelDailyFitted = modelDailyModel.fit(disp='off')
        # modelDailyFitted.plot(annualize='D')
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.plot(self.__dataDailyCum, label=self.__Col)
        plt.title(self.__ticker + ' ' + self.__Col + ' Cumm. Daily Returns ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.ylabel(self.__Col + ' 1$ Growth Investment')
        plt.legend(loc=self.__legendPlace)
        return plt

    def MonthlyCum(self):
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.plot(self.__dataMonthlyCum, label=self.__Col)
        plt.title(
            self.__ticker + ' ' + self.__Col + ' Cumm. Monthly Returns ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.ylabel(self.__Col + ' 1$ Growth Investment')
        plt.legend(loc=self.__legendPlace)
        return plt

    def DailyHist(self):
        return self.__plotHist(self.__dataDaily, 'Daily')

    def MonthlyHist(self):
        return self.__plotHist(self.__dataMonthly, 'Monthly')
