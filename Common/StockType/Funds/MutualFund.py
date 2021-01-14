from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


class MutualFund(AbstractStockFund):

    def __init__(self):
        self.__class = 'Mutual'

    def __str__(self):
        return self.__class
