from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


class IndexFund(AbstractStockFund):

    def __init__(self, c_name: str):
        super().__init__(c_name.replace(' ', ''))
        self.__class = 'Index'

    def __str__(self):
        return self.__class
