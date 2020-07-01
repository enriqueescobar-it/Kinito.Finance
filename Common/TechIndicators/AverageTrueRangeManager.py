import pandas

from Common.TechIndicators.AbstractIndicatorManager import AbstractIndicatorManager


class AverageTrueRangeManager(AbstractIndicatorManager):
    """Average True Range class manager"""
    IndicatorDf: pandas.DataFrame

    def __init__(self, a_df: pandas.DataFrame, days_span: int = 20):
        self.__setIndicator(a_df, days_span)

    def __setIndicator(self, a_df: pandas.DataFrame, days_span: int = 20):
        """function to calculate True Range and Average True Range"""
        df: pandas.DataFrame = a_df.copy()
        df['H-L'] = abs(df['High'] - df['Low'])
        df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))
        df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1))
        # some take average instead of max
        df['TrueRange'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
        df['AvgTrueRate'] = df['TrueRange'].rolling(days_span).mean()
        # some use exponential mean
        # df['AvgTrueRate'] = df['TrueRange'].ewm(span=days_span,adjust=False,min_periods=days_span).mean()
        # df = df.drop(['H-L', 'H-PC', 'L-PC'], axis=1) #
        self.IndicatorDf = df

    def getAvgTrueRange(self, a_df: pandas.DataFrame, days_span: int = 20):
        """function to calculate True Range and Average True Range"""
        df: pandas.DataFrame = a_df.copy()
        df['H-L'] = abs(df['High'] - df['Low'])
        df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))
        df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1))
        # some take average instead of max
        df['TrueRange'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
        df['AvgTrueRate'] = df['TrueRange'].rolling(days_span).mean()
        # some use exponential mean
        # df['AvgTrueRate'] = df['TrueRange'].ewm(span=days_span,adjust=False,min_periods=days_span).mean()
        # df = df.drop(['H-L', 'H-PC', 'L-PC'], axis=1) #
        return df
