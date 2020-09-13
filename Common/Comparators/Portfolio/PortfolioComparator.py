import math
from sklearn import preprocessing
from Common.Comparators.Portfolio.AbstractPortfolioComparator import AbstractPortfolioComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from pandas import DataFrame, np
import matplotlib.pyplot as plt


class PortfolioComparator(AbstractPortfolioComparator):
    _stocks: list
    _weights: list
    _data: DataFrame = DataFrame()
    _dataNorm: DataFrame = DataFrame()
    _dataScaled: DataFrame = DataFrame()
    _dataBin: DataFrame = DataFrame()
    _returns: DataFrame = DataFrame()

    def __init__(self, y_stocks: list):
        iso_weight: float = 1.0 / len(y_stocks)
        self._stocks = y_stocks
        self._weights = iso_weight * 4
        for y_stock in y_stocks:
            print('stock EPS:', y_stock.FvEPS)
            self._data[y_stock.Ticker + y_stock.SourceColumn] = y_stock.HistoricalData[y_stock.SourceColumn]

        self._dataNorm = preprocessing.normalize(self._data, norm='l1')
        self._dataScaled = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(self._data)
        self._dataBin = preprocessing.Binarizer(threshold=1.4).transform(self._data)
        print('DF:', self._data.head())
        #plt.figure(figsize=(3 * math.log(y_stocks[0].TimeSpan.MonthCount), 4.5))
        #plt.tight_layout()
        #plt.plot(self._data)
        #plt.title('~title~')
        #plt.xlabel(y_stocks[0].TimeSpan.StartDateStr + ' - ' + y_stocks[0].TimeSpan.EndDateStr)
        #plt.ylabel(y_stocks[0].SourceColumn + ' in USD')
        #plt.legend(loc='upper left', labels=self._data.columns)
        #plt.show()
        self._setReturns(len(y_stocks), y_stock.SourceColumn, y_stocks[0].TimeSpan.MonthCount)

    def _setReturns(self, length: int = 0, column: str = 'Adj Close', n_months: int = 0):
        self._returns = (self._data / self._data.iloc[0]).fillna(method='backfill')
        self._returns['PORTFOLIO'] = self._returns.iloc[:, 0:length].sum(axis=1) / length
        #self._returns.columns = [x.replace(column, '') for x in self._returns.columns]
        print('RT', self._returns.head())
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
