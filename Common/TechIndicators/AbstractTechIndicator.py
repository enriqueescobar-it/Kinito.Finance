from abc import *
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class AbstractTechIndicator(ABC):
    _label: str = 'Indicator'
    _col: str
    __src: str

    def __init__(self, y_stock_option: YahooStockOption):
        self.__src = y_stock_option.Source
        self._col = 'Adj Close' if self.__src == 'yahoo' else 'Close'

    def GetCol(self):
        return self._col

    def GetLabel(self):
        return self._label
