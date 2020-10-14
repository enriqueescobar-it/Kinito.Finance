from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame, np, Series
import matplotlib.pyplot as plt


class PortfolioOptim(AbstractPortfolioMeasure):
    _threshold: int = 5000
    _weight_matrix: np.ndarray
    _annual_weighted_log_return_matrix: np.ndarray
    _risk_matrix: np.ndarray
    _sharpe_ratio_matrix: np.ndarray

    def __init__(self, portfolio_data: DataFrame = DataFrame(), log_ret: DataFrame = DataFrame(),
                 cov_mat: DataFrame = DataFrame()):
        # Creating an empty array to store portfolio weights
        self._weight_matrix = np.zeros((self._threshold, len(portfolio_data.columns)))
        # Creating an empty array to store portfolio returns
        self._annual_weighted_log_return_matrix = np.zeros(self._threshold)
        # Creating an empty array to store portfolio risks
        self._risk_matrix = np.zeros(self._threshold)
        # Creating an empty array to store portfolio sharpe ratio
        self._sharpe_ratio_matrix = np.zeros(self._threshold)
        self._setMatrices(portfolio_data, log_ret, cov_mat)
        col_names = portfolio_data.columns.str.replace('Adj Close', '')
        print('col_names', col_names)
        min_risk_arr: np.ndarray = self._weight_matrix[self._risk_matrix.argmin()]
        print('min_risk_arr', min_risk_arr)
        max_sharpe_ratio_arr: np.ndarray = self._weight_matrix[self._sharpe_ratio_matrix.argmax()]
        print('max_sharpe_ratio_arr', max_sharpe_ratio_arr)
        print('sharpe_ratio.max', self._sharpe_ratio_matrix.max())
        print('portfolio_risk.min', self._risk_matrix.min())
        min_risk_serie: Series = Series(min_risk_arr, index=col_names)
        print('0', min_risk_serie)
        #min_var = min_var.sort_values()
        #print('1', min_var)
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_xlabel('Asset')
        ax1.set_ylabel('Weights')
        ax1.set_title('Minimum Variance Portfolio weights')
        min_risk_serie.plot(kind='bar')
        plt.setp(ax1.get_xticklabels(), rotation=45)
        plt.show()
        max_sharpe_ratio_serie = Series(max_sharpe_ratio_arr, index=col_names)
        print('0', max_sharpe_ratio_serie)
        #max_sr = max_sr.sort_values()
        #print('1', max_sr)
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_xlabel('Asset')
        ax1.set_ylabel('Weights')
        ax1.set_title('Tangency Portfolio weights')
        max_sharpe_ratio_serie.plot(kind='bar')
        plt.setp(ax1.get_xticklabels(), rotation=45)
        plt.show()
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_xlabel('Risk')
        ax1.set_ylabel('Returns')
        ax1.set_title('Portfolio optimization and Efficient Frontier')
        plt.scatter(self._risk_matrix, self._annual_weighted_log_return_matrix)
        plt.show()

    def _setMatrices(self, portfolio_data: DataFrame, log_ret: DataFrame, cov_mat: DataFrame):
        for i in range(self._threshold):
            weight_arr: np.ndarray = np.random.uniform(size=len(portfolio_data.columns))
            weight_arr = weight_arr / np.sum(weight_arr)
            # saving weights in the array
            self._weight_matrix[i, :] = weight_arr
            # Portfolio Returns
            annual_weighted_log_ret: float = ((np.sum(log_ret.mean() * weight_arr)) + 1) ** 252 - 1
            # Saving Portfolio returns
            self._annual_weighted_log_return_matrix[i] = annual_weighted_log_ret
            # Saving Portfolio Risk
            portfolio_sd: float = np.sqrt(np.dot(weight_arr.T, np.dot(cov_mat, weight_arr)))
            self._risk_matrix[i] = portfolio_sd
            # Portfolio Sharpe Ratio
            # Assuming 0% Risk Free Rate
            sr: float = annual_weighted_log_ret / portfolio_sd
            self._sharpe_ratio_matrix[i] = sr
