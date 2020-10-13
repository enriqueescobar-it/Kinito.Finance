from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame, np, Series
from numpy import ndarray


class PortfolioStats(AbstractPortfolioMeasure):
    _annual_sharpe_ratio: float = -1.1
    _annual_ret_std: float = -1.1
    _geom_avg_annual_ret: float = -1.1
    _simple_daily_returns: DataFrame = DataFrame()
    _simple_weighted_returns: DataFrame = DataFrame()
    _simple_cum_weighted_returns: DataFrame = DataFrame()

    def __init__(self, portfolio_weights: ndarray, portfolio_data: DataFrame = DataFrame()):
        print(portfolio_data.head(3))
        self._simple_daily_returns: DataFrame = self._getSimpleDailyReturns(portfolio_data)
        print(self._simple_daily_returns.head(3))
        portfolio_weighted_returns: Series = (self._simple_daily_returns * portfolio_weights).sum(axis=1)
        self._simple_weighted_returns['SimpleWeightedReturns'] = portfolio_weighted_returns
        print(self._simple_weighted_returns.head(3))
        portfolio_cum_weighted_returns: Series = (portfolio_weighted_returns + 1).cumprod()
        self._simple_cum_weighted_returns['SimpleCumWeightedReturns'] = portfolio_cum_weighted_returns
        print(self._simple_cum_weighted_returns.head(3))
        self._geom_avg_annual_ret: float = np.prod(portfolio_weighted_returns + 1) ** (252 / portfolio_weighted_returns.shape[0]) - 1
        self._geom_avg_annual_ret = round(self._geom_avg_annual_ret, 5)
        #print(self._geom_avg_annual_ret)
        self._annual_ret_std: float = np.std(portfolio_weighted_returns) * np.sqrt(252)
        self._annual_ret_std = round(self._annual_ret_std, 5)
        #print(self._annual_ret_std)
        self._annual_sharpe_ratio: float = self._geom_avg_annual_ret / self._annual_ret_std
        self._annual_sharpe_ratio = round(self._annual_sharpe_ratio, 5)

    def _getSimpleDailyReturns(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        a_df.columns = a_df.columns.str.replace('Adj Close', 'SimpleDailyRet')
        # can do all lines but line 0 should be = 0
        return a_df.pct_change()[1:]

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
    def SimpleDailyReturns(self):
        return self._simple_daily_returns

    @property
    def SimpleWeightedReturns(self):
        return self._simple_weighted_returns

    @property
    def SimpleCumWeightedReturns(self):
        return self._simple_cum_weighted_returns
