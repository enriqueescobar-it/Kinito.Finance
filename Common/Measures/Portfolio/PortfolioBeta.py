import numpy as np
from pandas import DataFrame, Series
from scipy import stats

from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex


class PortfolioBeta(AbstractPortfolioMeasure):
    _index: AbstractStockMarketIndex
    _alpha: float = -1.1
    _beta: float = -1.1
    _r_val: float = -1.1
    _p_val: float = -1.1
    _std_err: float = -1.1

    def __init__(self, an_index: AbstractStockMarketIndex, portfolio_df_returns: DataFrame = DataFrame()):
        self._index = an_index
        index_returns: Series = an_index.HistoricalData.iloc[:, 0].pct_change() + 1
        index_returns[np.isnan(index_returns)] = 1
        nb_col: int = len(portfolio_df_returns.columns)
        portfolio_returns: Series = portfolio_df_returns.iloc[:, 0:nb_col].sum(axis=1) / nb_col
        (self._beta, self._alpha, self._r_val, self._p_val, self._std_err) = self._getValues(index_returns, portfolio_returns)
        self._beta = round(self._beta, 5)
        self._alpha = round(self._alpha, 5)

    def _getValues(self, index_returns: Series = Series(), portfolio_returns: Series = Series()):
        return stats.linregress(index_returns, portfolio_returns)

    @property
    def Alpha(self):
        return self._alpha

    @property
    def Beta(self):
        return self._beta

    @property
    def Rvalue(self):
        return self._r_val

    @property
    def Pvalue(self):
        return self._p_val

    @property
    def StdError(self):
        return self._std_err
