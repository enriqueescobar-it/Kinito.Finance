from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


class IndexFund(AbstractStockFund):
    #_class: str = 'NA'

    def __init__(self):
        self.__class = 'Index'

    def __str__(self):
        return self.__class
