from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame, np, Series
from numpy import ndarray
import matplotlib.pyplot as plt
from math import sqrt
from scipy.cluster.vq import kmeans, vq
from sklearn.cluster import KMeans
from pylab import plot, show
from numpy import vstack, array


class PortfolioStats(AbstractPortfolioMeasure):
    _a_title: str = ''
    _a_float: float = -1.1
    _legend_place: str = ''
    _annual_sharpe_ratio: float = -1.1
    _annual_ret_std: float = -1.1
    _geom_avg_annual_ret: float = -1.1
    _column: str = 'Adj Close'
    _returns: DataFrame = DataFrame()
    _simple_returns: DataFrame = DataFrame()
    _simple_returns_cumulative: DataFrame = DataFrame()
    _simple_returns_summary: DataFrame = DataFrame()
    _simple_daily_returns: DataFrame = DataFrame()
    _log_daily_returns: DataFrame = DataFrame()
    _simple_weighted_returns: DataFrame = DataFrame()
    _simple_cum_weighted_returns: DataFrame = DataFrame()

    def __init__(self, portfolio_weights: ndarray, a_str: str = 'Adj Close', portfolio_data: DataFrame = DataFrame(),
                 a_title: str = '', a_float: float = -1.1, legend_place: str = ''):
        self._a_float = a_float
        self._a_title = a_title
        self._legend_place = legend_place
        print(portfolio_data.head(3))
        self._column = a_str
        self._returns = self._getReturns(portfolio_data)
        self._simple_returns = self._getSimpleReturnsNan(portfolio_data)
        self._simple_returns_cumulative = self._getSimpleReturnsNanCumulative(self._simple_returns)
        self._simple_returns_summary = self._getSimpleReturnsNanSummary(self._simple_returns)
        self._simple_daily_returns = self._getSimpleDailyReturns(portfolio_data)
        self._log_daily_returns = self._getLogDailyReturns(portfolio_data)
        portfolio_weighted_returns: Series = (self._simple_daily_returns * portfolio_weights).sum(axis=1)
        self._simple_weighted_returns['SimpleWeightedReturns'] = portfolio_weighted_returns
        portfolio_cum_weighted_returns: Series = (portfolio_weighted_returns + 1).cumprod()
        self._simple_cum_weighted_returns['SimpleCumWeightedReturns'] = portfolio_cum_weighted_returns
        self._geom_avg_annual_ret = self._getGeomAvgAnnualRet(portfolio_weighted_returns)
        self._annual_ret_std = self._getAnnualReturnStd(portfolio_weighted_returns)
        self._annual_sharpe_ratio = self._getAnnualSharpeRatio()

    def __roundFloat(self, a_float: float) -> float:
        return round(a_float, 5)

    def _getReturns(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame = (a_df / a_df.iloc[0]).fillna(method='backfill')
        new_df.fillna(method='ffill', inplace=True)
        new_df.columns = new_df.columns.str.replace(self._column, '')
        return new_df

    def _getSimpleReturnsNan(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        # == (self._data / self._data.shift(1))-1
        new_df: DataFrame = a_df.pct_change(1)
        new_df.columns = new_df.columns.str.replace(self._column, 'SimpleReturns')
        return new_df

    def _getSimpleReturnsNanCumulative(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame = (a_df + 1).cumprod()
        new_df.columns = new_df.columns.str.replace('Returns', 'Cumulative')
        return new_df

    def _getSimpleReturnsNanSummary(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame = DataFrame()
        new_df['Volatility'] = a_df.std()
        new_df['Daily'] = a_df.mean()
        new_df['Variance'] = a_df.var()
        return new_df

    def _getSimpleDailyReturns(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame() = a_df.pct_change()[1:]
        new_df.columns = new_df.columns.str.replace(self._column, 'SimpleDailyRet')
        # can do all lines but line 0 should be = 0
        return new_df

    def _getLogDailyReturns(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame() = np.log(a_df / a_df.shift(1))
        new_df.columns = new_df.columns.str.replace(self._column, 'LogDailyRet')
        return new_df

    def _getGeomAvgAnnualRet(self, a_series: Series = Series()) -> float:
        return self.__roundFloat(np.prod(a_series + 1) ** (252 / a_series.shape[0]) - 1)

    def _getAnnualReturnStd(self, a_series: Series = Series()) -> float:
        return self.__roundFloat(np.std(a_series) * np.sqrt(252))

    def _getAnnualSharpeRatio(self) -> float:
        return self.__roundFloat(self._geom_avg_annual_ret / self._annual_ret_std)

    def Plot(self) -> plt:
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31'
        fig, ax = plt.subplots(3, 1, figsize=(self._a_float, self._a_float/1.5), sharex=True)
        fig.suptitle(self._a_title)
        self._simple_returns_cumulative.plot(ax=ax[0], label=self._simple_returns_cumulative.columns)
        ax[0].set(ylabel='Simple Return - Cumulative')
        ax[0].legend(loc=self._legend_place)
        self._simple_returns.plot(ax=ax[1], label=self._simple_returns.columns)
        ax[1].set(ylabel='Simple Return - Volatility')
        ax[1].legend(loc=self._legend_place)
        self._returns.plot(ax=ax[2], label=self._returns.columns)
        ax[2].set(ylabel='Returns')
        ax[2].legend(loc=self._legend_place)
        plt.tight_layout()
        return plt

    # volatility
    @property
    def AnnualStdDeviation(self):
        return self._annual_ret_std

    @property
    def GeometricAnnualReturnAverage(self):
        return self._geom_avg_annual_ret

    @property
    def AnnualSharpeRatio(self):
        return self._annual_sharpe_ratio

    @property
    def Returns(self):
        return self._returns

    @property
    def SimpleReturnsNan(self):
        return self._simple_returns

    @property
    def SimpleReturnsNanSummary(self):
        return self._simple_returns_summary

    @property
    def SimpleReturnsNanCumulative(self):
        return self._simple_returns_cumulative

    @property
    def SimpleDailyReturns(self):
        return self._simple_daily_returns

    @property
    def SimpleWeightedReturns(self):
        return self._simple_weighted_returns

    @property
    def SimpleCumWeightedReturns(self):
        return self._simple_cum_weighted_returns

    @property
    def LogDailyReturns(self):
        return self._log_daily_returns

    @property
    def LogDailyCovarianceMatrix(self):
        return self._log_daily_returns.cov()

    @property
    def LogWeeklyCovarianceMatrix(self):
        return self._log_daily_returns.cov() * 5

    @property
    def LogMonthlyCovarianceMatrix(self):
        return self._log_daily_returns.cov() * 21

    @property
    def LogQuarterlyCovarianceMatrix(self):
        return self._log_daily_returns.cov() * 63

    @property
    def LogAnnualCovarianceMatrix(self):
        return self._log_daily_returns.cov() * 252
