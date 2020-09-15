import math
from sklearn import preprocessing
from Common.Comparators.Portfolio.AbstractPortfolioComparator import AbstractPortfolioComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from pandas import DataFrame, np
from numpy import ndarray
import matplotlib.pyplot as plt


class PortfolioComparator(AbstractPortfolioComparator):
    _a_float: float
    _stocks: list
    _weights: list
    _legend_place: str = 'upper left'
    _data: DataFrame = DataFrame()
    _dataNorm: DataFrame = DataFrame()
    _dataScaled: DataFrame = DataFrame()
    _dataBin: DataFrame = DataFrame()
    _returns: DataFrame = DataFrame()
    _arrayNorm: ndarray
    _arrayScaled: ndarray
    _arrayBin: ndarray

    def __init__(self, y_stocks: list):
        self._a_float = 3 * math.log(y_stocks[0].TimeSpan.MonthCount)
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
        self._setReturns(len(y_stocks), y_stocks[0].SourceColumn, y_stocks[0].TimeSpan.MonthCount)
        print('SR', self._returns.head())

    def _setAllData(self, y_stocks):
        for y_stock in y_stocks:
            print('stock EPS:', y_stock.FvEPS)
            self._data[y_stock.Ticker + y_stock.SourceColumn] = y_stock.HistoricalData[y_stock.SourceColumn]
        self._arrayNorm = preprocessing.normalize(self._data, norm='l1')
        self._dataNorm = DataFrame(self._arrayNorm, columns=self._data.columns, index=self._data.index)
        self._arrayScaled = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(self._data)
        self._dataScaled = DataFrame(self._arrayScaled, columns=self._data.columns, index=self._data.index)
        self._arrayBin = preprocessing.Binarizer(threshold=1.4).transform(self._data)
        self._dataBin = DataFrame(self._arrayBin, columns=self._data.columns, index=self._data.index)

    def _setReturns(self, length: int = 0, column: str = 'Adj Close', n_months: int = 0):
        self._returns = (self._data / self._data.iloc[0]).fillna(method='backfill')
        self._returns['PORTFOLIO'] = self._returns.iloc[:, 0:length].sum(axis=1) / length
        #self._returns.columns = [x.replace(column, '') for x in self._returns.columns]
        #plt.figure(figsize=(3 * math.log(n_months), 4.5))
        #plt.tight_layout()
        #plt.plot(self._returns)
        #plt.title('~title~')
        #plt.xlabel(y_stocks[0].TimeSpan.StartDateStr + ' - ' + y_stocks[0].TimeSpan.EndDateStr)
        #plt.ylabel(y_stocks[0].SourceColumn + ' in USD')
        #plt.legend(loc='upper left', labels=self._returns.columns)
        #plt.show()
        daily_pct_change = np.log(self._returns.pct_change() + 1)
        vols = daily_pct_change.std() * np.sqrt(252)
        print('vols', vols)

    def PlotAllData(self):
        fig, ax = plt.subplots(4, 1, figsize=(self._a_float, self._a_float), sharex=True)
        self._data.plot(ax=ax[0], label=self._data.columns)
        ax[0].legend(loc=self._legend_place)
        self._dataNorm.plot(ax=ax[1], label=self._dataNorm.columns)
        ax[1].legend(loc=self._legend_place)
        self._dataScaled.plot(ax=ax[2], label=self._dataScaled.columns)
        ax[2].legend(loc=self._legend_place)
        self._dataBin.plot(ax=ax[3], label=self._dataBin.columns)
        ax[3].legend(loc=self._legend_place)
        plt.style.use('fivethirtyeight')
        plt.tight_layout()
        return plt
