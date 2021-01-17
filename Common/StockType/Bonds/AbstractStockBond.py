from prettytable import PrettyTable

from Common.StockType.AbstractStock import AbstractStock


class AbstractStockBond(AbstractStock):
    _info_labels: list = list()
    _info_list: list = list()
    _name: str = 'NA'
    _pretty_table: PrettyTable = PrettyTable()

    def __init__(self, c_name: str):
        self.__class = 'Bond'
        self._name = c_name
        self._info_labels.append('Name')
        self._info_list.append(self._name)
        self._pretty_table.add_column('Labels', self.InfoLabels)
        self._pretty_table.add_column(self.__class, self.InfoList)

    def __str__(self):
        return self._pretty_table.__str__()

    @property
    def InfoList(self):
        return self._info_list

    @property
    def InfoLabels(self):
        return self._info_labels

    @property
    def Name(self):
        return self._name
