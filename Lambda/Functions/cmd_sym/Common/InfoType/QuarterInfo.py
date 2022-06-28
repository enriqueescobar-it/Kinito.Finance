import json
import math
from datetime import datetime

import pandas as pd
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
    _current_quarter_start: datetime = _current_dt
    _current_quarter_stop: datetime = _current_dt
    _previous_dt: datetime = _current_dt
    _previous_dt_year: int = 2001
    _previous_dt_q: int = 2
    _previous_dt_q_num: str = 'Q2'
    _previous_dt_q_str: str = '2001Q2'
    _previous_quarter: FiscalQuarter = FiscalQuarter(2001, 2)
    _previous_quarter_start: datetime = _current_dt
    _previous_quarter_stop: datetime = _current_dt
    _base_dt: datetime = _current_dt
    _base_dt_year: int = 2001
    _base_dt_q: int = 3
    _base_dt_q_num: str = 'Q2'
    _base_dt_q_str: str = '2001Q2'
    _base_quarter: FiscalQuarter = FiscalQuarter(2001, 3)
    _base_quarter_start: datetime = _current_dt
    _base_quarter_stop: datetime = _current_dt
    _year_dt: datetime = _current_dt
    _year_dt_year: int = 2001
    _year_dt_q: int = 3
    _year_dt_q_num: str = 'Q2'
    _year_dt_q_str: str = '2000Q2'
    _year_quarter: FiscalQuarter = FiscalQuarter(2000, 3)
    _year_quarter_start: datetime = _current_dt
    _year_quarter_stop: datetime = _current_dt
    _has_balance_sheets_df: bool = False
    _balance_sheets_df: pd.DataFrame = pd.DataFrame()
    _has_cashflows_df: bool = False
    _cashflows_df: pd.DataFrame = pd.DataFrame()
    _has_earnings_df: bool = False
    _earnings_df: pd.DataFrame = pd.DataFrame()
    _has_financials_df: bool = False
    _financials_df: pd.DataFrame = pd.DataFrame()

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))):
        self._current_dt = d_t
        fdt: FiscalDateTime =\
            FiscalDateTime(d_t.year, d_t.month, d_t.day, d_t.hour, d_t.minute, d_t.second, d_t.microsecond)
        self._current_dt_day = self._current_dt.day
        self._current_dt_day_th = fdt.fiscal_day
        self._current_dt_week_th = self._current_dt.isocalendar()[1]
        self._current_dt_month = self._current_dt.month
        self._current_dt_year = self._current_dt.year
        self._current_dt_q = self.__get_quarter_int(self._current_dt)
        self._current_dt_q_num = self.__get_quarter_str(self._current_dt)
        self._current_dt_q_str = self.__get_quarter_string(self._current_dt)
        self._current_quarter = self.__get_quarter_fiscal(self._current_dt)
        self._current_quarter_start = self.__get_quarter_fiscal_start(self._current_dt)
        self._current_quarter_stop = self.__get_quarter_fiscal_stop(self._current_dt)
        self._previous_dt = datetime(self._current_dt.year, self._current_dt.month - 3, self._current_dt.day,
                                     tzinfo=self._current_dt.tzinfo)
        self._previous_dt_year = self._previous_dt.year
        self._previous_dt_q = self.__get_quarter_int(self._previous_dt)
        self._previous_dt_q_num = self.__get_quarter_str(self._previous_dt)
        self._previous_dt_q_str = self.__get_quarter_string(self._previous_dt)
        self._previous_quarter = self.__get_quarter_fiscal(self._previous_dt)
        self._previous_quarter_start = self.__get_quarter_fiscal_start(self._previous_dt)
        self._previous_quarter_stop = self.__get_quarter_fiscal_stop(self._previous_dt)
        self.__set_year_line()
        self.__set_balance_sheets_df()
        self.__set_cashflows_df()
        self.__set_earnings_df()
        self.__set_financials_df()
        self.set_baseline()

    def __str__(self) -> str:
        self._pretty_table.field_names = self.__header
        self._pretty_table.add_row(['CurrentDateTime', self._current_dt])
        self._pretty_table.add_row(['CurrentDay', self._current_dt_day])
        self._pretty_table.add_row(['CurrentDayTh', self._current_dt_day_th])
        self._pretty_table.add_row(['CurrentWeekTh', self._current_dt_week_th])
        self._pretty_table.add_row(['CurrentMonth', self._current_dt_month])
        self._pretty_table.add_row(['CurrentYear', self._current_dt_year])
        self._pretty_table.add_row(['CurrentQ', self._current_dt_q])
        self._pretty_table.add_row(['CurrentQNumber', self._current_dt_q_num])
        self._pretty_table.add_row(['CurrentQuarter', self._current_dt_q_str])
        self._pretty_table.add_row(['CurrentFiscalQuarter', str(self._current_quarter)])
        self._pretty_table.add_row(['CurrentFiscalQuarterStart', self._current_quarter_start])
        self._pretty_table.add_row(['CurrentFiscalQuarterStop', self._current_quarter_stop])
        self._pretty_table.add_row(['PreviousDateTime', self._previous_dt])
        self._pretty_table.add_row(['PreviousYear', self._previous_dt_year])
        self._pretty_table.add_row(['PreviousQ', self._previous_dt_q])
        self._pretty_table.add_row(['PreviousQNumber', self._previous_dt_q_num])
        self._pretty_table.add_row(['PreviousQuarter', self._previous_dt_q_str])
        self._pretty_table.add_row(['PreviousFiscalQuarter', str(self._previous_quarter)])
        self._pretty_table.add_row(['PreviousFiscalQuarterStart', self._previous_quarter_start])
        self._pretty_table.add_row(['PreviousFiscalQuarterStop', self._previous_quarter_stop])
        self._pretty_table.add_row(['YearDateTime', self._year_dt])
        self._pretty_table.add_row(['YearYear', self._year_dt_year])
        self._pretty_table.add_row(['YearQ', self._year_dt_q])
        self._pretty_table.add_row(['YearQNumber', self._year_dt_q_num])
        self._pretty_table.add_row(['YearQuarter', self._year_dt_q_str])
        self._pretty_table.add_row(['YearFiscalQuarter', str(self._year_quarter)])
        self._pretty_table.add_row(['YearFiscalQuarterStart', self._year_quarter_start])
        self._pretty_table.add_row(['YearFiscalQuarterStop', self._year_quarter_stop])
        self._pretty_table.add_row(['BaseDateTime', self._base_dt])
        self._pretty_table.add_row(['BaseYear', self._base_dt_year])
        self._pretty_table.add_row(['BaseQ', self._base_dt_q])
        self._pretty_table.add_row(['BaseQNumber', self._base_dt_q_num])
        self._pretty_table.add_row(['BaseQuarter', self._base_dt_q_str])
        self._pretty_table.add_row(['BaseFiscalQuarter', str(self._base_quarter)])
        self._pretty_table.add_row(['BaseFiscalQuarterStart', self._base_quarter_start])
        self._pretty_table.add_row(['BaseFiscalQuarterStop', self._base_quarter_stop])
        self._pretty_table.add_row(['HasBalanceSheetDf', self._has_balance_sheets_df])
        self._pretty_table.add_row(['HasCashflowDf', self._has_cashflows_df])
        self._pretty_table.add_row(['HasEarningDf', self._has_earnings_df])
        self._pretty_table.add_row(['HasFinancialDf', self._has_financials_df])
        return self._pretty_table.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            "current_dt": str(self._current_dt),
            "current_day": self._current_dt_day,
            "current_day_th": self._current_dt_day_th,
            "current_week_th": self._current_dt_week_th,
            "current_month": self._current_dt_month,
            "current_year": self._current_dt_year,
            "current_q": self._current_dt_q,
            "current_q_num": self._current_dt_q_num,
            "current_q_str": self._current_dt_q_str,
            "current_quarter": str(self._current_quarter),
            "current_quarter_start": str(self._current_quarter_start),
            "current_quarter_stop": str(self._current_quarter_stop),
            "previous_dt": str(self._previous_dt),
            "previous_year": self._previous_dt_year,
            "previous_q": self._previous_dt_q,
            "previous_q_num": self._previous_dt_q_num,
            "previous_q_str": self._previous_dt_q_str,
            "previous_quarter": str(self._previous_quarter),
            "previous_quarter_start": str(self._previous_quarter_start),
            "previous_quarter_stop": str(self._previous_quarter_stop),
            "year_dt": str(self._year_dt),
            "year_year": self._year_dt_year,
            "year_q": self._year_dt_q,
            "year_q_num": self._year_dt_q_num,
            "year_q_str": self._year_dt_q_str,
            "year_quarter": str(self._year_quarter),
            "year_quarter_start": str(self._year_quarter_start),
            "year_quarter_stop": str(self._year_quarter_stop),
            "base_dt": str(self._base_dt),
            "base_year": self._base_dt_year,
            "base_q": self._base_dt_q,
            "base_q_num": self._base_dt_q_num,
            "base_q_str": self._base_dt_q_str,
            "base_quarter": str(self._base_quarter),
            "base_quarter_start": str(self._base_quarter_start),
            "base_quarter_stop": str(self._base_quarter_stop),
            "has_balance_sheet_df": self._has_balance_sheets_df,
            "has_cashflows_df": self._has_cashflows_df,
            "has_earnings_df": self._has_earnings_df,
            "has_financials_df": self._has_financials_df
        }.items()

    def __get_quarter_int(self, dt: datetime) -> int:
        return math.ceil(dt.month/3)

    def __get_quarter_str(self, dt: datetime) -> str:
        return "Q" + str(self.__get_quarter_int(dt))

    def __get_quarter_string(self, dt: datetime) -> str:
        return str(dt.year) + self.__get_quarter_str(dt)

    def __get_quarter_fiscal(self, dt: datetime) -> FiscalQuarter:
        fdt = FiscalDateTime(dt.year, dt.month, dt.day)
        return FiscalQuarter(fdt.year, fdt.fiscal_quarter)

    def __get_quarter_fiscal_start(self, dt: datetime) -> datetime:
        fq: FiscalQuarter = self.__get_quarter_fiscal(dt)
        return datetime(fq.start.year, fq.start.month, fq.start.day)

    def __get_quarter_fiscal_stop(self, dt: datetime) -> datetime:
        fq: FiscalQuarter = self.__get_quarter_fiscal(dt)
        return datetime(fq.end.year, fq.end.month, fq.end.day)

    def __set_year_line(self):
        self._year_dt = datetime(self._previous_dt.year - 1, self._previous_dt.month,
                                 self._previous_dt.day).replace(tzinfo=self._previous_dt.tzinfo)
        self._year_dt_year = self._year_dt.year
        self._year_dt_q = self.__get_quarter_int(self._year_dt)
        self._year_dt_q_num = self.__get_quarter_str(self._year_dt)
        self._year_dt_q_str = self.__get_quarter_string(self._year_dt)
        self._year_quarter = self.__get_quarter_fiscal(self._year_dt)
        self._year_quarter_start = self.__get_quarter_fiscal_start(self._year_dt)
        self._year_quarter_stop = self.__get_quarter_fiscal_stop(self._year_dt)

    def __set_balance_sheets_df(self):
        pass

    def __set_cashflows_df(self):
        pass

    def __set_earnings_df(self):
        pass

    def __set_financials_df(self):
        pass

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def set_baseline(self, base_years: int = 5):
        self._base_dt = datetime(self._previous_dt.year - base_years, self._previous_dt.month,
                                 self._previous_dt.day, tzinfo=self._previous_dt.tzinfo)
        self._base_dt_year = self._base_dt.year
        self._base_dt_q = self.__get_quarter_int(self._base_dt)
        self._base_dt_q_num = self.__get_quarter_str(self._base_dt)
        self._base_dt_q_str = self.__get_quarter_string(self._base_dt)
        self._base_quarter = self.__get_quarter_fiscal(self._base_dt)
        self._base_quarter_start = self.__get_quarter_fiscal_start(self._base_dt)
        self._base_quarter_stop = self.__get_quarter_fiscal_stop(self._base_dt)

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

    def set_earnings_df(self, a_df: pd.DataFrame):
        self._has_earnings_df = any(a_df) and isinstance(a_df, pd.DataFrame) and not a_df.empty and \
                                 not a_df.shape[0] == 0 and not len(a_df) == 0 and not len(a_df.index) == 0
        if self._has_earnings_df:
            self._earnings_df = a_df
            print(a_df)

    def set_financials_df(self, a_df: pd.DataFrame):
        self._has_financials_df = any(a_df) and isinstance(a_df, pd.DataFrame) and not a_df.empty and \
                                not a_df.shape[0] == 0 and not len(a_df) == 0 and not len(a_df.index) == 0
        if self._has_financials_df:
            self._financials_df = a_df
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
