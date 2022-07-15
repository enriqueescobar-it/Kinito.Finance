from datetime import datetime

from backports.zoneinfo import ZoneInfo
from fiscalyear import FiscalDateTime, FiscalQuarter, FiscalYear, FiscalMonth, FiscalDay, FiscalDate
from prettytable import PrettyTable

from Common.InfoType.Times.DateTimeInfo import DateTimeInfo
from Common.InfoType.Times.Spans.AbstractTimeSpanInfo import AbstractTimeSpanInfo


class QuarterSpanInfo(AbstractTimeSpanInfo):
    __pretty_table: PrettyTable = PrettyTable()
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

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))):
        super().__init__(date_time_start=d_t)
        dti: DateTimeInfo = DateTimeInfo(d_t)
        self._dt = dti.datetime
        self._dt_day = dti.datetime.day
        self._dt_f = dti.fiscal_datetime
        self._dt_day_th = dti.year_day
        self._dt_week_th = dti.year_week
        self._dt_month = dti.datetime.month
        self._dt_year = dti.datetime.year
        self._d_f = dti.fiscal_date
        #
        self._dt_day_f = dti.fiscal_day
        self._dt_month_f = dti.fiscal_month
        self._quarter_f = dti.fiscal_quarter
        self._dt_year_f = dti.fiscal_year
        self._quarter_int = dti.quarter_int
        self._quarter_str = dti.quarter_str
        self._quarter_string = dti.quarter_string
        self._start_dt = self.__get_quarter_fiscal_dt_start(dti)
        self._stop_dt = self.__get_quarter_fiscal_dt_stop(dti)

    def __str__(self) -> str:
        self.__pretty_table.field_names = self._header
        self.__pretty_table.add_row(['DateTime', self._dt])
        self.__pretty_table.add_row(['DateDay', self._dt_day])
        self.__pretty_table.add_row(['DateDayTh', self._dt_day_th])
        self.__pretty_table.add_row(['DateWeekTh', self._dt_week_th])
        self.__pretty_table.add_row(['DateMonth', self._dt_month])
        self.__pretty_table.add_row(['DateYear', self._dt_year])
        self.__pretty_table.add_row(['DateQ', self._quarter_int])
        self.__pretty_table.add_row(['DateQNumber', self._quarter_str])
        self.__pretty_table.add_row(['DateQuarter', self._quarter_string])
        self.__pretty_table.add_row(['FiscalDate', self._d_f])
        self.__pretty_table.add_row(['FiscalDateTime', self._dt_f])
        self.__pretty_table.add_row(['FiscalDay', str(self._dt_day_f)])
        self.__pretty_table.add_row(['FiscalMonth', str(self._dt_month_f)])
        self.__pretty_table.add_row(['FiscalQuarter', str(self._quarter_f)])
        self.__pretty_table.add_row(['FiscalYear', str(self._dt_year_f)])
        self.__pretty_table.add_row(['DateTimeStart', self._start_dt])
        self.__pretty_table.add_row(['DateTimeStop', self._stop_dt])
        return self.__pretty_table.__str__()

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
            "f_d": str(self._d_f),
            "f_dt": str(self._dt_f),
            "f_day": str(self._dt_day_f),
            "f_month": str(self._dt_month_f),
            "f_quarter": str(self._quarter_f),
            "f_year": str(self._dt_year_f),
            "date_time_start": str(self._start_dt),
            "date_time_stop": str(self._stop_dt)
        }.items()

    def __get_quarter_fiscal_dt_start(self, dti: DateTimeInfo) -> datetime:
        return datetime(dti.fiscal_quarter.start.year, dti.fiscal_quarter.start.month, dti.fiscal_quarter.start.day)

    def __get_quarter_fiscal_dt_stop(self, dti: DateTimeInfo) -> datetime:
        return datetime(dti.fiscal_quarter.end.year, dti.fiscal_quarter.end.month, dti.fiscal_quarter.end.day)

    @property
    def day(self) -> int:
        return self._dt_day
