from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


class IndexFund(AbstractStockFund):

    def __init__(self):
        self.__class = 'Index'

    def __str__(self):
        return self.__class
