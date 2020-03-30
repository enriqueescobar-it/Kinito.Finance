from typing import List, Any, Union

from alpha_vantage.timeseries import TimeSeries
import Data.Yahoo.YahooTicker as YahooTicker


class AlphaVantageManager(object):
    """description of class"""
    PandasTimeSeries: TimeSeries
    column_names: List[str] = ["open", "high", "low", "close", "volume"]
    min_s: str = "min"

    def __init__(self, a_key: str, y_ticker: YahooTicker):
        self.__alphaK: str = a_key
        self.PandasTimeSeries = TimeSeries(key=open(a_key, 'r').read(), output_format='pandas')
        self.__ticker = y_ticker

    def GetIntraDayMinuteSparse(self, a_int: int):
        s_int = str(a_int) + self.min_s
        a_df = self.PandasTimeSeries.get_intraday(symbol=self.__ticker.TickerName, interval=s_int, outputsize='full')[0]
        a_df.columns = self.column_names
        return a_df
