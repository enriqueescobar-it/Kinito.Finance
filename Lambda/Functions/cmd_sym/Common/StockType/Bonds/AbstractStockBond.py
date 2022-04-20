from Common.StockType.AbstractStock import AbstractStock


class AbstractStockBond(AbstractStock):
    __ticker: str = 'NA'
    _name: str = 'NA'

    def __init__(self, c_name: str, t_name: str):
        self._name = c_name.replace(' ', '')
        self.__ticker = t_name
        self.__class = 'Bond'
        self._pretty_table.add_row(['type', self.__class])
        self._pretty_table.add_row(['name', self._name])

    def __str__(self):
        return self._pretty_table.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "type": self.__class,
            "name": self._name
        }.items()

    @property
    def InfoList(self):
        return self._info_list

    @property
    def InfoLabels(self):
        return self._info_labels

    @property
    def Name(self):
        return self._name
