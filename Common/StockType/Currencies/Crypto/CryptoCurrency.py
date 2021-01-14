from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency


class CryptoCurrency(AbstractCurrency):

    def __init__(self):
        self.__class = 'Crypto'

    def __str__(self):
        return self.__class
