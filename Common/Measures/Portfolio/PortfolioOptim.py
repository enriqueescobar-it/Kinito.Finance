from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame, np, Series
import matplotlib.pyplot as plt


class PortfolioOptim(AbstractPortfolioMeasure):
    _threshold: int = 5000
    _weight_matrix: np.ndarray
    _return_matrix: np.ndarray
    _risk_matrix: np.ndarray
    _sharpe_ratio_matrix: np.ndarray

    def __init__(self, portfolio_data: DataFrame = DataFrame(), log_ret: DataFrame = DataFrame(),
                 cov_mat: DataFrame = DataFrame()):
        # Creating an empty array to store portfolio weights
        self._weight_matrix = np.zeros((self._threshold, len(portfolio_data.columns)))
        # Creating an empty array to store portfolio returns
        self._return_matrix = np.zeros(self._threshold)
        # Creating an empty array to store portfolio risks
        self._risk_matrix = np.zeros(self._threshold)
        # Creating an empty array to store portfolio sharpe ratio
        self._sharpe_ratio_matrix = np.zeros(self._threshold)
        self._setMatrices(portfolio_data, log_ret, cov_mat)

    def _setMatrices(self, portfolio_data: DataFrame, log_ret: DataFrame, cov_mat: DataFrame):
        for i in range(self._threshold):
            wts: np.ndarray = np.random.uniform(size=len(portfolio_data.columns))
            wts = wts / np.sum(wts)
            # saving weights in the array
            self._weight_matrix[i, :] = wts
            # Portfolio Returns
            port_ret: float = np.sum(log_ret.mean() * wts)
            port_ret = (port_ret + 1) ** 252 - 1
            # Saving Portfolio returns
            self._return_matrix[i] = port_ret
            # Saving Portfolio Risk
            port_sd: float = np.sqrt(np.dot(wts.T, np.dot(cov_mat, wts)))
            self._risk_matrix[i] = port_sd
            # Portfolio Sharpe Ratio
            # Assuming 0% Risk Free Rate
            sr: float = port_ret / port_sd
            self._sharpe_ratio_matrix[i] = sr
        col_names = portfolio_data.columns
        print('col_names', col_names)
        min_var: np.ndarray = self._weight_matrix[self._risk_matrix.argmin()]
        print('min_var', min_var)
        max_sr: np.ndarray = self._weight_matrix[self._sharpe_ratio_matrix.argmax()]
        print('max_sr', max_sr)
        print('sharpe_ratio', self._sharpe_ratio_matrix.max())
        print('port_risk', self._risk_matrix.min())
        min_var: Series = Series(min_var, index=col_names)
        min_var = min_var.sort_values()
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_xlabel('Asset')
        ax1.set_ylabel('Weights')
        ax1.set_title('Minimum Variance Portfolio weights')
        min_var.plot(kind='bar')
        plt.setp(ax1.get_xticklabels(), rotation=45)
        plt.show()
        max_sr = Series(max_sr, index=col_names)
        max_sr = max_sr.sort_values()
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_xlabel('Asset')
        ax1.set_ylabel('Weights')
        ax1.set_title('Tangency Portfolio weights')
        max_sr.plot(kind='bar')
        plt.setp(ax1.get_xticklabels(), rotation=45)
        plt.show()
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_xlabel('Risk')
        ax1.set_ylabel('Returns')
        ax1.set_title('Portfolio optimization and Efficient Frontier')
        plt.scatter(self._risk_matrix, self._return_matrix)
        plt.show()
