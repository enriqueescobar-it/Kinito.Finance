import math
from sklearn import preprocessing
from Common.Comparators.Portfolio.AbstractPortfolioComparator import AbstractPortfolioComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from pandas import DataFrame, np
from numpy import ndarray
import seaborn as sns
import matplotlib.pyplot as plt
from heatmapcluster import heatmapcluster


class PortfolioComparator(AbstractPortfolioComparator):
    _a_float: float = -1.1
    _a_int: int = -1
    _a_title: str = 'Portfolio: '
    _stocks: list
    _weights: list
    _legend_place: str = 'upper left'
    _data: DataFrame = DataFrame()
    _dataNorm: DataFrame = DataFrame()
    _dataScaled: DataFrame = DataFrame()
    _dataBin: DataFrame = DataFrame()
    _dataReturns: DataFrame = DataFrame()
    _dataSimpleReturns: DataFrame = DataFrame()
    _dataSimpleVolatility: DataFrame = DataFrame()
    _dataSimpleDaily: DataFrame = DataFrame()
    _dataSimpleCorrelation: DataFrame = DataFrame()
    _dataSimpleReturnsCumulative: DataFrame = DataFrame()
    _arrayNorm: ndarray
    _arrayScaled: ndarray
    _arrayBin: ndarray

    def __init__(self, y_stocks: list):
        self._a_float = 3 * math.log(y_stocks[0].TimeSpan.MonthCount)
        self._a_int = len(y_stocks)
        iso_weight: float = 1.0 / len(y_stocks)
        self._stocks = y_stocks
        self._weights = iso_weight * 4
        self._setAllData(y_stocks)
        print('DF:', self._data.head())
        print('DN:', self._dataNorm.head())
        print('DS:', self._dataScaled.head())
        print('DB:', self._dataBin.head())
        #plt.figure(figsize=(3 * math.log(y_stocks[0].TimeSpan.MonthCount), 4.5))
        #plt.tight_layout()
        #plt.plot(self._data)
        #plt.title('~title~')
        #plt.xlabel(y_stocks[0].TimeSpan.StartDateStr + ' - ' + y_stocks[0].TimeSpan.EndDateStr)
        #plt.ylabel(y_stocks[0].SourceColumn + ' in USD')
        #plt.legend(loc='upper left', labels=self._data.columns)
        #plt.show()
        self._setReturns()
        print('SR', self._dataReturns.head())

    def _setAllData(self, y_stocks):
        for y_stock in y_stocks:
            print('stock EPS:', y_stock.FvEPS)
            self._a_title += y_stock.Ticker + ' '
            self._data[y_stock.Ticker + y_stock.SourceColumn] = y_stock.HistoricalData[y_stock.SourceColumn]
        self._arrayNorm = preprocessing.normalize(self._data, norm='l1')
        self._dataNorm = DataFrame(self._arrayNorm, columns=self._data.columns, index=self._data.index)
        self._arrayScaled = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(self._data)
        self._dataScaled = DataFrame(self._arrayScaled, columns=self._data.columns, index=self._data.index)
        self._arrayBin = preprocessing.Binarizer(threshold=1.4).transform(self._data)
        self._dataBin = DataFrame(self._arrayBin, columns=self._data.columns, index=self._data.index)
        self._dataSimpleReturns = self._data.pct_change(1)
        self._dataSimpleVolatility = self._dataSimpleReturns.std().to_frame()
        self._dataSimpleDaily = self._dataSimpleReturns.mean().to_frame()
        self._dataSimpleCorrelation = self._dataSimpleReturns.corr()
        print(self._dataSimpleCorrelation)
        self._dataSimpleReturnsCumulative = (self._dataSimpleReturns + 1).cumprod()

    def _setReturns(self):
        self._dataReturns = (self._data / self._data.iloc[0]).fillna(method='backfill')
        self._dataReturns['PORTFOLIO'] = self._dataReturns.iloc[:, 0:self._a_int].sum(axis=1) / self._a_int
        daily_pct_change = np.log(self._dataReturns.pct_change() + 1)
        vols = daily_pct_change.std() * np.sqrt(252)
        print('vols', vols)

    def PlotAllData(self):
        plt.style.use('seaborn')
        fig, ax = plt.subplots(4, 1, figsize=(self._a_float, self._a_float/2.0), sharex=True)
        fig.suptitle(self._a_title)
        self._data.plot(ax=ax[0], label=self._data.columns)
        ax[0].set(ylabel='Price $USD')
        ax[0].legend(loc=self._legend_place)
        self._dataNorm.plot(ax=ax[1], label=self._dataNorm.columns)
        ax[1].set(ylabel='Norm L1 base t(0)')
        ax[1].legend(loc=self._legend_place)
        self._dataScaled.plot(ax=ax[2], label=self._dataScaled.columns)
        ax[2].set(ylabel='Scaled values [0 - 1]')
        ax[2].legend(loc=self._legend_place)
        self._dataBin.plot(ax=ax[3], label=self._dataBin.columns)
        ax[3].set(ylabel='Binary [-1,0,+1]')
        ax[3].legend(loc=self._legend_place)
        plt.tight_layout()
        return plt

    def PlotAllSimple(self):
        plt.style.use('seaborn')
        fig, ax = plt.subplots(3, 1, figsize=(self._a_float, self._a_float/1.5), sharex=True)
        fig.suptitle(self._a_title)
        self._dataReturns.plot(ax=ax[0], label=self._dataReturns.columns)
        ax[0].set(ylabel='Returns')
        ax[0].legend(loc=self._legend_place)
        self._dataSimpleReturns.plot(ax=ax[1], label=self._dataSimpleReturns.columns)
        ax[1].set(ylabel='Simple Return - Volatility')
        ax[1].legend(loc=self._legend_place)
        self._dataSimpleReturnsCumulative.plot(ax=ax[2], label=self._dataSimpleReturnsCumulative.columns)
        ax[2].set(ylabel='Simple Return - Cumulative')
        ax[2].legend(loc=self._legend_place)
        plt.tight_layout()
        return plt

    def PlotAllHeatmaps(self):
        prf_returns = (self._dataReturns.pct_change() + 1)[1:]
        avg_return = (prf_returns-1).mean()
        daily_pct_change = np.log(self._dataReturns.pct_change() + 1)
        vols = daily_pct_change.std() * np.sqrt(252)
        plt.style.use('seaborn')
        fig, ax = plt.subplots(1, 1, figsize=(self._a_float, self._a_float/2.0))
        #print('AX', type(ax)) AX <class 'matplotlib.axes._subplots.AxesSubplot'>
        fig.suptitle(self._a_title)
        ax.set(ylabel='Simple Return Std', xlabel='Simple Return Mean')
        ax.scatter(vols, avg_return)
        for i, txt in enumerate(list(vols.index)):
            ax.annotate(txt, (vols[i], avg_return[i]))
        plt.tight_layout()
        plt.show()
        #cm = sns.clustermap(self._dataSimpleCorrelation, cmap="coolwarm", annot=True, row_cluster=True, col_cluster=True)
        #print('CM', cm) CM <seaborn.matrix.ClusterGrid object at 0x000001B927DDD520>
        plt.tight_layout()
        return plt
