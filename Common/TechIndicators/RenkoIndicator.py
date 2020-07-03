import pandas
from stocktrends import Renko

from Common.TechIndicators.AbstractIndicatorManager import AbstractIndicatorManager


class RenkoManager(AbstractIndicatorManager):
    """ Renko bricks manager class"""
    IndicatorDf: pandas.DataFrame

    def __init__(self, a_df: pandas.DataFrame):
        self.__setIndicator(a_df)

    def __setIndicator(self, a_df: pandas.DataFrame):
        """function to convert ohlc data into renko bricks"""
        df: pandas.DataFrame = a_df.copy()
        df.reset_index(inplace=True)
        df = df.iloc[:, [0, 1, 2, 3, 5, 6]]
        df.rename(columns={"Date": "date", "High": "high", "Low": "low", "Open": "open", "Adj Close": "close",
                           "Volume": "volume"}, inplace=True)
        ren = Renko(df)
        ren.brick_size = round(self.__getAvgTrueRange(a_df.copy(), 120)["AvgTrueRate"][-1], 0)
        # if get_bricks() does not work try using get_ohlc_data() instead
        # df2.get_bricks() error => using get_ohlc_data()
        # renkoDataFrame = df2.get_bricks()
        renDf: pandas.DataFrame = ren.get_ohlc_data()
        self.IndicatorDf = renDf

    def __getAvgTrueRange(self, a_df: pandas.DataFrame, days_span: int = 20):
        """function to calculate True Range and Average True Range"""
        df: pandas.DataFrame = a_df.copy()
        df['H-L'] = abs(df['High'] - df['Low'])
        df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))
        df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1))
        # some take average instead of max
        df['TrueRange'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
        df['AvgTrueRate'] = df['TrueRange'].rolling(days_span).mean()
        # some take average instead of max
        df['TrueRange'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
        df['AvgTrueRate'] = df['TrueRange'].rolling(days_span).mean()
        # some use exponential mean
        # df['AvgTrueRate'] = df['TrueRange'].ewm(span=days_span,adjust=False,min_periods=days_span).mean()
        # df = df.drop(['H-L', 'H-PC', 'L-PC'], axis=1) #
        return df
