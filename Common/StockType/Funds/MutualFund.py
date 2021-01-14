from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


class MutualFund(AbstractStockFund):
    #_class: str = 'NA'

    def __init__(self):
        self.__class = 'Mutual'

    def __str__(self):
        return self.__class
