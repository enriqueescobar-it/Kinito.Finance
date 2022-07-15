import json
from datetime import datetime

from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo
from Common.InfoType.Times.DateTimeInfo import DateTimeInfo


class AbstractTimeInfo(AbstractInfo):
    __pretty_table: PrettyTable = PrettyTable()
    _header: list = ['Field', 'FieldInfo']
    _stop_dti: DateTimeInfo = DateTimeInfo(datetime.now())

    def __init__(self, date_time: datetime = datetime.now()) -> None:
        self._stop_dti = DateTimeInfo(date_time)

    def __str__(self) -> str:
        self.__pretty_table.field_names = self._header
        self.__pretty_table.add_row(['DateTime', self._stop_dti.datetime])
        return self.__pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "date_time": str(self._stop_dti.datetime)
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def stop_datetime_info(self) -> DateTimeInfo:
        return self._stop_dti

    @property
    def current_datetime_info(self) -> DateTimeInfo:
        return self._stop_dti
