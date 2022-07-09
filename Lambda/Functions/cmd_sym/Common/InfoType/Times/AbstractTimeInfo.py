import json
from datetime import datetime

from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo


class AbstractTimeInfo(AbstractInfo):
    _stop_dt: datetime = datetime.now()
    _header: list = ['Field', 'FieldInfo']
    __pretty_table: PrettyTable = PrettyTable()

    def __init__(self, date_time: datetime = datetime.now()) -> None:
        self._stop_dt = date_time

    def __str__(self) -> str:
        self.__pretty_table.field_names = self._header
        self.__pretty_table.add_row(['DateTime', self._stop_dt])
        return self.__pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "date_time": str(self._stop_dt)
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def stop_datetime(self) -> datetime:
        return self._stop_dt

    @property
    def current_datetime(self) -> datetime:
        return self._stop_dt
