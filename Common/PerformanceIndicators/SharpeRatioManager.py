import pandas
import numpy as np


class SharpeRatioManager(object):
    """ Sharpe Ratio of a trading strategy KPI """
    KPIdf: np.float64

    def __init__(self, a_df: pandas.DataFrame, risk_free_rate: float = 0.022):
        self.__setIndicator(a_df, risk_free_rate)

    def __setIndicator(self, a_df: pandas.DataFrame, risk_free_rate):
        """function to calculate sharpe ratio ; rf is the risk free rate"""
        df: pandas.DataFrame = a_df.copy()
        self.KPIdf = (self.__getCagr(df) - risk_free_rate) / self.__getVolatility(df)

    @staticmethod
    def __getVolatility(a_df: pandas.DataFrame):
        """function to calculate annualized volatility of a trading strategy"""
        df: pandas.DataFrame = a_df.copy()
        df['DailyReturn'] = a_df['Adj Close'].pct_change()
        return df['DailyReturn'].std() * np.sqrt(252)

    @staticmethod
    def __getCagr(a_df: pandas.DataFrame):
        """function to calculate the Cumulative Annual Growth Rate of a trading strategy"""
        df: pandas.DataFrame = a_df.copy()
        df['DailyReturn'] = a_df['Adj Close'].pct_change()
        df['CumulativeReturn'] = (1 + df['DailyReturn']).cumprod()
        annual_length = len(df) / 252
        return (df['CumulativeReturn'][-1]) ** (1 / annual_length) - 1
