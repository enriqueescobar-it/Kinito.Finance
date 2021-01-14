from Common.StockType.Funds.AbstractStockFund import AbstractStockFund


class ExchangeTradedFund(AbstractStockFund):
    #_class: str = 'NA'

    def __init__(self):
        self.__class = 'Etf'

    def __str__(self):
        return self.__class
