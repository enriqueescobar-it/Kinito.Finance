from datetime import date
from pandas import DataFrame
from pandas_datareader import get_data_yahoo
import DataReaders.YahooTicker as YahooTicker

class YahooPdrManager(object):
    """description of class"""
    DateTo: date
    DateFrom: date
    YahooData: DataFrame
    YahooDailyReturn: DataFrame

    def __init__(self, yahoo_ticker: YahooTicker, from_date: date, to_date: date, y_data=None):
        self.DateTo = to_date
        self.DateFrom = from_date
        self.__ticker = yahoo_ticker
        if y_data is None:
            gdy = get_data_yahoo(self.__ticker.TickerName, from_date, to_date)
            gdy.dropna(inplace=True)
            self.YahooData = gdy
        else:
            self.YahooData = y_data
        self.__updateDailyReturn()

    def __updateDailyReturn(self):
        self.YahooDailyReturn = self.YahooData.pct_change()

    def FillNaWithNextValue(self):
        self.YahooData.fillna(method='bfill', axis=0, inplace=True)
        self.__updateDailyReturn()

    def DropRowsWithNan(self):
        self.YahooData.dropna(how='any', axis=0, inplace=True)
        self.__updateDailyReturn()
