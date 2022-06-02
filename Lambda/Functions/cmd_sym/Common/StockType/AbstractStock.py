from abc import *
import json
from prettytable import PrettyTable


class AbstractStock(ABC):
    __class: str = 'NA'
    _quote_type: str = 'NA'
    _header: list = ['Info', 'TypeInfo']

    def __init__(self):
        self.__class = 'TypeInfo'

    def __str__(self):
        pt: PrettyTable = PrettyTable()
        pt.field_names = self._header
        return pt.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            "Info": self.__class
        }.items()

    def is_dict_valid(self, a_dict: dict, a_str: str):
        str_subs = "summaryTypes=" + a_str
        str_dict = str(a_dict)
        boo: bool = any(a_dict) and not(str_subs in str_dict)
        if boo:
            return boo, a_dict
        else:
            return boo, {}

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
