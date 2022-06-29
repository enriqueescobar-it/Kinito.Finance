import json

from datetime import datetime, timedelta

from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo


class TimeSpanInfo(AbstractInfo):

    __header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()

    def __init__(self):
        pass

    def __str__(self) -> str:
        self._pretty_table.field_names = self.__header
        return self._pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1]
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
