from abc import ABC
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class AbstractTechIndicator(ABC):
    _Label: str
    _Col: str
    __src: str

    def __init__(self, y_stock_option: YahooStockOption):
        self.__src = y_stock_option.Source
        self._Col = 'Adj Close' if self.__src == 'yahoo' else 'Close'
