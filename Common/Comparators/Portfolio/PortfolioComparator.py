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
    _dataSimpleSummary: DataFrame = DataFrame()
    _dataSimpleCorrelation: DataFrame = DataFrame()
    _dataSimpleCovariance: DataFrame = DataFrame()
    _dataSimpleCovarianceAnnual: DataFrame = DataFrame()
    _data_returns_avg: Series = Series()
    #_portfolio_weighted_returns: Series = Series()
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
        self._basics = PortfolioBasics(y_stocks, self._a_float, self._legend_place)
        self._stats = PortfolioStats(self._weights, self._basics)
        self._dataSimpleCorrelation = self._stats.SimpleReturnsNan.corr()
        self._dataSimpleCovariance = self._stats.SimpleReturnsNan.cov()
        self._dataSimpleCovarianceAnnual = self._dataSimpleCovariance * 252
        self._dataSimpleSummary = self._stats.SimpleReturnsNanSummary
        self._dataWeightedReturns = self._stats.SimpleWeightedReturns
        # axis =1 tells pandas we want to add the rows
        self._portfolio_weighted_returns = round(self._dataWeightedReturns.sum(axis=1), 5)
        print('7', self._portfolio_weighted_returns.head())
        print('7', self._stats.SimpleWeightedReturnsSum.head())
        #self._dataWeightedReturns['PORTFOLIOWeighted'] = portfolio_weighted_returns
        portfolio_weighted_returns_mean = round(self._portfolio_weighted_returns.mean(), 5)
        print('port_ret mean', portfolio_weighted_returns_mean)
        print(round(self._stats.SimpleWeightedReturnsSum.mean(), 5))
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
        print('%', self._stats.Returns.head())
        self._data_returns_avg = self._getDataReturnsAverage(self._stats.Returns)
        print('^', self._data_returns_avg.head())
        daily_log_pct_changes: DataFrame = np.log(self._stats.Returns.pct_change() + 1) #avant portfolio
        daily_log_pct_changes.columns = daily_log_pct_changes.columns + 'LogReturn'
        print('&', daily_log_pct_changes.head())
        daily_log_volatilities: DataFrame = (daily_log_pct_changes.std() * np.sqrt(252)).to_frame()
        daily_log_volatilities.columns = ['Volatility']
        print('*', daily_log_volatilities)
        port_daily_simple_ret: float = round(np.sum(self._stats.SimpleReturnsNan.mean()*self._weights), 5)
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
        self._optimizer = PortfolioOptimizer(self._legend_place, self._a_float, self._stats, self._basics.Data)
        self._stock_market_index = SnP500Index('yahoo', "^GSPC", self._a_ts)
        self._linear_reg = PortfolioLinearReg(self._stock_market_index, self._stats.Returns)
        print(f'The portfolio beta is {self._linear_reg.Beta}, for each 1% of index portfolio will move {self._linear_reg.Beta}%')
        print('The portfolio alpha is ', self._linear_reg.Alpha)
        print('_', self._basics.DataLogReturns.head())
        cov_mat_annual = self._basics.DataLogReturns.cov() * 252
        print('-', cov_mat_annual)

    def _getDataReturnsAverage(self, a_df: DataFrame = DataFrame()) -> Series:
        return a_df.iloc[:, 0:self._a_length].sum(axis=1) / self._a_length

    def _setPortfolioInfo(self):
        port_annual_var: float = round(np.dot(self._weights.T, np.dot(self._dataSimpleCovarianceAnnual, self._weights)), 5)
        port_annual_volatility: float = round(np.sqrt(port_annual_var), 5)
        port_annual_simple_ret: float = round(np.sum(self._stats.SimpleReturnsNan.mean() * self._weights) * 252, 5)
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

    def PlotMarket(self) -> plt:
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31'
        stock_market_returns: Series = self._stock_market_index.Data.iloc[:, 0].pct_change()+1#[1:]
        stock_market_returns[np.isnan(stock_market_returns)] = 1
        print(stock_market_returns.head())
        sns.regplot(stock_market_returns.values, self._data_returns_avg.values)
        plt.xlabel('Benchmark Returns')
        plt.ylabel('Portfolio Returns')
        plt.title('Portfolio Returns vs Benchmark Returns')
        #plt.show()
        return plt

    def PlotOptimal(self):
        self._optimizer.Plot()

    def PlotBasics(self) -> plt:
        return self._basics.Plot()

    def PlotStats(self) -> plt:
        return self._stats.Plot()

    def PlotAllHeatmaps(self):
        prf_returns = (self._stats.Returns.pct_change() + 1)[1:]
        avg_return = (prf_returns-1).mean()
        daily_pct_change = np.log(self._stats.Returns.pct_change() + 1)
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
