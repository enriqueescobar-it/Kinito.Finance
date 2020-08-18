from Common.Comparators.Index.AbstractIndexComparer import AbstractIndexComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class IndexComparer(AbstractIndexComparator):
    __stockOption: YahooStockOption

    def __init__(self, stock_option: YahooStockOption, indices):
        self.__stockOption = stock_option
