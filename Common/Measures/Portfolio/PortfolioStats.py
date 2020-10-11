from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame, np, Series
from numpy import ndarray


class PortfolioStats(AbstractPortfolioMeasure):

    def __init__(self, portfolio_data: DataFrame = DataFrame()):
        portfolio_daily_ret = portfolio_data.pct_change()[1:]
        print(type(portfolio_daily_ret))
        #portfolio_ret = (portfolio_daily_ret * portfolio_weights).sum(axis=1)
        #print(type(portfolio_ret))
        #portfolio_ret_cum = (portfolio_ret + 1).cumprod()
        #print(type(portfolio_ret_cum))
        #portfolio_ret_geom_avg_annual = np.prod(portfolio_ret + 1) ** (252/portfolio_ret.shape[0]) - 1
        #print(type(portfolio_ret_geom_avg_annual))

    '''@property
    def AverageReturns(self):
        return self._std_err

    @property
    def StdDeviation(self):#volatility
        return self._std_err

    @property
    def SharpeRatio(self):
        return self._std_err'''
