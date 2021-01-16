from prettytable import PrettyTable

from Common.StockType.AbstractStock import AbstractStock


class AbstractStockFuture(AbstractStock):
    __pretty_table: PrettyTable = PrettyTable()
    _info_labels: list = list()
    _info_list: list = list()
    _name: str = 'NA'
    __ticker: str = 'NA'

    def __init__(self, c_name: str):
        self.__class = 'Future'
        self._name = c_name.replace(' ', '')
        self._info_labels.append('Name')
        self._info_list.append(self._name)
        self.__pretty_table.add_column('Labels', self.InfoLabels)
        self.__pretty_table.add_column(self.__class, self.InfoList)

    def __str__(self):
        return self.__pretty_table.__str__()

    @property
    def InfoList(self):
        return self._info_list

    @property
    def InfoLabels(self):
        return self._info_labels

    @property
    def Name(self):
        return self._name
