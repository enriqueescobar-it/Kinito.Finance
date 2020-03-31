import datetime
import pandas


class MovingAverageConvergenceDivergenceManager(object):
    """ MACD indicator manager class"""
    MovingAverageConvergenceDivergenceDf: pandas.DataFrame

    def __init__(self, a_df: pandas.DataFrame, from_date: datetime.date, to_date: datetime.date):
        self.__fromDate: datetime.date = from_date
        self.__toDate: datetime.date = to_date
        self.__setIndicator(a_df)

    def __setIndicator(self, a_df: pandas.DataFrame, a: int = 12, b: int = 26, c: int = 9):
        df: pandas.DataFrame = a_df.copy()
        df["MA_Fast"] = df["Adj Close"].ewm(span=a, min_periods=a).mean()
        df["MA_Slow"] = df["Adj Close"].ewm(span=b, min_periods=b).mean()
        df["MACD"] = df["MA_Fast"] - df["MA_Slow"]
        df["Signal"] = df["MACD"].ewm(span=c, min_periods=c).mean()
        df.dropna(inplace=True)
        self.MovingAverageConvergenceDivergenceDf = df
