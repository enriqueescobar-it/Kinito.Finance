from Common.StockType.AbstractStock import AbstractStock


class AbstractStockFund(AbstractStock):
    _info_labels: list = list()
    _info_list: list = list()
    _name: str = 'NA'

    def __init__(self, c_name: str):
        self.__class = 'Fund'
        self._name = c_name.replace(' ', '')

    def __str__(self):
        return self._pretty_table.__str__()

    def __repr__(self):
        return self.__str__()

    @property
    def InfoList(self):
        return self._info_list

    @property
    def InfoLabels(self):
        return self._info_labels

    @property
    def Name(self):
        return self._name
