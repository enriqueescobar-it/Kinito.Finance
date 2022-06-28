import json
from datetime import datetime, timedelta

from backports.zoneinfo import ZoneInfo
from prettytable import PrettyTable
from typing import List

from Common.InfoType.AbstractInfo import AbstractInfo
from Common.InfoType.QuarterInfo import QuarterInfo


class DateTimeInfo(AbstractInfo):
    __header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))
    _qi_list: List[QuarterInfo] = []
    _current_qi: QuarterInfo
    _previous_qi: QuarterInfo

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))):
        self._d_t = d_t
        self._current_qi = QuarterInfo(d_t)
        self._previous_qi = QuarterInfo(self._current_qi.StartDateTime - timedelta(days=5))
        self._qi_list.append(self._previous_qi)

    def __str__(self) -> str:
        self._pretty_table.field_names = self.__header
        self._pretty_table.add_row(['Length', len(self._qi_list)])
        return self._pretty_table.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            "len": len(self._qi_list)
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
