from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame, np, Series
import matplotlib.pyplot as plt


class PortfolioOptim(AbstractPortfolioMeasure):
    _threshold: int = 5000

    def __init__(self, portfolio_data: DataFrame = DataFrame(), log_ret: DataFrame = DataFrame(),
                 cov_mat: DataFrame = DataFrame()):
        # Creating an empty array to store portfolio weights
        all_wts: np.ndarray = np.zeros((self._threshold, len(portfolio_data.columns)))
        # Creating an empty array to store portfolio returns
        port_returns: np.ndarray = np.zeros(self._threshold)
        # Creating an empty array to store portfolio risks
        port_risk: np.ndarray = np.zeros(self._threshold)
        # Creating an empty array to store portfolio sharpe ratio
        sharpe_ratio: np.ndarray = np.zeros(self._threshold)
        for i in range(self._threshold):
            wts: np.ndarray = np.random.uniform(size=len(portfolio_data.columns))
            wts = wts / np.sum(wts)
            # saving weights in the array
            all_wts[i, :] = wts
            # Portfolio Returns
            port_ret: float = np.sum(log_ret.mean() * wts)
            port_ret = (port_ret + 1) ** 252 - 1
            # Saving Portfolio returns
            port_returns[i] = port_ret
            # Saving Portfolio Risk
            port_sd: float = np.sqrt(np.dot(wts.T, np.dot(cov_mat, wts)))
            port_risk[i] = port_sd
            # Portfolio Sharpe Ratio
            # Assuming 0% Risk Free Rate
            sr: float = port_ret / port_sd
            sharpe_ratio[i] = sr
        col_names = portfolio_data.columns
        min_var: np.ndarray = all_wts[port_risk.argmin()]
        print('min_var', min_var)
        max_sr: np.ndarray = all_wts[sharpe_ratio.argmax()]
        print('max_sr', max_sr)
        print('sharpe_ratio', sharpe_ratio.max())
        print('port_risk', port_risk.min())
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
        plt.scatter(port_risk, port_returns)
        plt.show()
