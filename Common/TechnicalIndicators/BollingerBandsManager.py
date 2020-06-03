import pandas


class BollingerBandsManager(object):
    """Bollinger Bands class manager"""
    IndicatorDf: pandas.DataFrame

    def __init__(self, a_df: pandas.DataFrame):
        self.__setIndicator(a_df)

    def __setIndicator(self, a_df: pandas.DataFrame, days_span: int = 20):
        """function to calculate Bollinger Bands"""
        movingAverageTitle: str = "MovingAverage{0}".format(str(days_span))
        df: pandas.DataFrame = a_df.copy()
        df[movingAverageTitle] = df['Adj Close'].rolling(days_span).mean()
        # ddof=0 is required since we want to take the standard deviation of the population and not sample
        df["BBup"] = df[movingAverageTitle] + 2 * df['Adj Close'].rolling(days_span).std(ddof=0)
        # ddof=0 is required since we want to take the standard deviation of the population and not sample
        df["BBdn"] = df[movingAverageTitle] - 2 * df['Adj Close'].rolling(days_span).std(ddof=0)
        df["BBwidth"] = df["BBup"] - df["BBdn"]
        df.dropna(inplace=True)
        self.IndicatorDf = df
