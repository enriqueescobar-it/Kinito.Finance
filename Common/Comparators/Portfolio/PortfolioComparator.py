import math

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import ndarray
from pandas import DataFrame, np, Series

from Common.Comparators.Portfolio.AbstractPortfolioComparator import AbstractPortfolioComparator
from Common.Measures.Portfolio.PortfolioBasics import PortfolioBasics
from Common.Measures.Portfolio.PortfolioLinearReg import PortfolioLinearReg
from Common.Measures.Portfolio.PortfolioOptimizer import PortfolioOptimizer
from Common.Measures.Portfolio.PortfolioStats import PortfolioStats
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index


class PortfolioComparator(AbstractPortfolioComparator):
    _a_ts: TimeSpan
    _alpha: float = -1.1
    _beta: float = -1.1
    _a_float: float = -1.1
    _a_suffix: str = ''
    _a_length: int = -1
    _stocks: list
    _weights: ndarray
    _legend_place: str = 'upper left'
    _dataWeightedReturns: DataFrame = DataFrame()
    _dataReturns: DataFrame = DataFrame()
    _dataSimple: DataFrame = DataFrame()
    _dataSimpleReturns: DataFrame = DataFrame()
    _dataSimpleReturnsCumulative: DataFrame = DataFrame()
    _dataSimpleCorrelation: DataFrame = DataFrame()
    _dataSimpleCovariance: DataFrame = DataFrame()
    _dataSimpleCovarianceAnnual: DataFrame = DataFrame()
    _dataLogReturns: DataFrame = DataFrame()
    _portfolio_weighted_returns: Series = Series()
    _portfolio_weighted_returns_cum: Series = Series()
    _portfolio_weighted_returns_geom: float = -1.1
    _portfolio_weighted_annual_std: float = -1.1
    _portfolio_weighted_sharpe_ratio: float = -1.1
    _stock_market_index: AbstractStockMarketIndex
    _basics: PortfolioBasics
    _linear_reg: PortfolioLinearReg
    _stats: PortfolioStats
    _optimizer: PortfolioOptimizer

    def __init__(self, y_stocks: list):
        self._a_float = 3 * math.log(y_stocks[0].TimeSpan.MonthCount)
        self._a_suffix = y_stocks[0].SourceColumn
        self._a_ts = y_stocks[0].TimeSpan
        self._a_length = len(y_stocks)
        iso_weight: float = round(1.0 / len(y_stocks), 3)
        self._stocks = y_stocks
        self._weights = np.array(len(y_stocks) * [iso_weight], dtype=float)
        self._basics = PortfolioBasics(y_stocks)
        self._stats = PortfolioStats(self._weights, self._a_suffix, self._basics.Data)
        self._dataReturns = self._getDataReturns(self._basics.Data)
        self._dataSimpleReturns = self._getDataSimpleReturns(self._basics.Data)
        print('?', self._dataSimpleReturns.head())
        self._dataSimpleCorrelation = self._dataSimpleReturns.corr()
        #print(self._dataSimpleCorrelation)
        self._dataSimpleCovariance = self._dataSimpleReturns.cov()
        #print(self._dataSimpleCovariance)
        self._dataSimpleCovarianceAnnual = self._dataSimpleCovariance * 252
        #print(self._dataSimpleCovarianceAnnual)
        self._dataSimpleReturnsCumulative = self._getDataSimpleReturnsCumulative(self._dataSimpleReturns)
        print('~', self._dataSimpleReturnsCumulative.head())
        self._dataSimple = self._getDataSimple(self._dataSimpleReturns)
        self._dataWeightedReturns = self._getDataWeighted(self._dataSimpleReturns)
        print('#', self._dataWeightedReturns.head())
        # axis =1 tells pandas we want to add the rows
        self._portfolio_weighted_returns = round(self._dataWeightedReturns.sum(axis=1), 5)
        #self._dataWeightedReturns['PORTFOLIOWeighted'] = portfolio_weighted_returns
        portfolio_weighted_returns_mean = round(self._portfolio_weighted_returns.mean(), 5)
        print('port_ret mean', portfolio_weighted_returns_mean)
        portfolio_weighted_returns_std = round(self._portfolio_weighted_returns.std(), 5)
        print('port_ret std', portfolio_weighted_returns_std)
        self._portfolio_weighted_returns_cum: Series = round((self._portfolio_weighted_returns + 1).cumprod(), 5)
        #self._dataWeightedReturns['PORTFOLIOCumulative'] = self._portfolio_weighted_returns_cum
        print('$', self._dataWeightedReturns.head())
        self._portfolio_weighted_returns_geom = round(np.prod(self._portfolio_weighted_returns + 1) ** (252 / self._portfolio_weighted_returns.shape[0]) - 1, 5)
        print('geometric_port_return', self._portfolio_weighted_returns_geom)
        self._portfolio_weighted_annual_std = round(np.std(self._portfolio_weighted_returns) * np.sqrt(252), 5)
        print('port_ret annual', self._portfolio_weighted_annual_std)
        self._portfolio_weighted_sharpe_ratio = round(self._portfolio_weighted_returns_geom / self._portfolio_weighted_annual_std, 5)
        print('port_sharpe_ratio', self._portfolio_weighted_sharpe_ratio)
        print('%', self._dataReturns.head())
        dataReturns_avg: Series = self._getDataReturnsAverage(self._dataReturns)
        print('^', dataReturns_avg.head())
        daily_log_pct_changes: DataFrame = np.log(self._dataReturns.pct_change() + 1) #avant portfolio
        daily_log_pct_changes.columns = daily_log_pct_changes.columns + 'LogReturn'
        print('&', daily_log_pct_changes.head())
        daily_log_volatilities: DataFrame = (daily_log_pct_changes.std() * np.sqrt(252)).to_frame()
        daily_log_volatilities.columns = ['Volatility']
        print('*', daily_log_volatilities)
        port_daily_simple_ret: float = round(np.sum(self._dataSimpleReturns.mean()*self._weights), 5)
        port_weekly_simple_ret: float = round(4.856 * port_daily_simple_ret, 5)
        port_monthly_simple_ret: float = round(21 * port_daily_simple_ret, 5)
        port_quarterly_simple_ret: float = round(63 * port_daily_simple_ret, 5)
        port_yearly_simple_ret: float = round(252 * port_daily_simple_ret, 5)
        print('port_daily_simple_ret', str(100*port_daily_simple_ret) + '%')
        print('port_weekly_simple_ret', str(100*port_weekly_simple_ret) + '%')
        print('port_monthly_simple_ret', str(100*port_monthly_simple_ret) + '%')
        print('port_quarterly_simple_ret', str(100*port_quarterly_simple_ret) + '%')
        print('port_yearly_simple_ret', str(100*port_yearly_simple_ret) + '%')
        self._setPortfolioInfo()
        self._optimizer = PortfolioOptimizer(self._stats, self._basics.Data)
        self._stock_market_index = SnP500Index('yahoo', "^GSPC", self._a_ts)
        stock_market_returns: Series = self._stock_market_index.HistoricalData.iloc[:, 0].pct_change()+1#[1:]
        stock_market_returns[np.isnan(stock_market_returns)] = 1
        sns.regplot(stock_market_returns.values, dataReturns_avg.values)
        plt.xlabel('Benchmark Returns')
        plt.ylabel('Portfolio Returns')
        plt.title('Portfolio Returns vs Benchmark Returns')
        plt.show()
        self._linear_reg = PortfolioLinearReg(self._stock_market_index, self._dataReturns)
        print(f'The portfolio beta is {self._linear_reg.Beta}, for each 1% of index portfolio will move {self._linear_reg.Beta}%')
        print('The portfolio alpha is ', self._linear_reg.Alpha)
        self._dataLogReturns = self._getLogReturns(self._basics.Data)
        print('_', self._dataLogReturns.head())
        cov_mat_annual = self._dataLogReturns.cov() * 252
        print('-', cov_mat_annual)

    def _getDataReturns(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame = (a_df / a_df.iloc[0]).fillna(method='backfill')
        new_df.fillna(method='ffill', inplace=True)
        new_df.columns = new_df.columns.str.replace(self._a_suffix, '')
        return new_df

    def _getDataSimpleReturns(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        # == (self._data / self._data.shift(1))-1
        new_df: DataFrame = a_df.pct_change(1)
        new_df.columns = new_df.columns.str.replace(self._a_suffix, 'SimpleReturns')
        return new_df

    def _getDataSimpleReturnsCumulative(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame = (a_df + 1).cumprod()
        new_df.columns = new_df.columns.str.replace('Returns', 'Cumulative')
        return new_df

    def _getDataSimple(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame = DataFrame()
        new_df['Volatility'] = a_df.std()
        new_df['Daily'] = a_df.mean()
        new_df['Variance'] = a_df.var()
        return new_df

    def _getDataWeighted(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame = DataFrame()
        for ind, column in enumerate(a_df.columns):
            print('ind|col', str(ind) + '|' + column)
            a_col: str = column.replace('Simple', 'Weighted')
            new_df[a_col] = round(self._weights[ind] * a_df[column], 5)
        new_df.fillna(method='ffill', inplace=True)
        new_df.fillna(method='bfill', inplace=True)
        return new_df

    def _getDataReturnsAverage(self, a_df: DataFrame = DataFrame()) -> Series:
        return a_df.iloc[:, 0:self._a_length].sum(axis=1) / self._a_length

    def _setPortfolioInfo(self):
        port_annual_var: float = round(np.dot(self._weights.T, np.dot(self._dataSimpleCovarianceAnnual, self._weights)), 5)
        port_annual_volatility: float = round(np.sqrt(port_annual_var), 5)
        port_annual_simple_ret: float = round(np.sum(self._dataSimpleReturns.mean() * self._weights) * 252, 5)
        print('Port Ann Ret', str(round(port_annual_var, 5)*100)+'%')
        print('Port Ann Volatility/ Risk', str(round(port_annual_volatility, 5)*100)+'%')
        print('Port Ann Variance', str(round(port_annual_simple_ret, 5)*100)+'%')
        '''
        # Calculate the portfolio standard deviation
        portfolio_volatility = np.sqrt(np.dot(portfolio_weights.T, np.dot(cov_mat_annual, portfolio_weights)))
        print(portfolio_volatility)
        # Calculate the weighted stock returns
        - norm base[0] * weights -> WeightedData -> sum by row then *.sum(axis=1 to port value)
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

    def _getLogReturns(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame = np.log(a_df/a_df.shift(1))
        new_df.columns = new_df.columns.str.replace(self._a_suffix, 'LogReturn')
        return new_df

    def PlotAllData(self):
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31'
        fig, ax = plt.subplots(5, 1, figsize=(self._a_float, self._a_float/2.0), sharex=True)
        fig.suptitle(self._basics.Title)
        self._basics.Data.plot(ax=ax[0], label=self._basics.Data.columns)
        ax[0].set(ylabel='Price $USD')
        ax[0].legend(loc=self._legend_place, fontsize=8)
        self._basics.DataNorm.plot(ax=ax[1], label=self._basics.DataNorm.columns)
        ax[1].set(ylabel='Norm base t(0)')
        ax[1].legend(loc=self._legend_place, fontsize=8)
        self._basics.DataNormL1.plot(ax=ax[2], label=self._basics.DataNormL1.columns)
        ax[2].set(ylabel='Norm L1 base t(0)')
        ax[2].legend(loc=self._legend_place, fontsize=8)
        self._basics.DataScaled.plot(ax=ax[3], label=self._basics.DataScaled.columns)
        ax[3].set(ylabel='Scaled values [0 - 1]')
        ax[3].legend(loc=self._legend_place, fontsize=8)
        self._basics.DataSparse.plot(ax=ax[4], label=self._basics.DataSparse.columns)
        ax[4].set(ylabel='Sparsed values')
        ax[4].legend(loc=self._legend_place, fontsize=8)
        plt.tight_layout()
        return plt

    def PlotAllSimple(self):
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31'
        fig, ax = plt.subplots(3, 1, figsize=(self._a_float, self._a_float/1.5), sharex=True)
        fig.suptitle(self._basics.Title)
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
        fig.suptitle(self._basics.Title)
        ax.set(ylabel='Simple Return Std', xlabel='Simple Return Mean')
        ax.scatter(vols, avg_return)
        for i, txt in enumerate(list(vols.index)):
            ax.annotate(txt, (vols[i], avg_return[i]))
        plt.tight_layout()
        plt.show()
        fig, ax = plt.subplots(1, 1, figsize=(self._a_float, self._a_float/2.0))
        fig.suptitle('Main Heat Map')
        plt.title('Heat Map', fontsize=18)
        ax.title.set_position([0.5, 1.05])
        ax.set_xticks([])
        sns.heatmap(self._dataSimpleCorrelation, cmap='coolwarm', annot=True, fmt='.2%', ax=ax)
        #sns.clustermap(self._dataSimpleCorrelation, cmap='coolwarm', annot=True, row_cluster=False, col_cluster=True, fmt='.2%')
        ##cm = sns.clustermap(self._dataSimpleCorrelation, cmap="coolwarm", annot=True, row_cluster=True, col_cluster=True)
        ##print('CM', cm) CM <seaborn.matrix.ClusterGrid object at 0x000001B927DDD520>
        plt.tight_layout()
        plt.show()
        fig, ax = plt.subplots(1, 1, figsize=(self._a_float, self._a_float/2.0))
        fig.suptitle('Main Heat Map')
        plt.title('Heat Map', fontsize=18)
        ax.title.set_position([0.5, 1.05])
        ax.set_xticks([])
        sns.heatmap(self._dataSimpleCovarianceAnnual, cmap="coolwarm", annot=True, fmt='.2%', ax=ax)
        #sns.clustermap(self._dataSimpleCovarianceAnnual, cmap="coolwarm", annot=True, row_cluster=False, col_cluster=True, fmt='.2%')
        plt.tight_layout()
        return plt

    @property
    def Data(self):
        return self._basics.Data
