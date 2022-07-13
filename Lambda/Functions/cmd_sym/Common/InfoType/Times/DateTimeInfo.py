import calendar
import json
from datetime import datetime

from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo


class DateTimeInfo(AbstractInfo):
    __pretty_table: PrettyTable = PrettyTable()
    _header: list = ['Field', 'FieldInfo']
    _dt: datetime = datetime.now()
    _year_week: int = 0
    _month_day: int = 0
    _week_day_int: int = 0
    _week_day_iso: int = 0
    _week_day_str: str = 'Sunday'

    def __init__(self, dt: datetime = datetime.now()) -> None:
        self._dt = dt
        self._year_week = dt.isocalendar()[1]
        self._month_day = dt.day
        self._week_day_int = dt.weekday()
        self._week_day_iso = dt.isocalendar()[2]
        self._week_day_str = calendar.day_name[dt.weekday()]

    def __str__(self) -> str:
        self.__pretty_table.field_names = self._header
        self.__pretty_table.add_row(['DateTime', self._dt])
        self.__pretty_table.add_row(['YearWeek', self._year_week])
        self.__pretty_table.add_row(['MonthDay', self._month_day])
        self.__pretty_table.add_row(['WeekDayInt', self._week_day_int])
        self.__pretty_table.add_row(['WeekDayISO', self._week_day_iso])
        self.__pretty_table.add_row(['WeekDayStr', self._week_day_str])
        return self.__pretty_table.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "date_time": str(self._dt),
            "year_week": str(self._year_week),
            "month_day": str(self._month_day),
            "week_day_int": str(self._week_day_int),
            "week_day_iso": str(self._week_day_iso),
            "week_day_str": str(self._week_day_str)
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def datetime(self) -> datetime:
        return self._dt

    @property
    def month_day(self) -> int:
        return self._month_day

    @property
    def week_day_int(self) -> int:
        return self._week_day_int

    @property
    def week_day_iso(self) -> int:
        return self._week_day_iso

    @property
    def week_day_str(self) -> str:
        return self._week_day_str
