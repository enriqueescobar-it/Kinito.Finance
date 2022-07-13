import calendar
import json
import math

import pytz

from datetime import datetime, date
from fiscalyear import FiscalDateTime
from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo


class DateTimeInfo(AbstractInfo):
    __pretty_table: PrettyTable = PrettyTable()
    _header: list = ['Field', 'FieldInfo']
    _dt: datetime = datetime.now()
    _date: date = _dt.date()
    _tz: pytz.timezone = pytz.timezone("America/Toronto")
    _quarter_int: int = 3
    _quarter_str: str = 'Q3'
    _quarter_string: str = '2001Q3'
    _fdt: FiscalDateTime = FiscalDateTime(2001, 9, 11)
    _year_week: int = 0
    _month_day: int = 0
    _week_day_int: int = 0
    _week_day_iso: int = 0
    _week_day_str: str = 'Sunday'
    _fiscal_year_day: int = 0

    def __init__(self, dt: datetime = datetime.now()) -> None:
        self._dt = dt
        self._date = dt.date()
        self._tz = self._set_timezone(dt)
        self._quarter_int = self._get_quarter_int(dt)
        self._quarter_str = self._get_quarter_str(dt)
        self._quarter_string = self._get_quarter_string(dt)
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
        self.__pretty_table.add_row(['TimeZone', self._tz])
        self.__pretty_table.add_row(['Date', self._date])
        self.__pretty_table.add_row(['QuarterInt', self._quarter_int])
        self.__pretty_table.add_row(['QuarterStr', self._quarter_str])
        self.__pretty_table.add_row(['QuarterString', self._quarter_string])
        self.__pretty_table.add_row(['YearWeek', self._year_week])
        self.__pretty_table.add_row(['MonthDay', self._month_day])
        self.__pretty_table.add_row(['WeekDayInt', self._week_day_int])
        self.__pretty_table.add_row(['WeekDayISO', self._week_day_iso])
        self.__pretty_table.add_row(['WeekDayStr', self._week_day_str])
        self.__pretty_table.add_row(['FiscalDateTime', self._fdt])
        self.__pretty_table.add_row(['FiscalYearDay', self._fiscal_year_day])
        return self.__pretty_table.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "date_time": str(self._dt),
            "time_zone": str(self._tz),
            "date": str(self._date),
            "quarter_int": str(self._quarter_int),
            "quarter_str": str(self._quarter_str),
            "quarter_string": str(self._quarter_string),
            "year_week": str(self._year_week),
            "month_day": str(self._month_day),
            "week_day_int": str(self._week_day_int),
            "week_day_iso": str(self._week_day_iso),
            "week_day_str": str(self._week_day_str),
            "fiscal_date_time": str(self._fdt),
            "fiscal_year_day": str(self._fiscal_year_day)
        }.items()

    def _get_fiscal_date_time(self, dt: datetime) -> FiscalDateTime:
        return FiscalDateTime(dt.year, dt.month, dt.day)

    def _get_quarter_int(self, dt: datetime) -> int:
        return math.ceil(dt.month/3)

    def _get_quarter_str(self, dt: datetime) -> str:
        return "Q" + str(self._get_quarter_int(dt))

    def _get_quarter_string(self, dt: datetime) -> str:
        return str(dt.year) + self._get_quarter_str(dt)

    def _set_timezone(self, dt: datetime) -> pytz.timezone:
        if dt.timetz() is None or dt.tzinfo is None:
            timezone: pytz.timezone = pytz.timezone("America/Toronto")
            self._dt = timezone.localize(dt)
            return timezone
        else:
            return dt.tzinfo

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def datetime(self) -> datetime:
        return self._dt

    @property
    def timezone(self) -> pytz.timezone:
        return self._tz

    @property
    def date(self) -> date:
        return self._date

    @property
    def quarter_int(self) -> int:
        return self._quarter_int

    @property
    def quarter_str(self) -> str:
        return self._quarter_str

    @property
    def quarter_string(self) -> str:
        return self._quarter_string

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
