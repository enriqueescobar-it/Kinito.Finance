from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame, np, Series
import matplotlib.pyplot as plt
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices


class PortfolioOptimizer(AbstractPortfolioMeasure):
    _threshold: int = 5000
    _weight_matrix: np.ndarray
    _annual_weighted_log_return_matrix: np.ndarray
    _risk_matrix: np.ndarray
    _sharpe_ratio_matrix: np.ndarray
    _min_risk_series: Series = Series()
    _max_sharpe_ratio_series: Series = Series()

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
        print('portfolio_risk.min', self._risk_matrix.min())
        print('sharpe_ratio.max', self._sharpe_ratio_matrix.max())
        self._min_risk_series = \
            self._getMinimalRisk(self._weight_matrix[self._risk_matrix.argmin()], portfolio_data.columns)
        print(self._min_risk_series)
        self._plotMinimalRisk()
        self._max_sharpe_ratio_series = \
            self._getMaximalSharpeRatio(self._weight_matrix[self._sharpe_ratio_matrix.argmax()], portfolio_data.columns)
        print(self._max_sharpe_ratio_series)
        self._plotMaximalSharpeRatio()
        self._plotRiskReturns(portfolio_data)
        mu = expected_returns.mean_historical_return(portfolio_data)  # returns.mean() * 252
        S = risk_models.sample_cov(portfolio_data)  # Get the sample covariance matrix
        ef = EfficientFrontier(mu, S)
        weights = ef.max_sharpe()  # Maximize the Sharpe ratio, and get the raw weights
        cleaned_weights = ef.clean_weights()
        print(
            cleaned_weights)  # Note the weights may have some rounding error, meaning they may not add up exactly to 1 but should be close
        ef.portfolio_performance(verbose=True)
        latest_prices = get_latest_prices(portfolio_data)
        weights = cleaned_weights
        da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=10000)
        allocation, leftover = da.lp_portfolio()
        print("Discrete allocation:", allocation)
        print("Funds remaining: ${:.2f}".format(leftover))

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

    def _getMinimalRisk(self, risk_arr: np.ndarray, col_names) -> Series:
        a_col_names = col_names.str.replace('Adj Close', 'risk')
        return Series(risk_arr, index=a_col_names)

    def _plotMinimalRisk(self):
        plt.style.use('seaborn')
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_xlabel('Asset')
        ax1.set_ylabel('Weights')
        ax1.set_title('Minimum Variance Portfolio weights')
        self._min_risk_series.plot(kind='bar')
        plt.setp(ax1.get_xticklabels(), rotation=45)
        plt.show()

    def _getMaximalSharpeRatio(self, sharpe_ratio_arr: np.ndarray, col_names) -> Series:
        a_col_names = col_names.str.replace('Adj Close', 'SharpeRatio')
        return Series(sharpe_ratio_arr, index=a_col_names)

    def _plotMaximalSharpeRatio(self):
        plt.style.use('seaborn')
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_xlabel('Asset')
        ax1.set_ylabel('Weights')
        ax1.set_title('Maximal Sharpe Ratio Portfolio weights')
        self._max_sharpe_ratio_series.plot(kind='bar')
        plt.setp(ax1.get_xticklabels(), rotation=45)
        plt.show()

    def _plotRiskReturns(self, portfolio_data: DataFrame):
        plt.style.use('seaborn')
        fig = plt.figure()
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_xlabel('Risk')
        ax1.set_ylabel('Returns')
        ax1.set_title('Portfolio optimization and Efficient Frontier')
        for i, txt in enumerate(portfolio_data.columns):
            ax1.annotate(txt,
                         (self._risk_matrix[i], self._annual_weighted_log_return_matrix[i]),
                         xytext=(10, 0),
                         arrowprops=dict(facecolor='black', shrink=0.05), textcoords='offset points')
        plt.scatter(self._risk_matrix, self._annual_weighted_log_return_matrix,
                    c=self._sharpe_ratio_matrix, cmap='coolwarm', marker='o', s=10, alpha=0.7)
        plt.colorbar(label='Sharpe Ratio')
        plt.scatter(self._risk_matrix[self._sharpe_ratio_matrix.argmax()],
                    self._annual_weighted_log_return_matrix[self._sharpe_ratio_matrix.argmax()],
                    marker='*', color='red', s=500, edgecolors='black', label='Maximum Sharpe ratio')
        plt.scatter(self._risk_matrix[self._risk_matrix.argmin()],
                    self._annual_weighted_log_return_matrix[self._risk_matrix.argmin()],
                    marker='*', color='blue', s=500, label='Minimum volatility')
        plt.show()

    @property
    def MinimalRiskSeries(self):
        return self._min_risk_series

    @property
    def MaximalSharpeRatio(self):
        return self._max_sharpe_ratio_series
