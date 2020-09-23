import math
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scs
import seaborn as sns
import statsmodels.api as sm
from numpy import ndarray
from pandas import DataFrame
from pandas import Series
from arch import arch_model
from Common.Plotters.AbstractPlotter import AbstractPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class HistoricalPlotter(AbstractPlotter):
    _dataSimpleReturns: DataFrame
    _dataLogReturns: DataFrame
    _dataDaily: DataFrame
    _dataDailyCum: Series
    _dataMonthly: DataFrame
    _dataMonthlyCum: Series
    _mean: ndarray
    _median: ndarray
    _std: ndarray
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
            self.__Col = "Adj Close"
        self.__dataFrame = stock_option.HistoricalData
        '''self.__dataTreeRegPrediction = y_stockOption.HistoricalTreeRegPrediction
        self.__dataTreeRegScore = round(y_stockOption.HistoricalTreeRegScore, 5)
        self.__dataLinearRegPrediction = y_stockOption.HistoricalLinRegPrediction
        self.__dataLinearRegScore = round(y_stockOption.HistoricalLinRegScore, 5)
        self.__dataSVRLinearPrediction = y_stockOption.HistoricalSVRLinearPrediction
        self.__dataSVRLinearScore = round(y_stockOption.HistoricalSVRLinearScore, 5)
        self.__dataSVRPolyPrediction = y_stockOption.HistoricalSVRPolyPrediction
        self.__dataSVRPolyScore = round(y_stockOption.HistoricalSVRPolyScore, 5)
        self.__dataSVRrbfPrediction = y_stockOption.HistoricalSVRRbfPrediction
        self.__dataSVRrbfScore = round(y_stockOption.HistoricalSVRRbfScore, 5)
        self.__dataXarray = y_stockOption.Xarray'''
        self._dataSimpleReturns = stock_option.HistoricalSimpleReturns
        self._dataLogReturns = stock_option.HistoricalLogReturns
        self._dataDaily = stock_option.HistoricalDaily
        self._dataDailyCum = stock_option.HistoricalDailyCum
        self._dataMonthly = stock_option.HistoricalMonthly
        self._dataMonthlyCum = stock_option.HistoricalMonthlyCum
        self._mean = np.mean(stock_option.HistoricalData[self.__Col])
        self._mean = np.round(self._mean, 2)
        self._median = np.median(stock_option.HistoricalData[self.__Col])
        self._median = np.round(self._median, 2)
        self._std = np.std(stock_option.HistoricalData[self.__Col])
        self._std = np.round(self._std, 2)
        self.__src = stock_option.Source
        self.__legendPlace = 'upper left'
        self.__ticker = stock_option.Ticker
        self.__timeSpan = stock_option.TimeSpan
        self._stockOption = stock_option

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
        plus1sd = np.round(self._mean + self._std, 2)
        plus2sd = np.round(self._mean + 2 * self._std, 2)
        minus1sd = np.round(self._mean - self._std, 2)
        minus2sd = np.round(self._mean - 2 * self._std, 2)
        price_label: str = self.__Col + '_Price=' + str(self._price)
        median_label: str = self.__Col + '_Median=' + str(self._median)
        mean_label: str = self.__Col + '_Mean=' + str(self._mean)
        high52_label: str = 'High52=' + str(self._yeHigh52)
        low52_label: str = 'Low52=' + str(self._yeLow52)
        mean200_label: str = 'Average200=' + str(self._yeAverage200)
        mean50_label: str = 'Average50=' + str(self._yeAverage50)
        plus1_label: str = self.__Col + '_+1Std=' + str(plus1sd)
        plus2_label: str = self.__Col + '_+2Std=' + str(plus2sd)
        minus1_label: str = self.__Col + '_-1Std=' + str(minus1sd)
        minus2_label: str = self.__Col + '_-2Std=' + str(minus2sd)
        ax.plot(self.__dataFrame[self.__Col], label=self.__Col)
        ax.axhline(self._price, linestyle='--', label=price_label, color='cyan', alpha=0.50)
        ax.axhline(self._median, linestyle='--', label=median_label, color='blue', alpha=0.50)
        ax.axhline(self._mean, linestyle='--', label=mean_label, color='orange')
        ax.axhline(plus1sd, linestyle='--', label=plus1_label, color='grey', alpha=0.50)
        ax.axhline(plus2sd, linestyle='--', label=plus2_label, color='grey', alpha=0.35)
        ax.axhline(minus1sd, linestyle='--', label=minus1_label, color='grey', alpha=0.50)
        ax.axhline(minus2sd, linestyle='--', label=minus2_label, color='grey', alpha=0.35)
        ax.axhline(self._yeHigh52, linestyle='--', label=high52_label, color='red', alpha=0.50)
        ax.axhline(self._yeLow52, linestyle='--', label=low52_label, color='green', alpha=0.50)
        ax.axhline(self._yeAverage200, linestyle='-.', label=mean200_label, color='yellow', alpha=0.50)
        ax.axhline(self._yeAverage50, linestyle='-.', label=mean50_label, color='orange', alpha=0.50)
        ax.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
        ax.legend(loc=self.__legendPlace, fontsize=8)
        # ax.axis('tight')
        return ax

    def __plotDistro(self, ax: object):
        plus1sd = np.round(self._mean + self._std, 2)
        plus2sd = np.round(self._mean + 2 * self._std, 2)
        minus1sd = np.round(self._mean - self._std, 2)
        minus2sd = np.round(self._mean - 2 * self._std, 2)
        price_label: str = self.__Col + '_Price=' + str(self._price)
        median_label: str = self.__Col + '_Median=' + str(self._median)
        mean_label: str = self.__Col + '_Mean=' + str(self._mean)
        high52_label: str = 'High52=' + str(self._yeHigh52)
        low52_label: str = 'Low52=' + str(self._yeLow52)
        mean200_label: str = 'Average200=' + str(self._yeAverage200)
        mean50_label: str = 'Average50=' + str(self._yeAverage50)
        plus1_label: str = self.__Col + '_+1Std=' + str(plus1sd)
        plus2_label: str = self.__Col + '_+2Std=' + str(plus2sd)
        minus1_label: str = self.__Col + '_-1Std=' + str(minus1sd)
        minus2_label: str = self.__Col + '_-2Std=' + str(minus2sd)
        ax = sns.distplot(self.__dataFrame[self.__Col], vertical=True, rug=True)
        ax.axhline(self._price, linestyle='--', label=price_label, color='cyan', alpha=0.50)
        ax.axhline(self._median, linestyle='--', label=median_label, color='blue', alpha=0.50)
        ax.axhline(self._mean, linestyle='--', label=mean_label, color='orange')
        ax.axhline(plus1sd, linestyle='--', label=plus1_label, color='grey', alpha=0.50)
        ax.axhline(plus2sd, linestyle='--', label=plus2_label, color='grey', alpha=0.35)
        ax.axhline(minus1sd, linestyle='--', label=minus1_label, color='grey', alpha=0.50)
        ax.axhline(minus2sd, linestyle='--', label=minus2_label, color='grey', alpha=0.35)
        ax.axhline(self._yeHigh52, linestyle='--', label=high52_label, color='red', alpha=0.50)
        ax.axhline(self._yeLow52, linestyle='--', label=low52_label, color='green', alpha=0.50)
        ax.axhline(self._yeAverage200, linestyle='-.', label=mean200_label, color='yellow', alpha=0.50)
        ax.axhline(self._yeAverage50, linestyle='-.', label=mean50_label, color='orange', alpha=0.50)
        ax.legend(loc=self.__legendPlace, fontsize=8)
        # ax.axis('tight')
        return ax

    def __newPeriodDist(self, an_ax, a_df: DataFrame, period_str: str):
        r_range: ndarray = self.__GetRankRange(a_df)
        mu: float = a_df[self.__Col].mean()
        sigma: float = a_df[self.__Col].std()
        norm_pdf: ndarray = self.__GetProbabilityDensityFunction(r_range, mu, sigma)
        sns.distplot(a_df, vertical=False, rug=True, kde=True, norm_hist=True, ax=an_ax)
        an_ax.set_title('Distribution of ' + self.__ticker + ' ' + self.__Col + ' ' + period_str + ' Returns', fontsize=12)
        an_ax.plot(r_range, norm_pdf, 'g', lw=2, label=f'N({mu:.2f}, {sigma ** 2:.4f})')
        an_ax.legend(loc=self.__legendPlace)
        plt.tight_layout()
        return an_ax

    def __newPeriodQqPlot(self, an_ax, a_df: DataFrame, period_str: str):
        sm.qqplot(a_df[self.__Col].values, line='q', ax=an_ax)
        an_ax.set_title('Q-Q plot of ' + self.__ticker + ' ' + self.__Col + ' ' + period_str + ' Returns', fontsize=12)
        return an_ax

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
        a_title: str = self.__ticker + ' ' + self.__Col + ' Flat ' + str(self.__timeSpan.MonthCount) + ' months'
        x_label: str = self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr
        plt.style.use('seaborn')
        fig, ax = plt.subplots(4, 1, figsize=(3 * math.log(self._stockOption.TimeSpan.MonthCount), 5.5), sharex=True)
        # ax0
        self.__dataFrame[self.__Col].plot(ax=ax[0])
        ax[0].set(ylabel='Stock price ($)', title=a_title)
        # ax1
        self._dataSimpleReturns[self.__Col].plot(ax=ax[1], label='Normal')
        ax[1].scatter(self._dataSimpleReturns.index, self._dataSimpleReturns['Outliers'], color='red', label='Anomaly')
        ax[1].set(ylabel='Simple returns (%)\n&\nOutliers')
        ax[1].legend(loc=self.__legendPlace)
        # ax2
        self._dataLogReturns[self.__Col].plot(ax=ax[2])
        ax[2].set(ylabel='Log returns (%)')
        # ax3
        self._dataLogReturns['MovingStd252'].plot(ax=ax[3], color='r', label='Moving Volatility 252 Day')
        self._dataLogReturns['MovingStd21'].plot(ax=ax[3], color='g', label='Moving Volatility 21 Day')
        ax[3].set(ylabel='Moving Volatility', xlabel=x_label)
        ax[3].legend(loc=self.__legendPlace)
        plt.tight_layout()
        return plt

    def PlotForecast(self):
        forecast_df: DataFrame = self.__dataFrame[self.__dataXarray.shape[0]:]
        title: str = ' Model '
        x_label: str = 'Days'
        label: str = 'Predictions'
        #
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.title('Tree Regression Prediction' + title + 'Score=' + str(self.__dataTreeRegScore))
        plt.xlabel(x_label)
        plt.ylabel(self.__Col)
        plt.scatter(self.__dataFrame.index, self.__dataFrame[self.__Col], color='black')
        plt.plot(self.__dataFrame[self.__Col])
        forecast_df[label] = self.__dataTreeRegPrediction
        plt.plot(forecast_df[[self.__Col, label]])
        plt.legend([self.__Col, self.__Col + 'Training', self.__Col + 'Predicted'])
        plt.show()
        #
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.title('Linear Regression Prediction' + title + 'Score=' + str(self.__dataLinearRegScore))
        plt.xlabel(x_label)
        plt.ylabel(self.__Col)
        plt.scatter(self.__dataFrame.index, self.__dataFrame[self.__Col], color='black')
        plt.plot(self.__dataFrame[self.__Col])
        forecast_df[label] = self.__dataLinearRegPrediction
        plt.plot(forecast_df[[self.__Col, label]])
        plt.legend([self.__Col, self.__Col + 'Training', self.__Col + 'Predicted'])
        plt.show()
        #
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.title('SVR Linear Regression Prediction' + title + 'Score=' + str(self.__dataSVRLinearScore))
        plt.xlabel(x_label)
        plt.ylabel(self.__Col)
        plt.scatter(self.__dataFrame.index, self.__dataFrame[self.__Col], color='black')
        plt.plot(self.__dataFrame[self.__Col])
        forecast_df[label] = self.__dataSVRLinearPrediction
        plt.plot(forecast_df[[self.__Col, label]])
        plt.legend([self.__Col, self.__Col + 'Training', self.__Col + 'Predicted'])
        plt.show()
        #
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.title('SVR Polynomial Regression Prediction' + title + 'Score=' + str(self.__dataSVRPolyScore))
        plt.xlabel(x_label)
        plt.ylabel(self.__Col)
        plt.scatter(self.__dataFrame.index, self.__dataFrame[self.__Col], color='black')
        plt.plot(self.__dataFrame[self.__Col])
        forecast_df[label] = self.__dataSVRPolyPrediction
        plt.plot(forecast_df[[self.__Col, label]])
        plt.legend([self.__Col, self.__Col + 'Training', self.__Col + 'Predicted'])
        plt.show()
        #
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.title('SVR RBF Regression Prediction' + title + 'Score=' + str(self.__dataSVRrbfScore))
        plt.xlabel(x_label)
        plt.ylabel(self.__Col)
        plt.scatter(self.__dataFrame.index, self.__dataFrame[self.__Col], color='black')
        plt.plot(self.__dataFrame[self.__Col])
        forecast_df[label] = self.__dataSVRrbfPrediction
        plt.plot(forecast_df[[self.__Col, label]])
        plt.legend([self.__Col, self.__Col + 'Training', self.__Col + 'Predicted'])
        return plt

    def GraphPlot(self):
        a_title: str = self.__ticker + ' ' + self.__Col + ' Flat ' + str(self.__timeSpan.MonthCount) + ' months'
        fig = plt.figure(constrained_layout=True, figsize=(3 * math.log(self._stockOption.TimeSpan.MonthCount), 7))
        fig.suptitle(a_title)
        gs = gridspec.GridSpec(ncols=2, nrows=1, width_ratios=[3, 2], figure=fig)
        plt.style.use('seaborn')
        ax1 = fig.add_subplot(gs[0, 0])
        ax1 = self.__plot(ax1)
        ax2 = fig.add_subplot(gs[0, 1])
        ax2 = self.__plotDistro(ax2)
        plt.tight_layout()
        return plt

    def __newPlot(self, df_period: DataFrame, df_periodCum: DataFrame, period_str: str = 'Daily'):
        a_title: str = self.__ticker + ' ' + self.__Col + ' ' + period_str + ' ' + str(self.__timeSpan.MonthCount) + ' months'
        x_label: str = self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr
        a_float: float = 3 * math.log(self._stockOption.TimeSpan.MonthCount)
        fig, ax = plt.subplots(2, 2, figsize=(a_float, a_float), sharex=False)
        fig.suptitle(a_title)
        plt.style.use('seaborn')
        # ax0
        ax[0, 0] = self.__newPeriod(ax[0, 0], df_period, period_str)
        # ax1
        ax[0, 1] = self.__newPeriodCum(ax[0, 1], df_periodCum, period_str)
        # ax2
        ax[1, 0] = self.__newPeriodDist(ax[1, 0], df_period, period_str)
        # ax3
        ax[1, 1] = self.__newPeriodQqPlot(ax[1, 1], df_period, period_str)
        plt.tight_layout()
        return plt

    def __newPeriod(self, an_ax, a_df: DataFrame, period_str: str):
        an_ax.plot(a_df, label=self.__Col)
        an_ax.legend(loc=self.__legendPlace)
        an_ax.set(ylabel=self.__Col + ' Percent Base=1')
        return an_ax

    def __plotPeriod(self, a_df: DataFrame, period_str: str = 'Daily'):
        a_title: str = self.__ticker + ' ' + self.__Col + ' ' + period_str + ' Returns ' + str(self.__timeSpan.MonthCount) + ' months'
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.plot(a_df, label=self.__Col)
        plt.title(a_title)
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.ylabel(self.__Col + ' Percent Base=1')
        plt.legend(loc=self.__legendPlace)
        return plt

    def __newPeriodCum(self, an_ax, a_df: DataFrame, period_str: str):
        modelDailyDrop = a_df[self.__Col].dropna()
        modelDailyModel = arch_model(modelDailyDrop, mean='Zero', vol='ARCH', p=1, o=0, q=0)
        modelDailyFitted = modelDailyModel.fit(disp='off')
        # modelDailyFitted.plot(annualize='D')
        avg_return = 100 * modelDailyDrop.mean()
        avg_return_str: str = f'{avg_return:.2f}%'
        print(f'Average return: {100 * modelDailyDrop.mean():.2f}%')
        a_title: str = f'{self.__ticker} {self.__Col} ({avg_return_str}) Cumulative {period_str} Returns {self.__timeSpan.MonthCount} months'
        an_ax.plot(a_df, label=self.__Col)
        an_ax.legend(loc=self.__legendPlace)
        an_ax.set_title(a_title, fontsize=10)
        an_ax.set(ylabel=self.__Col + ' 1$ Growth Invested')
        return an_ax

    def __plotPeriodCum(self, a_df: DataFrame, a_period: str = 'Daily'):
        modelDailyDrop = a_df[self.__Col].dropna()
        modelDailyModel = arch_model(modelDailyDrop, mean='Zero', vol='ARCH', p=1, o=0, q=0)
        modelDailyFitted = modelDailyModel.fit(disp='off')
        # modelDailyFitted.plot(annualize='D')
        avg_return = 100 * modelDailyDrop.mean()
        avg_return_str: str = f'{avg_return:.2f}%'
        print(f'Average return: {100 * modelDailyDrop.mean():.2f}%')
        a_title: str = f'{self.__ticker} {self.__Col} ({avg_return_str}) Cumulative {a_period} Returns {self.__timeSpan.MonthCount} months'
        plt.figure(figsize=(3 * math.log(self.__timeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.plot(a_df, label=self.__Col)
        plt.title(a_title)
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.ylabel(self.__Col + ' 1$ Growth Invested')
        plt.legend(loc=self.__legendPlace)
        return plt

    def Daily(self):
        return self.__plotPeriod(self._dataDaily, 'Daily')

    def Monthly(self):
        return self.__plotPeriod(self._dataMonthly, 'Monthly')

    def DailyCum(self):
        return self.__plotPeriodCum(self._dataDailyCum, 'Daily')

    def MonthlyCum(self):
        return self.__plotPeriodCum(self._dataMonthlyCum, 'Monthly')

    def DailyHist(self):
        return self.__plotHist(self._dataDaily, 'Daily')

    def MonthlyHist(self):
        return self.__plotHist(self._dataMonthly, 'Monthly')

    def PlotDaily(self):
        return self.__newPlot(self._dataDaily, self._dataDailyCum, 'Daily')

    def PlotMonthly(self):
        return self.__newPlot(self._dataMonthly, self._dataMonthlyCum, 'Monthly')
