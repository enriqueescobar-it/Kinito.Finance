from datetime import datetime
from dateutil.relativedelta import relativedelta
from pandas import DataFrame
from pandas_datareader import data
from Common.Readers.Engine.AbstractPandaEngine import AbstractPandaEngine


class YahooPandaEngine(AbstractPandaEngine):
    _source: str = 'yahoo'
    _df: DataFrame = DataFrame()

    def __init__(self, a_ticker: str = 'AAPL', a_dt: datetime = datetime.now()) -> None:
        self._df = data.DataReader(a_ticker, start=a_dt - relativedelta(months=6), end=a_dt, data_source=self._source)
        self._df = self._df.dropna(inplace=True)
        print(self._df.head())
        print(self._df.tail())
