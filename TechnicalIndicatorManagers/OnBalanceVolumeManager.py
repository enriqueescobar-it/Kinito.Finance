import pandas
import numpy as np


class OnBalanceVolumeManager(object):
    """On Balance Volume manager class"""
    IndicatorDf: pandas.DataFrame

    def __init__(self, a_df: pandas.DataFrame):
        self.__setIndicator(a_df)

    def __setIndicator(self, a_df: pandas.DataFrame):
        """function to calculate On Balance Volume"""
        df: pandas.DataFrame = a_df.copy()
        df['DailyReturn'] = df['Adj Close'].pct_change()
        df['Direction'] = np.where(df['DailyReturn'] >= 0, 1, -1)
        df['Direction'][0] = 0
        df['VolumeAdj'] = df['Volume'] * df['Direction']
        df['OnBalanceVolume'] = df['VolumeAdj'].cumsum()
        self.IndicatorDf = df
