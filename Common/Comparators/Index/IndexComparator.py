from Common.Comparators.Index.AbstractIndexComparator import AbstractIndexComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class IndexComparator(AbstractIndexComparator):
    __stockOption: YahooStockOption

    def __init__(self, stock_option: YahooStockOption, indices: list()):
        self.__stockOption = stock_option
