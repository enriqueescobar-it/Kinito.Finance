import json

import pandas as pd

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
    _current_dt_q_str: str = '2001Q3'
    _current_quarter: FiscalQuarter = FiscalQuarter(2001, 3)
    _previous_quarter: FiscalQuarter = FiscalQuarter(2001, 2)
    _previous_dt: datetime = _current_dt
    _previous_dt_q: int = 2
    _previous_dt_q_num: str = 'Q2'
    _previous_dt_q_str: str = '2001Q2'
    _base_quarter: FiscalQuarter = FiscalQuarter(2001, 3)
    _base_dt: datetime = _current_dt
    _base_dt_q: int = 3
    _base_dt_q_num: str = 'Q2'
    _base_dt_q_str: str = '2001Q2'
    _has_balance_sheets_df: bool = False
    _balance_sheets_df: pd.DataFrame = pd.DataFrame()
    _has_cashflows_df: bool = False
    _cashflows_df: pd.DataFrame = pd.DataFrame()

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))):
        self._current_dt = d_t
        self._fdt = FiscalDateTime(d_t.year, d_t.month, d_t.day, d_t.hour, d_t.minute,
                                   d_t.second, d_t.microsecond)
        self._current_dt_day = d_t.day
        self._current_dt_day_th = self._fdt.fiscal_day
        self._current_dt_week_th = d_t.isocalendar()[1]
        self._current_dt_month = d_t.month
        self._current_dt_year = self._fdt.fiscal_year
        self._current_dt_q = self._fdt.fiscal_quarter
        self._current_dt_q_num = 'Q' + str(self._current_dt_q)
        self._current_dt_q_str = str(self._fdt.fiscal_year) + self._current_dt_q_num
        self._current_quarter = FiscalQuarter(self._fdt.fiscal_year, self._fdt.fiscal_quarter)
        self._previous_quarter = self._fdt.prev_fiscal_quarter
        self._previous_dt_q = self._previous_quarter.fiscal_quarter
        self._previous_dt_q_num = 'Q' + str(self._previous_dt_q)
        self._previous_dt_q_str = str(self._previous_quarter.fiscal_year) + self._previous_dt_q_num
        self._previous_dt_day = self._previous_quarter.start.day
        self._previous_dt_day_th = self._previous_quarter.start.fiscal_day
        self._previous_dt_week_th = self._previous_quarter.start.date().isocalendar()[1]
        self._previous_dt_month = self._previous_quarter.start.month
        self._previous_dt_year = self._previous_quarter.start.year
        self._previous_dt = datetime(self._previous_quarter.start.year, self._previous_quarter.start.month,
                                     self._previous_quarter.start.day).replace(
            tzinfo=self._previous_quarter.start.tzinfo)
        self.set_baseline()

    def __str__(self) -> str:
        self._pretty_table.field_names = self.__header
        self._pretty_table.add_row(['CurrentDay', self._current_dt_day])
        self._pretty_table.add_row(['CurrentDayTh', self._current_dt_day_th])
        self._pretty_table.add_row(['CurrentWeekTh', self._current_dt_week_th])
        self._pretty_table.add_row(['CurrentMonth', self._current_dt_month])
        self._pretty_table.add_row(['CurrentYear', self._current_dt_year])
        self._pretty_table.add_row(['CurrentQ', self._current_dt_q])
        self._pretty_table.add_row(['CurrentQNumber', self._current_dt_q_num])
        self._pretty_table.add_row(['CurrentQuarter', self._current_dt_q_str])
        self._pretty_table.add_row(['CurrentFiscalQuarter', str(self._current_quarter)])
        self._pretty_table.add_row(['PreviousQ', self._previous_dt_q])
        self._pretty_table.add_row(['PreviousQNumber', self._previous_dt_q_num])
        self._pretty_table.add_row(['PreviousQuarter', self._previous_dt_q_str])
        self._pretty_table.add_row(['PreviousFiscalQuarter', str(self._previous_quarter)])
        self._pretty_table.add_row(['PreviousFiscalQuarterStart', self._previous_dt])
        self._pretty_table.add_row(['BaseQ', self._base_dt_q])
        self._pretty_table.add_row(['BaseQNumber', self._base_dt_q_num])
        self._pretty_table.add_row(['BaseQuarter', self._base_dt_q_str])
        self._pretty_table.add_row(['BaseFiscalQuarter', str(self._base_quarter)])
        self._pretty_table.add_row(['BaseFiscalQuarterStart', self._base_dt])
        self._pretty_table.add_row(['HasBalanceSheetDf', self._has_balance_sheets_df])
        return self._pretty_table.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            "current_day": self._current_dt_day,
            "current_day_th": self._current_dt_day_th,
            "current_week_th": self._current_dt_week_th,
            "current_month": self._current_dt_month,
            "current_year": self._current_dt_year,
            "current_q": self._current_dt_q,
            "current_q_num": self._current_dt_q_num,
            "current_q_str": self._current_dt_q_str,
            "current_quarter": str(self._current_quarter),
            "previous_q": self._previous_dt_q,
            "previous_q_num": self._previous_dt_q_num,
            "previous_q_str": self._previous_dt_q_str,
            "previous_quarter": str(self._previous_quarter),
            "previous_quarter_start": str(self._previous_dt),
            "base_q": self._base_dt_q,
            "base_q_num": self._base_dt_q_num,
            "base_q_str": self._base_dt_q_str,
            "base_quarter": str(self._base_quarter),
            "base_quarter_start": str(self._base_dt),
            "has_balance_sheet_df": self._has_balance_sheets_df
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def set_baseline(self, base_years: int = 5):
        self._base_quarter = \
            FiscalQuarter(self._previous_quarter.fiscal_year - base_years, self._previous_quarter.fiscal_quarter)
        self._base_dt = datetime(self._base_quarter.start.year, self._base_quarter.start.month,
                                 self._base_quarter.start.day).replace(tzinfo=self._base_quarter.start.tzinfo)
        self._base_dt_q = self._base_quarter.fiscal_quarter
        self._base_dt_q_num = 'Q' + str(self._base_dt_q)
        self._base_dt_q_str = str(self._base_quarter.fiscal_year) + self._base_dt_q_num

    def set_balance_sheets_df(self, a_df: pd.DataFrame):
        self._has_balance_sheets_df = any(a_df) and isinstance(a_df, pd.DataFrame) and not a_df.empty and \
                                      not a_df.shape[0] == 0 and not len(a_df) == 0 and not len(a_df.index) == 0
        if self._has_balance_sheets_df:
            self._balance_sheets_df = a_df
            print(a_df)

    def set_cashflows_df(self, a_df: pd.DataFrame):
        self._has_cashflows_df = any(a_df) and isinstance(a_df, pd.DataFrame) and not a_df.empty and \
                                      not a_df.shape[0] == 0 and not len(a_df) == 0 and not len(a_df.index) == 0
        if self._has_cashflows_df:
            self._cashflows_df = a_df
            print(a_df)

    @property
    def CurrentDay(self):
        return self._current_dt_day

    @property
    def CurrentDayTh(self):
        return self._current_dt_day_th

    @property
    def CurrentWeekTh(self):
        return self._current_dt_week_th

    @property
    def CurrentMonth(self):
        return self._current_dt_month

    @property
    def CurrentYear(self):
        return self._current_dt_year

    @property
    def CurrentQ(self):
        return self._current_dt_q

    @property
    def CurrentQNumber(self):
        return self._current_dt_q_num

    @property
    def CurrentQuarter(self):
        return self._current_dt_q_str

    @property
    def CurrentFiscalQuarter(self):
        return self._current_quarter

    @property
    def PreviousQ(self):
        return self._previous_dt_q

    @property
    def PreviousQNumber(self):
        return self._previous_dt_q_num

    @property
    def PreviousQuarter(self):
        return self._previous_dt_q_str

    @property
    def PreviousFiscalQuarter(self):
        return self._previous_quarter

    @property
    def PreviousFiscalQuarterStart(self):
        return self._previous_dt

    @property
    def BaseQ(self):
        return self._base_dt_q

    @property
    def BaseQNumber(self):
        return self._base_dt_q_num

    @property
    def BaseQuarter(self):
        return self._base_dt_q_str

    @property
    def BaseFiscalQuarter(self):
        return self._base_quarter

    @property
    def BaseFiscalQuarterStart(self):
        return self._base_dt
