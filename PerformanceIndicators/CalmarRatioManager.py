import pandas
import numpy as np


class CalmarRatioManager(object):
    """ Calmar Ratio of a trading strategy KPI """
    KPIdf: np.float64

    def __init__(self, a_df: pandas.DataFrame):
        self.__setIndicator(a_df)

    def __setIndicator(self, a_df: pandas.DataFrame):
        """function to calculate Calmar Ratio"""
        df: pandas.DataFrame = a_df.copy()
        self.KPIdf = self.__getCagr(df) / self.__getMaxDrawDown(df)

    @staticmethod
    def __getCagr(a_df: pandas.DataFrame):
        """function to calculate the Cumulative Annual Growth Rate of a trading strategy"""
        df: pandas.DataFrame = a_df.copy()
        df['DailyReturn'] = a_df['Adj Close'].pct_change()
        df['CumulativeReturn'] = (1 + df['DailyReturn']).cumprod()
        annual_length = len(df) / 252
        return (df['CumulativeReturn'][-1]) ** (1 / annual_length) - 1

    @staticmethod
    def __getMaxDrawDown(a_df: pandas.DataFrame):
        """function to calculate the Maximum Draw Down of a trading strategy"""
        df: pandas.DataFrame = a_df.copy()
        df['DailyReturn'] = a_df['Adj Close'].pct_change()
        df['CumulativeReturn'] = (1 + df['DailyReturn']).cumprod()
        df['CumulativeRollMax'] = df['CumulativeReturn'].cummax()
        df['DrawDown'] = df['CumulativeRollMax'] - df['CumulativeReturn']
        df['DrawDownPercent'] = df['DrawDown'] / df['CumulativeRollMax']
        return df['DrawDownPercent'].max()
