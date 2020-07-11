import pandas
import numpy as np


class MaximumDrawDownIndicator(object):
    """ Maximum Draw Down of a trading strategy KPI """
    KPIdf: np.float64

    def __init__(self, a_df: pandas.DataFrame):
        self.__setIndicator(a_df)

    def __setIndicator(self, a_df: pandas.DataFrame):
        """function to calculate Maximum Draw Down"""
        df: pandas.DataFrame = a_df.copy()
        df['DailyReturn'] = a_df['Adj Close'].pct_change()
        df['CumulativeReturn'] = (1 + df['DailyReturn']).cumprod()
        df['CumulativeRollMax'] = df['CumulativeReturn'].cummax()
        df['DrawDown'] = df['CumulativeRollMax'] - df['CumulativeReturn']
        df['DrawDownPercent'] = df['DrawDown'] / df['CumulativeRollMax']
        self.KPIdf = df['DrawDownPercent'].max()
