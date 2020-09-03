from abc import *
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class AbstractTechIndicator(ABC):
    _label: str = 'Indicator'
    _col: str
    _src: str == 'yahoo'

    def __init__(self, y_stock_option: YahooStockOption):
        self._src = y_stock_option.Source
        self._col = 'Adj Close' if self._src == 'yahoo' else 'Close'

    def GetCol(self):
        return self._col

    def GetLabel(self):
        return self._label

    def GetSource(self):
        return self._src
