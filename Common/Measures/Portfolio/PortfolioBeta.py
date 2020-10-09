import numpy as np
from pandas import DataFrame, Series
from scipy import stats

from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex


class PortfolioBeta(AbstractPortfolioMeasure):
    _index: AbstractStockMarketIndex
    alpha: float = -1.1
    beta: float = -1.1
    r_val: float = -1.1
    p_val: float = -1.1
    std_err: float = -1.1

    def __init__(self, an_index: AbstractStockMarketIndex, portfolio_df_returns: DataFrame = DataFrame()):
        self._index = an_index
        index_returns: Series = an_index.HistoricalData.iloc[:, 0].pct_change() + 1
        index_returns[np.isnan(index_returns)] = 1
        nb_col: int = len(portfolio_df_returns.columns)
        portfolio_returns: Series = portfolio_df_returns.iloc[:, 0:nb_col].sum(axis=1) / nb_col
        (self.beta, self.alpha, self.r_val, self.p_val, self.std_err) = self._getValues(index_returns, portfolio_returns)
        self.beta = round(self.beta, 5)
        self.alpha = round(self.alpha, 5)

    def _getValues(self, index_returns: Series = Series(), portfolio_returns: Series = Series()):
        return stats.linregress(index_returns, portfolio_returns)
