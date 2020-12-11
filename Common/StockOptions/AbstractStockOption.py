from abc import *
from pandas import DataFrame
from Common.Measures.Time.TimeSpan import TimeSpan


class AbstractStockOption(ABC):
    _source: str = 'yahoo'
    _column: str = 'Adj Close'
    _ticker: str = 'TD'
    TimeSpan: TimeSpan
    _data: DataFrame

    def getData(self) -> DataFrame:
        return self._data

    @property
    def Column(self):
        return self._column

    @property
    def Data(self):
        return self._data

    @property
    def Source(self):
        return self._source

    @property
    def Ticker(self):
        return self._ticker

    @property
    def T(self):
        return self.TimeSpan
