from abc import *
import json
from prettytable import PrettyTable


class AbstractStock(ABC):
    __class: str = 'NA'
    _pretty_table: PrettyTable = PrettyTable()

    def __init__(self):
        self.__class = 'Stock'

    def __str__(self):
        return self.__class

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "type": self.__class
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)