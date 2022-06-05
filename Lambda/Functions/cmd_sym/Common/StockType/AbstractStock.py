import json
from abc import *

from pandas import DataFrame
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

    def __is_any_valid(self, a_any: any, a_str: str) -> bool:
        return any(a_any) and not (("summaryTypes=" + a_str) in str(a_any))

    def _get_df_valid(self, a_any: any, a_str: str) -> (bool, DataFrame):
        boo: bool = self.__is_any_valid(a_any, a_str)
        return (boo, a_any) if boo else (boo, DataFrame())

    def _get_df_available(self, a_any: any) -> (bool, DataFrame):
        boo: bool = not (" data unavailable for " in str(a_any))
        return (boo, a_any) if boo else (boo, DataFrame())

    def _get_dict_valid(self, a_dict: dict, a_str: str) -> (bool, dict):
        boo: bool = any(a_dict) and not(("summaryTypes=" + a_str) in str(a_dict))
        return (boo, a_dict) if boo else (boo, {})

    def _get_sub_dict(self, a_dict: dict, a_str: str) -> dict:
        return a_dict.get(a_str)

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
