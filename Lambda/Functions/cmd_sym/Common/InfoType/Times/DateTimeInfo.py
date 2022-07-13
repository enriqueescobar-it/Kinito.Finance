import calendar
import json
from datetime import datetime

from fiscalyear import FiscalDateTime
from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo


class DateTimeInfo(AbstractInfo):
    __pretty_table: PrettyTable = PrettyTable()
    _header: list = ['Field', 'FieldInfo']
    _dt: datetime = datetime.now()
    _fdt: FiscalDateTime = FiscalDateTime(2001, 9, 11)
    _year_week: int = 0
    _month_day: int = 0
    _week_day_int: int = 0
    _week_day_iso: int = 0
    _week_day_str: str = 'Sunday'
    _fiscal_year_day: int = 0

    def __init__(self, dt: datetime = datetime.now()) -> None:
        self._dt = dt
        self._fdt = self._get_fiscal_date_time(dt)
        self._year_week = dt.isocalendar()[1]
        self._month_day = dt.day
        self._week_day_int = dt.weekday()
        self._week_day_iso = dt.isocalendar()[2]
        self._week_day_str = calendar.day_name[dt.weekday()]
        self._fiscal_year_day = self._fdt.fiscal_day

    def __str__(self) -> str:
        self.__pretty_table.field_names = self._header
        self.__pretty_table.add_row(['DateTime', self._dt])
        self.__pretty_table.add_row(['FiscalDateTime', self._fdt])
        self.__pretty_table.add_row(['YearWeek', self._year_week])
        self.__pretty_table.add_row(['MonthDay', self._month_day])
        self.__pretty_table.add_row(['WeekDayInt', self._week_day_int])
        self.__pretty_table.add_row(['WeekDayISO', self._week_day_iso])
        self.__pretty_table.add_row(['WeekDayStr', self._week_day_str])
        self.__pretty_table.add_row(['FiscalYearDay', self._fiscal_year_day])
        return self.__pretty_table.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "date_time": str(self._dt),
            "fiscal_date_time": str(self._fdt),
            "year_week": str(self._year_week),
            "month_day": str(self._month_day),
            "week_day_int": str(self._week_day_int),
            "week_day_iso": str(self._week_day_iso),
            "week_day_str": str(self._week_day_str),
            "fiscal_year_day": str(self._fiscal_year_day)
        }.items()

    def _get_fiscal_date_time(self, dt: datetime) -> FiscalDateTime:
        return FiscalDateTime(dt.year, dt.month, dt.day)

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def datetime(self) -> datetime:
        return self._dt

    @property
    def fiscal_datetime(self) -> FiscalDateTime:
        return self._fdt

    @property
    def year_week(self) -> int:
        return self._year_week

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

    @property
    def fiscal_year_day(self) -> int:
        return self._fiscal_year_day
