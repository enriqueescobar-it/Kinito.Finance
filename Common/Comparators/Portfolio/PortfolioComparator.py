import math
from sklearn import preprocessing
from Common.Comparators.Portfolio.AbstractPortfolioComparator import AbstractPortfolioComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from pandas import DataFrame, np, Series
from numpy import ndarray
import seaborn as sns
import matplotlib.pyplot as plt
from heatmapcluster import heatmapcluster


class PortfolioComparator(AbstractPortfolioComparator):
    _a_float: float = -1.1
    _a_suffix: str = ''
    _a_length: int = -1
    _a_title: str = 'Portfolio: '
    _stocks: list
    _weights: ndarray
    _legend_place: str = 'upper left'
    _data: DataFrame = DataFrame()
    _dataWeightedReturns: DataFrame = DataFrame()
    _dataNorm: DataFrame = DataFrame()
    _dataNormL1: DataFrame = DataFrame()
    _dataScaled: DataFrame = DataFrame()
    _dataSparsed: DataFrame = DataFrame()
    _dataBin: DataFrame = DataFrame()
    _dataReturns: DataFrame = DataFrame()
    _dataSimple: DataFrame = DataFrame()
    _dataSimpleReturns: DataFrame = DataFrame()
    _dataSimpleReturnsCumulative: DataFrame = DataFrame()
    _dataSimpleCorrelation: DataFrame = DataFrame()
    _dataSimpleCovariance: DataFrame = DataFrame()
    _dataSimpleCovarianceAnnual: DataFrame = DataFrame()
    _portfolio_weighted_returns_cum: Series = Series()
    _portfolio_weighted_returns_geom: float = -1.1
    _portfolio_weighted_annual_std: float = -1.1
    _portfolio_weighted_sharpe_ratio: float = -1.1

    def __init__(self, y_stocks: list):
        self._a_float = 3 * math.log(y_stocks[0].TimeSpan.MonthCount)
        self._a_suffix = y_stocks[0].SourceColumn
        self._a_length = len(y_stocks)
        iso_weight: float = round(1.0 / len(y_stocks), 3)
        self._stocks = y_stocks
        self._weights = np.array(len(y_stocks) * [iso_weight], dtype=float)
        self._setBasicData(y_stocks)
        self._setSimpleData()
        self._setWeightedData()
        self._setPortfolioInfo()
        print('SR', self._dataReturns.head())

    def _setBasicData(self, y_stocks):
        for y_stock in y_stocks:
            print('stock EPS:', y_stock.Ticker + str(y_stock.FvEPS))
            self._a_title += y_stock.Ticker + ' '
            self._data[y_stock.Ticker + y_stock.SourceColumn] = y_stock.Data[y_stock.SourceColumn]
            self._dataBin[y_stock.Ticker + 'Binary'] = y_stock.Data['Binary']
            self._dataNorm[y_stock.Ticker + 'Norm'] = y_stock.Data['Norm']
            #self._dataNormL1[y_stock.Ticker + 'NormL1'] = y_stock.Data['NormL1']
            self._dataSparsed[y_stock.Ticker + 'Sparse'] = y_stock.Data['Sparse']
            #self._dataScaled[y_stock.Ticker + 'Scaled'] = y_stock.Data['Scaled']
        arrayNormL1 = preprocessing.normalize(self._data, norm='l1')
        self._dataNormL1 = DataFrame(arrayNormL1, columns=self._data.columns, index=self._data.index)
        arrayScaled = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(self._data)
        self._dataScaled = DataFrame(arrayScaled, columns=self._data.columns, index=self._data.index)
        self._dataSparsed = DataFrame(preprocessing.scale(self._data), columns=self._data.columns, index=self._data.index)
        self._dataReturns = (self._data / self._data.iloc[0]).fillna(method='backfill')
        self._dataReturns.fillna(method='ffill', inplace=True)

    def _setSimpleData(self):
        # == (self._data / self._data.shift(1))-1
        self._dataSimpleReturns = self._data.pct_change(1)
        print(self._dataSimpleReturns.head())
        self._dataSimpleReturnsCumulative = (self._dataSimpleReturns + 1).cumprod()
        print(self._dataSimpleReturnsCumulative.head())
        self._dataSimple['Volatility'] = self._dataSimpleReturns.std()
        self._dataSimple['Daily'] = self._dataSimpleReturns.mean()
        self._dataSimple['Variance'] = self._dataSimpleReturns.var()
        print(self._dataSimple)
        self._dataSimpleCorrelation = self._dataSimpleReturns.corr()
        print(self._dataSimpleCorrelation)
        self._dataSimpleCovariance = self._dataSimpleReturns.cov()
        print(self._dataSimpleCovariance)
        self._dataSimpleCovarianceAnnual = self._dataSimpleCovariance * 252
        print(self._dataSimpleCovarianceAnnual)

    def _setWeightedData(self):
        for ind, column in enumerate(self._dataSimpleReturns.columns):
            print('weight', ind)
            a_col: str = column.replace(self._a_suffix, '')
            self._dataWeightedReturns[a_col] = round(self._weights[ind] * self._dataSimpleReturns[column], 5)
        self._dataWeightedReturns.fillna(method='ffill', inplace=True)
        self._dataWeightedReturns.fillna(method='bfill', inplace=True)
        # axis =1 tells pandas we want to add the rows
        portfolio_weighted_returns: Series = round(self._dataWeightedReturns.sum(axis=1), 5)
        self._dataWeightedReturns['PORTFOLIO'] = portfolio_weighted_returns
        portfolio_weighted_returns_mean = round(portfolio_weighted_returns.mean(), 5)
        print('port_ret mean', portfolio_weighted_returns_mean)
        portfolio_weighted_returns_std = round(portfolio_weighted_returns.std(), 5)
        print('port_ret std', portfolio_weighted_returns_std)
        self._portfolio_weighted_returns_cum: Series = round((portfolio_weighted_returns + 1).cumprod(), 5)
        self._dataWeightedReturns['PORTFOLIOCumulative'] = self._portfolio_weighted_returns_cum
        print(self._dataWeightedReturns.head())
        self._portfolio_weighted_returns_geom = round(np.prod(portfolio_weighted_returns + 1) ** (252 / portfolio_weighted_returns.shape[0]) - 1, 5)
        print('geometric_port_return', self._portfolio_weighted_returns_geom)
        self._portfolio_weighted_annual_std = round(np.std(portfolio_weighted_returns) * np.sqrt(252), 5)
        print('port_ret annual', self._portfolio_weighted_annual_std)
        self._portfolio_weighted_sharpe_ratio = round(self._portfolio_weighted_returns_geom / self._portfolio_weighted_annual_std, 5)
        print('port_sharpe_ratio', self._portfolio_weighted_sharpe_ratio)

    def _setPortfolioInfo(self):
        print('_dataReturns', self._dataReturns)
        self._dataReturns['PORTFOLIO'] = self._dataReturns.iloc[:, 0:self._a_length].sum(axis=1) / self._a_length
        print('_dataReturns', self._dataReturns)
        exit(999)
        daily_pct_change = np.log(self._dataReturns.pct_change() + 1)
        vols = daily_pct_change.std() * np.sqrt(252)
        print('vols', vols)
        port_daily_simple_ret: float = np.sum(self._dataSimpleReturns.mean()*self._weights)
        port_daily_simple_ret = round(port_daily_simple_ret, 5)
        port_monthly_simple_ret: float = round(21 * port_daily_simple_ret, 5)
        port_yearly_simple_ret: float = round(252 * port_daily_simple_ret, 5)
        print('port_daily_simple_ret', str(100*port_daily_simple_ret) + '%')
        print('port_monthly_simple_ret', str(100*port_monthly_simple_ret) + '%')
        print('port_yearly_simple_ret', str(100*port_yearly_simple_ret) + '%')
        port_annual_var: float = np.dot(self._weights.T, np.dot(self._dataSimpleCovarianceAnnual, self._weights))
        port_annual_volatility: float = np.sqrt(port_annual_var)
        port_annual_simple_ret: float = np.sum(self._dataSimpleReturns.mean() * self._weights) * 252
        print('Port Ann Ret', str(round(port_annual_var, 5)*100)+'%')
        print('Port Ann Volatility/ Risk', str(round(port_annual_volatility, 5)*100)+'%')
        print('Port Ann Variance', str(round(port_annual_simple_ret, 5)*100)+'%')
        '''
        # Calculate the portfolio standard deviation
        portfolio_volatility = np.sqrt(np.dot(portfolio_weights.T, np.dot(cov_mat_annual, portfolio_weights)))
        print(portfolio_volatility)
        # Calculate the weighted stock returns
        - norm base[0] * weights -> WeigtedData -> sum by row then *.sum(axis=1 to port value)
        WeightedReturns = StockReturns.mul(portfolio_weights, axis=1)
        port_values = port_values[1:]
        - cum ret
        - avg daily ret
        - std daily ret
        - sharpe ratio
        # Calculate the portfolio returns
        StockReturns['Portfolio'] = WeightedReturns.sum(axis=1)
        # Plot the cumulative portfolio returns over time
        CumulativeReturns = ((1+StockReturns["Portfolio"]).cumprod()-1)
        CumulativeReturns.plot()
        plt.show()
        '''

    def PlotAllData(self):
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31'
        fig, ax = plt.subplots(5, 1, figsize=(self._a_float, self._a_float/2.0), sharex=True)
        fig.suptitle(self._a_title)
        self._data.plot(ax=ax[0], label=self._data.columns)
        ax[0].set(ylabel='Price $USD')
        ax[0].legend(loc=self._legend_place)
        self._dataNorm.plot(ax=ax[1], label=self._dataNorm.columns)
        ax[1].set(ylabel='Norm base t(0)')
        ax[1].legend(loc=self._legend_place)
        self._dataNormL1.plot(ax=ax[2], label=self._dataNormL1.columns)
        ax[2].set(ylabel='Norm L1 base t(0)')
        ax[2].legend(loc=self._legend_place)
        self._dataScaled.plot(ax=ax[3], label=self._dataScaled.columns)
        ax[3].set(ylabel='Scaled values [0 - 1]')
        ax[3].legend(loc=self._legend_place)
        self._dataSparsed.plot(ax=ax[4], label=self._dataSparsed.columns)
        ax[4].set(ylabel='Sparsed values')
        ax[4].legend(loc=self._legend_place)
        plt.tight_layout()
        return plt

    def PlotAllSimple(self):
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31'
        fig, ax = plt.subplots(3, 1, figsize=(self._a_float, self._a_float/1.5), sharex=True)
        fig.suptitle(self._a_title)
        self._dataSimpleReturnsCumulative.plot(ax=ax[0], label=self._dataSimpleReturnsCumulative.columns)
        ax[0].set(ylabel='Simple Return - Cumulative')
        ax[0].legend(loc=self._legend_place)
        self._dataSimpleReturns.plot(ax=ax[1], label=self._dataSimpleReturns.columns)
        ax[1].set(ylabel='Simple Return - Volatility')
        ax[1].legend(loc=self._legend_place)
        self._dataReturns.plot(ax=ax[2], label=self._dataReturns.columns)
        ax[2].set(ylabel='Returns')
        ax[2].legend(loc=self._legend_place)
        plt.tight_layout()
        return plt

    def PlotAllHeatmaps(self):
        prf_returns = (self._dataReturns.pct_change() + 1)[1:]
        avg_return = (prf_returns-1).mean()
        daily_pct_change = np.log(self._dataReturns.pct_change() + 1)
        vols = daily_pct_change.std() * np.sqrt(252)
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31'
        fig, ax = plt.subplots(1, 1, figsize=(self._a_float, self._a_float/2.0))
        #print('AX', type(ax)) AX <class 'matplotlib.axes._subplots.AxesSubplot'>
        fig.suptitle(self._a_title)
        ax.set(ylabel='Simple Return Std', xlabel='Simple Return Mean')
        ax.scatter(vols, avg_return)
        for i, txt in enumerate(list(vols.index)):
            ax.annotate(txt, (vols[i], avg_return[i]))
        plt.tight_layout()
        plt.show()
        sns.clustermap(self._dataSimpleCorrelation, cmap="coolwarm", annot=True, row_cluster=True, col_cluster=True, fmt='.2%')
        #cm = sns.clustermap(self._dataSimpleCorrelation, cmap="coolwarm", annot=True, row_cluster=True, col_cluster=True)
        #print('CM', cm) CM <seaborn.matrix.ClusterGrid object at 0x000001B927DDD520>
        plt.tight_layout()
        plt.show()
        sns.clustermap(self._dataSimpleCovarianceAnnual, cmap="coolwarm", annot=True, row_cluster=True, col_cluster=True, fmt='.2%')
        plt.tight_layout()
        return plt

    @property
    def data(self):
        return self._data
