from abc import *
import json
from prettytable import PrettyTable


class AbstractStock(ABC):
    __class: str = 'NA'
    _pretty_table: PrettyTable = PrettyTable()
    _info_labels: list = list()
    _info_list: list = list()

    def __init__(self):
        self.__class = 'StockInfo'
        self._pretty_table.add_column('Labels', self._info_labels)
        self._pretty_table.add_column(self.__class, self._info_list)

    def __str__(self):
        return self._pretty_table.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "type": self.__class
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
