from abc import *
from pandas import DataFrame
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy


class AbstractTechIndicator(ABC):
    _col: str
    _label: str = 'Indicator'
    _name: str
    _src: str == 'yahoo'
    _data: DataFrame = DataFrame()
    _strategy: AbstractTechIndicatorStrategy

    def __init__(self, y_stock_option: YahooStockOption):
        self._src = y_stock_option.Source
        self._col = 'Adj Close' if self._src == 'yahoo' else 'Close'

    @abstractmethod
    def _setData(self, y_stock_option: YahooStockOption):
        pass

    def GetCol(self) -> str:
        return self._col

    def GetLabel(self) -> str:
        return self._label

    def GetName(self) -> str:
        return self._name

    def GetSource(self) -> str:
        return self._src

    def GetData(self) -> DataFrame:
        return self._data
