from typing import List
import pandas
import numpy as np
import statsmodels.api as sm

from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class SlopesIndicator(AbstractTechIndicator):
    """Slopes of n consecutive points on a plot manager class"""
    IndicatorDf: pandas.DataFrame

    def __init__(self, a_df: pandas.DataFrame):
        self.__setIndicator(a_df)

    def __setIndicator(self, a_df: pandas.DataFrame, nb_points: int = 5):
        """function to calculate the slope of n consecutive points on a plot"""
        df: pandas.DataFrame = a_df.copy()
        n: int = nb_points  # you can use 20 or more
        slopesTitle: str = "Slopes{0}".format(str(n))
        slopes: List[int] = [i * 0 for i in range(n - 1)]
        a_series = df['Adj Close']
        i: int
        for i in range(n, len(a_series) + 1):
            y = a_series[i - n:i]
            x = np.array(range(n))
            y_scaled = (y - y.min()) / (y.max() - y.min())
            x_scaled = (x - x.min()) / (x.max() - x.min())
            # y = mx+c this is c
            x_scaled = sm.add_constant(x_scaled)
            modelOrdinaryLeastSquares = sm.OLS(y_scaled, x_scaled)
            modelOrdinaryLeastSquaresFitted = modelOrdinaryLeastSquares.fit()
            slopes.append(modelOrdinaryLeastSquaresFitted.params[-1])
        slope_angle = (np.rad2deg(np.arctan(np.array(slopes))))
        df[slopesTitle] = np.array(slope_angle)
        self.IndicatorDf = df
