import pandas
import numpy as np


class CumulativeAnnualGrowthRateIndicator(object):
    """ Cumulative Annual Growth Rate of a trading strategy KPI """
    KPIdf: np.float64

    def __init__(self, a_df: pandas.DataFrame):
        self.__setIndicator(a_df)

    def __setIndicator(self, a_df: pandas.DataFrame):
        """function to calculate the Cumulative Annual Growth Rate of a trading strategy"""
        df: pandas.DataFrame = a_df.copy()
        df['DailyReturn'] = a_df['Adj Close'].pct_change()
        df['CumulativeReturn'] = (1 + df["DailyReturn"]).cumprod()
        annual_length = len(df) / 252
        self.KPIdf = (df['CumulativeReturn'][-1]) ** (1 / annual_length) - 1
