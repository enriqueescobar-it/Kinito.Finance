import json
import math
from datetime import datetime

from backports.zoneinfo import ZoneInfo
from fiscalyear import FiscalDateTime, FiscalQuarter, FiscalYear, FiscalMonth, FiscalDay, FiscalDate
from prettytable import PrettyTable

from Common.InfoType.Times.AbstractTimeInfo import AbstractTimeInfo


class QuarterSpanInfo(AbstractTimeInfo):

    _header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _d_f: FiscalDate = FiscalDate(2001, 9, 11)
    _dt_f: FiscalDateTime = FiscalDateTime(2001, 9, 11)
    _dt_day_f: FiscalDay = FiscalDay(_dt_f.year, _dt_f.fiscal_day)
    _dt_month_f: FiscalMonth = FiscalMonth(2001, 9)
    _quarter_f: FiscalQuarter = FiscalQuarter(2001, 3)
    _dt_year_f: FiscalYear = FiscalYear(2001)
    _dt: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))
    _dt_day: int = 11
    _dt_day_th: int = 0
    _dt_week_th: int = 0
    _dt_month: int = 9
    _dt_year: int = 2001
    _quarter_int: int = 3
    _quarter_str: str = 'Q3'
    _quarter_string: str = '2001Q3'
    _quarter_dt_start: datetime = _dt
    _quarter_dt_stop: datetime = _dt

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))):
        self._dt = d_t
        self._dt_day = self._dt.day
        self._dt_f = self.__get_fiscal_date_time(self._dt)
        self._dt_day_th = self._dt_f.fiscal_day
        self._dt_week_th = self._dt.isocalendar()[1]
        self._dt_month = self._dt.month
        self._dt_year = self._dt.year
        self._d_f = self.__get_fiscal_date(self._dt)
        #
        self._dt_day_f = self.__get_fiscal_day(self._dt, self._dt_f)
        self._dt_month_f = self.__get_fiscal_month(self._dt)
        self._quarter_f = self.__get_fiscal_quarter(self._dt)
        self._dt_year_f = self.__get_fiscal_year(self._dt)
        self._quarter_int = self.__get_quarter_int(self._dt)
        self._quarter_str = self.__get_quarter_str(self._dt)
        self._quarter_string = self.__get_quarter_string(self._dt)
        self._quarter_dt_start = self.__get_quarter_fiscal_dt_start(self._dt)
        self._quarter_dt_stop = self.__get_quarter_fiscal_dt_stop(self._dt)

    def __str__(self) -> str:
        self._pretty_table.field_names = self._header
        self._pretty_table.add_row(['DateTime', self._dt])
        self._pretty_table.add_row(['DateDay', self._dt_day])
        self._pretty_table.add_row(['DateDayTh', self._dt_day_th])
        self._pretty_table.add_row(['DateWeekTh', self._dt_week_th])
        self._pretty_table.add_row(['DateMonth', self._dt_month])
        self._pretty_table.add_row(['DateYear', self._dt_year])
        self._pretty_table.add_row(['DateQ', self._quarter_int])
        self._pretty_table.add_row(['DateQNumber', self._quarter_str])
        self._pretty_table.add_row(['DateQuarter', self._quarter_string])
        self._pretty_table.add_row(['DateQuarterStart', self._quarter_dt_start])
        self._pretty_table.add_row(['DateQuarterStop', self._quarter_dt_stop])
        self._pretty_table.add_row(['FiscalDate', self._d_f])
        self._pretty_table.add_row(['FiscalDateTime', self._dt_f])
        self._pretty_table.add_row(['FiscalDay', str(self._dt_day_f)])
        self._pretty_table.add_row(['FiscalMonth', str(self._dt_month_f)])
        self._pretty_table.add_row(['FiscalQuarter', str(self._quarter_f)])
        self._pretty_table.add_row(['FiscalYear', str(self._dt_year_f)])
        return self._pretty_table.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "dt": str(self._dt),
            "dt_day": self._dt_day,
            "dt_day_th": self._dt_day_th,
            "dt_week_th": self._dt_week_th,
            "dt_month": self._dt_month,
            "dt_year": self._dt_year,
            "quarter_int": self._quarter_int,
            "quarter_str": self._quarter_str,
            "quarter_string": self._quarter_string,
            "quarter_dt_start": str(self._quarter_dt_start),
            "quarter_dt_stop": str(self._quarter_dt_stop),
            "f_d": str(self._d_f),
            "f_dt": str(self._dt_f),
            "f_day": str(self._dt_day_f),
            "f_month": str(self._dt_month_f),
            "f_quarter": str(self._quarter_f),
            "f_year": str(self._dt_year_f)
        }.items()

    def __get_fiscal_date(self, dt: datetime) -> FiscalDate:
        return FiscalDate(dt.year, dt.month, dt.day)

    def __get_fiscal_date_time(self, dt: datetime) -> FiscalDateTime:
        return FiscalDateTime(dt.year, dt.month, dt.day)

    def __get_fiscal_day(self, dt: datetime, fdt: FiscalDateTime) -> FiscalDay:
        return FiscalDay(dt.year, fdt.fiscal_day)

    def __get_fiscal_month(self, dt: datetime) -> FiscalMonth:
        return FiscalMonth(dt.year, dt.month)

    def __get_fiscal_quarter(self, dt: datetime) -> FiscalQuarter:
        fdt: FiscalDateTime = FiscalDateTime(dt.year, dt.month, dt.day)
        return FiscalQuarter(fdt.year, fdt.fiscal_quarter)

    def __get_fiscal_year(self, dt: datetime) -> FiscalYear:
        return FiscalYear(dt.year)

    def __get_quarter_int(self, dt: datetime) -> int:
        return math.ceil(dt.month/3)

    def __get_quarter_str(self, dt: datetime) -> str:
        return "Q" + str(self.__get_quarter_int(dt))

    def __get_quarter_string(self, dt: datetime) -> str:
        return str(dt.year) + self.__get_quarter_str(dt)

    def __get_quarter_fiscal_dt_start(self, dt: datetime) -> datetime:
        fq: FiscalQuarter = self.__get_fiscal_quarter(dt)
        return datetime(fq.start.year, fq.start.month, fq.start.day)

    def __get_quarter_fiscal_dt_stop(self, dt: datetime) -> datetime:
        fq: FiscalQuarter = self.__get_fiscal_quarter(dt)
        return datetime(fq.end.year, fq.end.month, fq.end.day)

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    @property
    def day(self) -> int:
        return self._dt_day

    @property
    def date_time_start(self) -> datetime:
        return self._quarter_dt_start

    @property
    def date_time_stop(self) -> datetime:
        return self._quarter_dt_stop
