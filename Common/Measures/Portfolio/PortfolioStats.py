from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame, np, Series
from numpy import ndarray


class PortfolioStats(AbstractPortfolioMeasure):
    _annual_sharpe_ratio: float = -1.1
    _annual_ret_std: float = -1.1
    _geom_avg_annual_ret: float = -1.1

    def __init__(self, portfolio_weights: ndarray, portfolio_data: DataFrame = DataFrame()):
        print(portfolio_data.shape)
        portfolio_daily_ret: DataFrame = portfolio_data.pct_change()[1:]
        print(portfolio_daily_ret.shape)
        portfolio_ret: Series = (portfolio_daily_ret * portfolio_weights).sum(axis=1)
        print(portfolio_ret.shape)
        portfolio_ret_cum: Series = (portfolio_ret + 1).cumprod()
        print(portfolio_ret_cum.shape)
        self._geom_avg_annual_ret: float = np.prod(portfolio_ret + 1) ** (252 / portfolio_ret.shape[0]) - 1
        self._geom_avg_annual_ret = round(self._geom_avg_annual_ret, 5)
        #print(self._geom_avg_annual_ret)
        self._annual_ret_std: float = np.std(portfolio_ret) * np.sqrt(252)
        self._annual_ret_std = round(self._annual_ret_std, 5)
        #print(self._annual_ret_std)
        self._annual_sharpe_ratio: float = self._geom_avg_annual_ret / self._annual_ret_std
        self._annual_sharpe_ratio = round(self._annual_sharpe_ratio, 5)

    '''@property
    def AverageReturns(self):
        return self._std_err'''

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
