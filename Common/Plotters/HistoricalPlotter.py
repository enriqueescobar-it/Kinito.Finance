import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scs
import seaborn as sns
import statsmodels.api as sm
from numpy import ndarray
from pandas import DataFrame
from arch import arch_model
from Common.Plotters.AbstractPlotter import AbstractPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class HistoricalPlotter(AbstractPlotter):
    _stock_option: YahooStockOption
    _price: float
    _yeAverage200: float
    _yeAverage50: float
    _yeHigh52: float
    _yeLow52: float

    def __init__(self, stock_option: YahooStockOption):
        self._price = np.round(stock_option.FvPrice, 2)
        self._yeHigh52 = np.round(stock_option.YeHigh52, 2)
        self._yeLow52 = np.round(stock_option.YeLow52, 2)
        self._yeAverage50 = np.round(stock_option.YeAverage50, 2)
        self._yeAverage200 = np.round(stock_option.YeAverage200, 2)
        if stock_option.Source == 'yahoo':
            self._col = "Adj Close"
        self._data_frame = stock_option.HistoricalData
        self._legend_place = 'upper left'
        self._ticker = stock_option.Ticker
        self._time_span = stock_option.TimeSpan
        self._stock_option = stock_option

    def Plot(self):
        a_title: str = self._ticker + ' ' + self._col + ' Flat ' + str(self._time_span.MonthCount) + ' months'
        x_label: str = self._time_span.StartDateStr + ' - ' + self._time_span.EndDateStr
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31 00:00:00'
        fig, ax = plt.subplots(4, 1, figsize=(3 * math.log(self._stock_option.TimeSpan.MonthCount), 5.5), sharex=True)
        # ax0
        self._data_frame[self._col].plot(ax=ax[0])
        ax[0].set(ylabel='Stock price ($)', title=a_title)
        # ax1
        self._stock_option.DataSimpleReturns[self._col].plot(ax=ax[1], label='Normal')
        ax[1].scatter(self._stock_option.DataSimpleReturns.index,
                      self._stock_option.DataSimpleReturns['Outliers'], color='red', label='Anomaly')
        ax[1].set(ylabel='Simple returns (%)\n&\nOutliers')
        ax[1].legend(loc=self._legend_place)
        # ax2
        self._stock_option.DataLogReturns[self._col].plot(ax=ax[2])
        ax[2].set(ylabel='Log returns (%)')
        # ax3
        self._stock_option.DataLogReturns['MovingStd252'].plot(ax=ax[3], color='r', label='Moving Volatility 252 Day')
        self._stock_option.DataLogReturns['MovingStd21'].plot(ax=ax[3], color='g', label='Moving Volatility 21 Day')
        ax[3].set(ylabel='Moving Volatility', xlabel=x_label)
        ax[3].legend(loc=self._legend_place)
        plt.tight_layout()
        return plt

    def GraphPlot(self):
        a_float: float = 3 * math.log(self._stock_option.TimeSpan.MonthCount)
        a_title: str = self._ticker + ' ' + self._col + ' Flat ' + str(self._time_span.MonthCount) + ' months'
        fig, ax = plt.subplots(1, 2, figsize=(a_float, a_float), sharey=True)
        fig.suptitle(a_title)
        plt.style.use('seaborn')
        self._getDataPlot(ax[0])
        self._getDataDistro(ax[1])
        plt.tight_layout()
        return plt

    def _getDataPlot(self, ax: object):
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
        plus1sd = np.round(self._stock_option.Mu + self._stock_option.Sigma, 2)
        plus2sd = np.round(self._stock_option.Mu + 2 * self._stock_option.Sigma, 2)
        minus1sd = np.round(self._stock_option.Mu - self._stock_option.Sigma, 2)
        minus2sd = np.round(self._stock_option.Mu - 2 * self._stock_option.Sigma, 2)
        price_label: str = self._col + '_Price=' + str(self._price)
        median_label: str = self._col + '_Median=' + str(self._stock_option.Median)
        mean_label: str = self._col + '_Mean=' + str(self._stock_option.Mu)
        high52_label: str = 'High52=' + str(self._yeHigh52)
        low52_label: str = 'Low52=' + str(self._yeLow52)
        mean200_label: str = 'Average200=' + str(self._yeAverage200)
        mean50_label: str = 'Average50=' + str(self._yeAverage50)
        plus1_label: str = self._col + '_+1Std=' + str(plus1sd)
        plus2_label: str = self._col + '_+2Std=' + str(plus2sd)
        minus1_label: str = self._col + '_-1Std=' + str(minus1sd)
        minus2_label: str = self._col + '_-2Std=' + str(minus2sd)
        ax.plot(self._data_frame[self._col], label=self._col)
        ax.axhline(self._price, linestyle='--', label=price_label, color='cyan', alpha=0.50)
        ax.axhline(self._stock_option.Median, linestyle='--', label=median_label, color='blue', alpha=0.50)
        ax.axhline(self._stock_option.Mu, linestyle='--', label=mean_label, color='orange')
        ax.axhline(plus1sd, linestyle='--', label=plus1_label, color='grey', alpha=0.50)
        ax.axhline(plus2sd, linestyle='--', label=plus2_label, color='grey', alpha=0.35)
        ax.axhline(minus1sd, linestyle='--', label=minus1_label, color='grey', alpha=0.50)
        ax.axhline(minus2sd, linestyle='--', label=minus2_label, color='grey', alpha=0.35)
        ax.axhline(self._yeHigh52, linestyle='--', label=high52_label, color='red', alpha=0.50)
        ax.axhline(self._yeLow52, linestyle='--', label=low52_label, color='green', alpha=0.50)
        ax.axhline(self._yeAverage200, linestyle='-.', label=mean200_label, color='yellow', alpha=0.50)
        ax.axhline(self._yeAverage50, linestyle='-.', label=mean50_label, color='orange', alpha=0.50)
        ax.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
        ax.legend(loc=self._legend_place, fontsize=8)
        # ax.axis('tight')
        return ax

    def _getDataDistro(self, ax: object):
        plus1sd = np.round(self._stock_option.Mu + self._stock_option.Sigma, 2)
        plus2sd = np.round(self._stock_option.Mu + 2 * self._stock_option.Sigma, 2)
        minus1sd = np.round(self._stock_option.Mu - self._stock_option.Sigma, 2)
        minus2sd = np.round(self._stock_option.Mu - 2 * self._stock_option.Sigma, 2)
        price_label: str = self._col + '_Price=' + str(self._price)
        median_label: str = self._col + '_Median=' + str(self._stock_option.Median)
        mean_label: str = self._col + '_Mean=' + str(self._stock_option.Mu)
        high52_label: str = 'High52=' + str(self._yeHigh52)
        low52_label: str = 'Low52=' + str(self._yeLow52)
        mean200_label: str = 'Average200=' + str(self._yeAverage200)
        mean50_label: str = 'Average50=' + str(self._yeAverage50)
        plus1_label: str = self._col + '_+1Std=' + str(plus1sd)
        plus2_label: str = self._col + '_+2Std=' + str(plus2sd)
        minus1_label: str = self._col + '_-1Std=' + str(minus1sd)
        minus2_label: str = self._col + '_-2Std=' + str(minus2sd)
        ax = sns.distplot(self._data_frame[self._col], vertical=True, rug=True)
        ax.axhline(self._price, linestyle='--', label=price_label, color='cyan', alpha=0.50)
        ax.axhline(self._stock_option.Median, linestyle='--', label=median_label, color='blue', alpha=0.50)
        ax.axhline(self._stock_option.Mu, linestyle='--', label=mean_label, color='orange')
        ax.axhline(plus1sd, linestyle='--', label=plus1_label, color='grey', alpha=0.50)
        ax.axhline(plus2sd, linestyle='--', label=plus2_label, color='grey', alpha=0.35)
        ax.axhline(minus1sd, linestyle='--', label=minus1_label, color='grey', alpha=0.50)
        ax.axhline(minus2sd, linestyle='--', label=minus2_label, color='grey', alpha=0.35)
        ax.axhline(self._yeHigh52, linestyle='--', label=high52_label, color='red', alpha=0.50)
        ax.axhline(self._yeLow52, linestyle='--', label=low52_label, color='green', alpha=0.50)
        ax.axhline(self._yeAverage200, linestyle='-.', label=mean200_label, color='yellow', alpha=0.50)
        ax.axhline(self._yeAverage50, linestyle='-.', label=mean50_label, color='orange', alpha=0.50)
        ax.legend(loc=self._legend_place, fontsize=8)
        # ax.axis('tight')
        return ax

    def Daily(self):
        return self._getPeriodPlot(self._stock_option.SimpleDaily, 'Daily')

    def Weekly(self):
        return self._getPeriodPlot(self._stock_option.SimpleWeekly, 'Weekly')

    def Monthly(self):
        return self._getPeriodPlot(self._stock_option.SimpleMonthly, 'Monthly')

    def Quarterly(self):
        return self._getPeriodPlot(self._stock_option.SimpleQuarterly, 'Quarterly')

    def Annually(self):
        return self._getPeriodPlot(self._stock_option.SimpleAnnually, 'Annually')

    def _getPeriodPlot(self, a_df: DataFrame, period_str: str = 'Daily'):
        a_title: str = self._ticker + ' ' + self._col + ' ' + period_str + ' Returns ' + str(self._time_span.MonthCount) + ' months'
        plt.rcParams['date.epoch'] = '0000-12-31'
        plt.figure(figsize=(3 * math.log(self._time_span.MonthCount), 4.5))
        plt.tight_layout()
        plt.plot(a_df, label=self._col)
        plt.title(a_title)
        plt.xlabel(self._time_span.StartDateStr + ' - ' + self._time_span.EndDateStr)
        plt.ylabel(self._col + ' Percent Base=1')
        plt.legend(loc=self._legend_place)
        return plt

    def DailyCum(self):
        return self._getPeriodCumPlot(self._stock_option.SimplyDailyCum, 'Daily')

    def WeeklyCum(self):
        return self._getPeriodCumPlot(self._stock_option.SimpleWeeklyCum, 'Weekly')

    def MonthlyCum(self):
        return self._getPeriodCumPlot(self._stock_option.SimpleMonthlyCum, 'Monthly')

    def QuarterlyCum(self):
        return self._getPeriodCumPlot(self._stock_option.SimpleQuarterlyCum, 'Quarterly')

    def AnnuallyCum(self):
        return self._getPeriodCumPlot(self._stock_option.SimpleAnnuallyCum, 'Annually')

    def _getPeriodCumPlot(self, a_df: DataFrame, a_period: str = 'Daily'):
        modelDailyDrop = a_df[self._col].dropna()
        modelDailyModel = arch_model(modelDailyDrop, mean='Zero', vol='ARCH', p=1, o=0, q=0)
        modelDailyFitted = modelDailyModel.fit(disp='off')
        # modelDailyFitted.plot(annualize='D')
        avg_return = 100 * modelDailyDrop.mean()
        avg_return_str: str = f'{avg_return:.2f}%'
        print(f'Average return {a_period}: {100 * modelDailyDrop.mean():.2f}%')
        a_title: str = f'{self._ticker} {self._col} ({avg_return_str}) Cumulative {a_period} Returns {self._time_span.MonthCount} months'
        plt.figure(figsize=(3 * math.log(self._time_span.MonthCount), 4.5))
        plt.tight_layout()
        plt.plot(a_df, label=self._col)
        plt.title(a_title)
        plt.xlabel(self._time_span.StartDateStr + ' - ' + self._time_span.EndDateStr)
        plt.ylabel(self._col + ' 1$ Growth Invested')
        plt.legend(loc=self._legend_place)
        return plt

    def DailyHist(self):
        return self._getPeriodHist(self._stock_option.SimpleDaily, 'Daily')

    def MonthlyHist(self):
        return self._getPeriodHist(self._stock_option.SimpleMonthly, 'Monthly')

    def _getPeriodHist(self, a_df: DataFrame, timely: str = 'Daily'):
        # plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        # plt.tight_layout()
        fig, ax = plt.subplots(1, 2, figsize=(3 * math.log(self._time_span.MonthCount), 4.5))
        # histogram
        # sns.distplot(self.__dataMonthly, vertical=False, rug=True)
        # plt.title(self.__ticker + ' ' + self.__Col + ' Monthly Returns ' + str(self.__timeSpan.MonthCount) + ' mts')
        # plt.ylabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        # plt.xlabel(self.__Col + ' Percent Base=1')
        # plt.legend(loc=self.__legendPlace)
        sns.distplot(a_df, vertical=False, rug=True, kde=True, norm_hist=True, ax=ax[0])
        ax[0].set_title('Distribution of ' + self._ticker + ' ' + self._col + ' ' + timely + ' Returns', fontsize=16)
        ax[0].plot(self._stock_option.DataRange, self._stock_option.NormProbDensityFn, 'g', lw=2, label=f'N({self._stock_option.Mu:.2f}, {self._stock_option.Sigma ** 2:.4f})')
        ax[0].legend(loc=self._legend_place)
        # Q-Q plot
        qq = sm.qqplot(a_df[self._col].values, line='q', ax=ax[1])
        ax[1].set_title('Q-Q plot of ' + self._ticker + ' ' + self._col + ' ' + timely + ' Returns', fontsize=16)
        return plt  
    
    def PlotTimely(self):
        if self._stock_option.IsDaily:
            self._plotDaily().show()
        if self._stock_option.IsWeekly:
            self._plotWeekly().show()
        if self._stock_option.IsMonthly:
            self._plotMonthly().show()
        if self._stock_option.IsQuarterly:
            self._plotQuarterly().show()
        if self._stock_option.IsAnnually:
            self._plotAnnually().show()

    def _plotDaily(self):
        return self._getTimelyPlot(self._stock_option.SimpleDaily, self._stock_option.SimplyDailyCum, 'Daily')

    def _plotWeekly(self):
        return self._getTimelyPlot(self._stock_option.SimpleWeekly, self._stock_option.SimpleWeeklyCum, 'Weekly')

    def _plotMonthly(self):
        return self._getTimelyPlot(self._stock_option.SimpleMonthly, self._stock_option.SimpleMonthlyCum, 'Monthly')

    def _plotQuarterly(self):
        return self._getTimelyPlot(self._stock_option.SimpleQuarterly, self._stock_option.SimpleQuarterlyCum, 'Quarterly')

    def _plotAnnually(self):
        return self._getTimelyPlot(self._stock_option.SimpleAnnually, self._stock_option.SimpleAnnuallyCum, 'Annually')

    def _getTimelyPlot(self, df_period: DataFrame, df_periodCum: DataFrame, period_str: str = 'Daily') -> plt:
        a_title: str = self._ticker + ' ' + self._col + ' ' + period_str + ' ' + str(self._time_span.MonthCount) + ' months'
        x_label: str = self._time_span.StartDateStr + ' - ' + self._time_span.EndDateStr
        a_float: float = 3 * math.log(self._stock_option.TimeSpan.MonthCount)
        fig, ax = plt.subplots(2, 2, figsize=(a_float, a_float), sharex=False)
        fig.suptitle(a_title)
        plt.style.use('seaborn')
        # ax0
        ax[0, 0] = self.__getTimelyPeriod(ax[0, 0], df_period, period_str)
        # ax1
        ax[0, 1] = self.__getTimelyPeriodCum(ax[0, 1], df_periodCum, period_str)
        # ax2
        ax[1, 0] = self.__getTimelyPeriodDist(ax[1, 0], df_period, period_str)
        # ax3
        ax[1, 1] = self.__getTimelyPeriodQqPlot(ax[1, 1], df_period, period_str)
        plt.tight_layout()
        return plt

    def __getTimelyPeriod(self, an_ax, a_df: DataFrame, period_str: str):
        an_ax.plot(a_df, label=self._col)
        an_ax.legend(loc=self._legend_place)
        an_ax.set(ylabel=self._col + ' Percent Base=1')
        return an_ax

    def __getTimelyPeriodCum(self, an_ax, a_df: DataFrame, a_period: str):
        modelDailyDrop = a_df[self._col].dropna()
        modelDailyModel = arch_model(modelDailyDrop, mean='Zero', vol='ARCH', p=1, o=0, q=0)
        modelDailyFitted = modelDailyModel.fit(disp='off')
        # modelDailyFitted.plot(annualize='D')
        avg_return = 100 * modelDailyDrop.mean()
        avg_return_str: str = f'{avg_return:.2f}%'
        print(f'Average return {a_period}: {100 * modelDailyDrop.mean():.2f}%')
        a_title: str = f'{self._ticker} {self._col} ({avg_return_str}) Cumulative {a_period} Returns {self._time_span.MonthCount} months'
        an_ax.plot(a_df, label=self._col)
        an_ax.legend(loc=self._legend_place)
        an_ax.set_title(a_title, fontsize=10)
        an_ax.set(ylabel=self._col + ' 1$ Growth Invested')
        return an_ax

    def __getTimelyPeriodDist(self, an_ax, a_df: DataFrame, period_str: str):
        r_range: ndarray = np.linspace(min(a_df[self._col]), max(a_df[self._col]), num=1000)
        mu: float = a_df[self._col].mean()
        sigma: float = a_df[self._col].std()
        norm_pdf: ndarray = scs.norm.pdf(r_range, loc=mu, scale=sigma)
        sns.distplot(a_df, vertical=False, rug=True, kde=True, norm_hist=True, ax=an_ax)
        an_ax.set_title('Distribution of ' + self._ticker + ' ' + self._col + ' ' + period_str + ' Returns', fontsize=12)
        an_ax.plot(r_range, norm_pdf, 'g', lw=2, label=f'N({mu:.2f}, {sigma ** 2:.4f})')
        an_ax.legend(loc=self._legend_place)
        plt.tight_layout()
        return an_ax

    def __getTimelyPeriodQqPlot(self, an_ax, a_df: DataFrame, period_str: str):
        sm.qqplot(a_df[self._col].values, line='q', ax=an_ax)
        an_ax.set_title('Q-Q plot of ' + self._ticker + ' ' + self._col + ' ' + period_str + ' Returns', fontsize=12)
        return an_ax
