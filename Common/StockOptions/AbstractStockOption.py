from abc import *
from pandas import DataFrame


class AbstractStockOption(ABC):
    _source: str = 'yahoo'
    _column: str = 'Adj Close'
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
