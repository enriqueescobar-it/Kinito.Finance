import datetime
import pandas

from Common.TechIndicators.AbstractIndicatorManager import AbstractIndicatorManager


class MovingAverageConvergenceDivergenceManager(AbstractIndicatorManager):
    """ MACD indicator manager class"""
    IndicatorDf: pandas.DataFrame

    def __init__(self, a_df: pandas.DataFrame, from_date: datetime.date, to_date: datetime.date):
        self.__fromDate: datetime.date = from_date
        self.__toDate: datetime.date = to_date
        self.__setIndicator(a_df)

    def __setIndicator(self, a_df: pandas.DataFrame, a: int = 12, b: int = 26, c: int = 9):
        df: pandas.DataFrame = a_df.copy()
        movingAverageFast: str = "MAfast{0}".format(str(a))
        movingAverageSlow: str = "MAslow{0}".format(str(b))
        signalStr: str = "Signal{0}".format(str(c))
        df[movingAverageFast] = df["Adj Close"].ewm(span=a, min_periods=a).mean()
        df[movingAverageSlow] = df["Adj Close"].ewm(span=b, min_periods=b).mean()
        df["MACD"] = df[movingAverageFast] - df[movingAverageSlow]
        df[signalStr] = df["MACD"].ewm(span=c, min_periods=c).mean()
        df.dropna(inplace=True)
        self.IndicatorDf = df
