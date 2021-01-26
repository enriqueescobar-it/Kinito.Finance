from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency


class CryptoCurrency(AbstractCurrency):

    def __init__(self, c_name: str, t_name: str):
        super().__init__(c_name.replace(' ', '').replace('-', ''))
        self.__class = 'Crypto'
