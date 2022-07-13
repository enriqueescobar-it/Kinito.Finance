from datetime import datetime, timedelta

from prettytable import PrettyTable

from Common.InfoType.Times.AbstractTimeInfo import AbstractTimeInfo


class AbstractTimeSpanInfo(AbstractTimeInfo):
    __pretty_table: PrettyTable = PrettyTable()
    _start_dt: datetime = datetime.now()
    _delta_days: int = 0
    _delta_hours: float = 0.00000
    _delta_minutes: float = 0.00000
    _delta_seconds: int = 0

    def __init__(self, date_time_start: datetime, date_time_stop: datetime = datetime.now()) -> None:
        super().__init__(date_time_stop)
        self._start_dt = date_time_start
        delta_datetime: timedelta = self.start_datetime - self.stop_datetime
        self._delta_days = delta_datetime.days
        self._delta_hours = round(delta_datetime.seconds/60/60, 4)
        self._delta_minutes = round(delta_datetime.seconds/60, 4)
        self._delta_seconds = delta_datetime.seconds

    def __str__(self) -> str:
        self.__pretty_table.field_names = self._header
        self.__pretty_table.add_row(['DateTimeStart', self._start_dt])
        self.__pretty_table.add_row(['DateTimeStop', self._stop_dt])
        self.__pretty_table.add_row(['DayCount', self._delta_days])
        self.__pretty_table.add_row(['HourCount', self._delta_hours])
        self.__pretty_table.add_row(['MinuteCount', self._delta_minutes])
        self.__pretty_table.add_row(['SecondCount', self._delta_seconds])
        return self.__pretty_table.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "date_time_start": str(self._start_dt),
            "date_time_stop": str(self._stop_dt),
            "delta_days": self._delta_days,
            "delta_hours": self._delta_hours,
            "delta_minutes": self._delta_minutes,
            "delta_seconds": self._delta_seconds
        }.items()

    @property
    def start_datetime(self) -> datetime:
        return self._start_dt
