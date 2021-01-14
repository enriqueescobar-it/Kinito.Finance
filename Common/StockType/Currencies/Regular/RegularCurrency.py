from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency


class RegularCurrency(AbstractCurrency):

    def __init__(self):
        self.__class = 'Regular'

    def __str__(self):
        return self.__class
