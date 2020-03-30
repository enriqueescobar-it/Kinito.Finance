import datetime

from alpha_vantage.timeseries import TimeSeries
from pandas import DataFrame
from pandas_datareader import get_data_yahoo

import Data.DateTime.PyDateTimes as PyDays


class YahooTicker(object):
    """description of class"""
    TickerName: str
    StockName: str
    DateTimeToStr: str
    DateTimeFromStr: str
    DateTimeFrom: datetime
    DateTimeTo: datetime
    PdrDf: DataFrame

    # Class Attribute
    YType: str = "yahoo_ticker"

    def __init__(self, stock_n: str = 'NYSE', ticker_n: str = '', from_week: int = 0, to_week: int = 0):
        self.__setToDate(PyDays.DateTimeWeeksAgo(to_week))
        self.__setFromDate(PyDays.DateTimeWeeksAgo(from_week))
        self.StockName: str = stock_n
        self.TickerName: str = ticker_n
        assert isinstance(ticker_n, str)
        if ticker_n != '' and ticker_n.strip() != '':
            self.__setPdrDf(from_week, to_week)
        else:
            self.PdrDf = DataFrame()

    def __setToDate(self, a_date: datetime):
        self.DateTimeTo = a_date
        self.DateTimeToStr = self.DateTimeTo.strftime('%Y-%m-%d')

    def __setFromDate(self, a_date: datetime):
        self.DateTimeFrom = a_date
        self.DateTimeFromStr = self.DateTimeFrom.strftime('%Y-%m-%d')

    def __setPdrDf(self, from_week: int, to_week: int):
        self.__setToDate(PyDays.DateTimeWeeksAgo(to_week))
        self.__setFromDate(PyDays.DateTimeWeeksAgo(from_week))
        a_df = get_data_yahoo(self.TickerName, self.DateTimeFrom, self.DateTimeTo)
        a_df.dropna(inplace=True)
        self.PdrDf = a_df

    @property
    def full_name(self):
        return self.YType + ":" + self.StockName + " " + self.TickerName

    @property
    def __str__(self):
        return self.PdrDf.head()

    @property
    def __repr__(self):
        return self.PdrDf.head().__class__.__name__
