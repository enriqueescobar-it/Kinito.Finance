from abc import *
from pandas import DataFrame
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class AbstractTechIndicator(ABC):
    _col: str
    _label: str = 'Indicator'
    _name: str
    _src: str == 'yahoo'
    _data: DataFrame = DataFrame()

    def __init__(self, y_stock_option: YahooStockOption):
        self._src = y_stock_option.Source
        self._col = 'Adj Close' if self._src == 'yahoo' else 'Close'

    def GetCol(self):
        return self._col

    def GetData(self):
        return self._data

    def GetLabel(self):
        return self._label

    def GetName(self):
        return self._name

    def GetSource(self):
        return self._src
