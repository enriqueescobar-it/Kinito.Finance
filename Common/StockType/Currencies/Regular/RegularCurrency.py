from prettytable import PrettyTable

from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency


class RegularCurrency(AbstractCurrency):
    __pretty_table: PrettyTable = PrettyTable()

    def __init__(self, c_name: str):
        self.__class = 'Regular'
        self._name = c_name.replace(' ', '')
        self._info_labels.append('Name')
        self._info_list.append(self._name)
        self.__pretty_table.add_column('Labels', self.InfoLabels)
        self.__pretty_table.add_column(self.__class, self.InfoList)

    def __str__(self):
        return self.__pretty_table.__str__()
