import json

from datetime import datetime, timezone, timedelta, tzinfo
from backports.zoneinfo import ZoneInfo
from fiscalyear import FiscalDateTime, FiscalQuarter
from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo


class QuarterInfo(AbstractInfo):
    __header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _fdt: FiscalDateTime = FiscalDateTime(2001, 9, 11, 0, 0, 0, 0, tzinfo=ZoneInfo("America/Toronto"))
    _current_dt: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))
    _current_dt_zi: ZoneInfo = ZoneInfo("America/Toronto")
    _current_dt_day: int = 11
    _current_dt_day_th: int = 0
    _current_dt_week_th: int = 0
    _current_dt_month: int = 9
    _current_dt_year: int = 2001
    _current_dt_q: int = 3
    _current_dt_q_num: str = 'Q3'
    _current_dt_quarter: str = '2001Q3'
    _current_quarter: FiscalQuarter = FiscalQuarter(2001, 3)
    _previous_quarter: FiscalQuarter = _fdt.prev_fiscal_quarter
    _previous_dt: datetime = _current_dt
    _base_quarter: FiscalQuarter = FiscalQuarter(2001, 3)
    _base_dt: datetime = _current_dt

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))):
        self._current_dt = d_t
        self._fdt = FiscalDateTime(d_t.year, d_t.month, d_t.day, d_t.hour, d_t.minute,
                                   d_t.second, d_t.microsecond, tzinfo=d_t.tzinfo)
        self._current_dt_day = d_t.day
        self._current_dt_day_th = self._fdt.fiscal_day
        self._current_dt_week_th = d_t.isocalendar()[1]
        self._current_dt_month = d_t.month
        self._current_dt_year = self._fdt.fiscal_year
        self._current_dt_q = self._fdt.fiscal_quarter
        self._current_dt_q_num = 'Q' + str(self._current_dt_q)
        self._current_dt_quarter = str(self._fdt.fiscal_year) + self._current_dt_q_num
        self._current_quarter = FiscalQuarter(self._fdt.fiscal_year, self._fdt.fiscal_quarter)
        self._previous_quarter = self._fdt.prev_fiscal_quarter
        self._previous_dt_day = self._previous_quarter.start.day
        self._previous_dt_day_th = self._previous_quarter.start.fiscal_day
        self._previous_dt_week_th = self._previous_quarter.start.date().isocalendar()[1]
        self._previous_dt_month = self._previous_quarter.start.month
        self._previous_dt_year = self._previous_quarter.start.year
        self._previous_dt = datetime(self._previous_quarter.start.year, self._previous_quarter.start.month,
                                     self._previous_quarter.start.day)
        self._previous_dt_q = self._previous_quarter.fiscal_quarter
        self._previous_dt_q_num = 'Q' + str(self._previous_dt_q)
        self._previous_dt_quarter = str(self._previous_quarter.fiscal_year) + self._previous_dt_q_num

    def __str__(self) -> str:
        self._pretty_table.field_names = self.__header
        self._pretty_table.add_row(['CurrentDay', self._current_dt_day])
        self._pretty_table.add_row(['CurrentDayTh', self._current_dt_day_th])
        self._pretty_table.add_row(['CurrentWeekTh', self._current_dt_week_th])
        self._pretty_table.add_row(['CurrentMonth', self._current_dt_month])
        self._pretty_table.add_row(['CurrentYear', self._current_dt_year])
        self._pretty_table.add_row(['CurrentQ', self._current_dt_q])
        self._pretty_table.add_row(['CurrentQNumber', self._current_dt_q_num])
        self._pretty_table.add_row(['CurrentQuarter', self._current_dt_quarter])
        self._pretty_table.add_row(['CurrentFiscalQuarter', self._current_quarter])
        return self._pretty_table.__str__()

    def set_baseline(self, base_years: int = 5):
        self._base_quarter =\
            FiscalQuarter(self._current_quarter.fiscal_year - 4 * base_years, self._current_quarter.fiscal_quarter)
        self._base_dt = datetime(self._base_quarter.start.year, self._base_quarter.start.month,
                                     self._base_quarter.start.day)
