from Common.StockType.AbstractStock import AbstractStock


class AbstractStockFuture(AbstractStock):

    def __init__(self):
        self.__class = 'Future'

    def __str__(self):
        return self.__class
