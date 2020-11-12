from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from Common.Measures.Time.TimeSpan import TimeSpan
from finquant.portfolio import build_portfolio
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

class PortfolioFinal(AbstractPortfolioMeasure):
    _data: DataFrame = DataFrame()
    _annualised_expected_return: float = -1.1
    _volatility: float = -1.1
    _sharpe_risk_free005: float = -1.1
    _annualised_mean_return_series: Series = Series()
    _skewness_series: Series = Series()
    _kurtosis_series: Series = Series()
    _portfolio_df: DataFrame = DataFrame()
    _cumulative_return_df: DataFrame = DataFrame()
    _cumulative_log_return_df: DataFrame = DataFrame()
    _pct_chng_return_df: DataFrame = DataFrame()
    _pct_chng_log_return_df: DataFrame = DataFrame()

    def __init__(self, y_stocks: list):
        yahoo_list: list = list()
        t_s: TimeSpan = y_stocks[0].TimeSpan
        for y_stock in y_stocks:
            yahoo_list.append(y_stock.Ticker)
        pf = build_portfolio(names=yahoo_list, start_date=t_s.StartDateStr, end_date=t_s.EndDateStr,
                             data_api='yfinance')
        self._data = pf.data
        # print(pf.properties())
        print(pf.portfolio.name)
        self._portfolio_df = pf.portfolio
        # annualised expected return
        self._annualised_expected_return = pf.expected_return
        # annualised mean returns
        self._annualised_mean_return_series = pf.comp_mean_returns()
        # volatility
        self._volatility = pf.volatility
        # Sharpe ratio (computed with a risk free rate of 0.005 by default)
        self._sharpe_risk_free005 = pf.sharpe
        # Getting Skewness and Kurtosis of the stocks
        self._skewness_series = pf.skew
        self._kurtosis_series = pf.kurtosis
        # daily returns (percentage change) price_{t} - price_{t=0}) / price_{t=0}
        self._cumulative_return_df = pf.comp_cumulative_returns()
        self._cumulative_return_df.plot().axhline(y=0, color="darkgrey", lw=3)
        plt.show()
        self._cumulative_log_return_df = pf.comp_daily_log_returns().cumsum()
        self._cumulative_log_return_df.plot().axhline(y=0, color="darkgrey", lw=3)
        plt.show()
        # daily percentage changes of returns
        self._pct_chng_return_df = pf.comp_daily_returns()
        # plotting daily percentage changes of returns
        self._pct_chng_return_df.plot().axhline(y=0, color="darkgrey")
        plt.show()
        self._pct_chng_log_return_df = pf.comp_daily_log_returns()
        # plotting daily log returns
        self._pct_chng_log_return_df.plot().axhline(y=0, color="darkgrey")
        plt.show()
        # building a portfolio by providing stock data
        # pf = build_portfolio(data=df_data)
