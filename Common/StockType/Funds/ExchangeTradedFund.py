from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


class ExchangeTradedFund(AbstractStockFund):

    def __init__(self):
        self.__class = 'Etf'

    def __str__(self):
        return self.__class
