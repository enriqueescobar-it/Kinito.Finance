from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from Common.Measures.Time.TimeSpan import TimeSpan
from finquant.portfolio import build_portfolio
from pandas import DataFrame, Series
import matplotlib.pyplot as plt


class PortfolioFinal(AbstractPortfolioMeasure):
    _freq: int = -1
    _size: float = -1.1
    _risk_free_rate: float = -1.1
    _annualised_expected_return: float = -1.1
    _volatility: float = -1.1
    _sharpe_risk_free005: float = -1.1
    _a_title: str = ''
    _legend_place: str = ''
    _annualised_mean_return_series: Series = Series()
    _skewness_series: Series = Series()
    _kurtosis_series: Series = Series()
    _data: DataFrame = DataFrame()
    _portfolio_df: DataFrame = DataFrame()
    _cumulative_return_df: DataFrame = DataFrame()
    _cumulative_log_return_df: DataFrame = DataFrame()
    _pct_chng_return_df: DataFrame = DataFrame()
    _pct_chng_log_return_df: DataFrame = DataFrame()

    def __init__(self, y_stocks: list,  a_float: float, legend_place: str):
        yahoo_list: list = list()
        self._size = a_float
        self._a_title = 'a title'
        self._legend_place = legend_place
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
        self._cumulative_log_return_df = pf.comp_daily_log_returns().cumsum()
        # daily percentage changes of returns
        self._pct_chng_return_df = pf.comp_daily_returns()
        self._pct_chng_log_return_df = pf.comp_daily_log_returns()
        # building a portfolio by providing stock data
        # pf = build_portfolio(data=df_data)
        # # Portfolio optimisation
        # ## Efficient Frontier
        # Based on the **Efficient Frontier**, the portfolio can be optimised for
        #  - minimum volatility
        #  - maximum Sharpe ratio
        #  - minimum volatility for a given target return
        #  - maximum Sharpe ratio for a given target volatility
        # See below for an example for each optimisation.
        # if needed, change risk free rate and frequency/time window of the portfolio
        self._freq = pf.freq
        self._risk_free_rate = pf.risk_free_rate
        print('ef_minimum_volatility')
        pf.ef_minimum_volatility(verbose=True)
        # optimisation for maximum Sharpe ratio
        print('ef_maximum_sharpe_ratio')
        pf.ef_maximum_sharpe_ratio(verbose=True)
        # minimum volatility for a given target return of 0.26
        print('ef_efficient_return: target return 0.26')
        pf.ef_efficient_return(0.26, verbose=True)
        # maximum Sharpe ratio for a given target volatility of 0.22
        print('ef_efficient_volatility: target volatility 0.22')
        pf.ef_efficient_volatility(0.22, verbose=True)

    def Plot(self): #-> plt:
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31'
        fig, ax = plt.subplots(2, 2, figsize=(self._size / 2.0, self._size / 2.0), sharex=True)
        fig.suptitle(self._a_title)
        #plt.title('another title', fontsize=18)
        self._cumulative_return_df.plot(ax=ax[0, 0]).axhline(y=0, color="darkgrey", lw=3)
        self._cumulative_log_return_df.plot(ax=ax[0, 1]).axhline(y=0, color="darkgrey", lw=3)
        # plotting daily percentage changes of returns
        self._pct_chng_return_df.plot(ax=ax[1, 0]).axhline(y=0, color="darkgrey")
        # plotting daily log returns
        self._pct_chng_log_return_df.plot(ax=ax[1, 1]).axhline(y=0, color="darkgrey")
        plt.tight_layout()
        return plt

    @property
    def Frequency(self):
        return self._freq

    @property
    def Volatility(self):
        return round(self._volatility, 5)

    @property
    def RiskFreeRate(self):
        return round(self._risk_free_rate, 5)

    @property
    def Free005SharpeRatio(self):
        return round(self._sharpe_risk_free005, 5)

    @property
    def AnnualExpectedReturn(self):
        return round(self._annualised_expected_return, 5)

    @property
    def AnnualMeanReturnSeries(self):
        return self._annualised_mean_return_series

    @property
    def SkewnessSeries(self):
        return self._skewness_series

    @property
    def KurtosisSeries(self):
        return self._kurtosis_series

    @property
    def CumulativeSimpleReturns(self):
        return self._cumulative_return_df

    @property
    def CumulativeLogReturns(self):
        return self._cumulative_log_return_df

    @property
    def DailyPcntChangesSimpleReturns(self):
        return self._pct_chng_return_df

    @property
    def DailyPcntChangesLogReturns(self):
        return self._pct_chng_log_return_df
