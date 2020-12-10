from abc import *
from pandas import DataFrame


class AbstractStockOption(ABC):
    Source: str = ''
    _data: DataFrame

    def getData(self) -> DataFrame:
        return self._data

    @property
    def Data(self):
        return self._data
