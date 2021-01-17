from prettytable import PrettyTable

from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency


class CryptoCurrency(AbstractCurrency):
    __pretty_table: PrettyTable = PrettyTable()

    def __init__(self, c_name: str):
        super().__init__(c_name.replace(' ', '').replace('-', '|'))
        self.__class = 'Crypto'
        self.__pretty_table.add_column('Labels', self.InfoLabels)
        self.__pretty_table.add_column(self.__class, self.InfoList)

    def __str__(self):
        return self.__pretty_table.__str__()
