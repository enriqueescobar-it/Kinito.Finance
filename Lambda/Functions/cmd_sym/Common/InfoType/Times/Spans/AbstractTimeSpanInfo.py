from datetime import datetime

from prettytable import PrettyTable

from Common.InfoType.Times.AbstractTimeInfo import AbstractTimeInfo


class AbstractTimeSpanInfo(AbstractTimeInfo):
    __pretty_table: PrettyTable = PrettyTable()
    _start_dt: datetime = datetime.now()

    def __init__(self, date_time_start: datetime, date_time_stop: datetime = datetime.now()) -> None:
        super().__init__(date_time_stop)
        self._start_dt = date_time_start

    def __str__(self) -> str:
        self.__pretty_table.field_names = self._header
        self.__pretty_table.add_row(['DateTimeStart', self._start_dt])
        self.__pretty_table.add_row(['DateTimeStop', self._stop_dt])
        return self.__pretty_table.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "date_time_start": str(self._start_dt),
            "date_time_stop": str(self._stop_dt)
        }.items()

    @property
    def start_datetime(self) -> datetime:
        return self._start_dt
