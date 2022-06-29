import json

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from typing import List

from pandas import DataFrame

from Common.InfoType.AbstractInfo import AbstractInfo
from Common.InfoType.QuarterInfo import QuarterInfo

from backports.zoneinfo import ZoneInfo
from prettytable import PrettyTable


class YearInfo(AbstractInfo):
    __quarters: int = 4
    __header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _dt: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))
    _dt_start: datetime = _dt
    _dt_stop: datetime = _dt
    _qi_list: List[QuarterInfo] = []
    _balance_sheets_df: DataFrame = DataFrame()
    _cashflows_df: DataFrame = DataFrame()
    _earnings_df: DataFrame = DataFrame()
    _financials_df: DataFrame = DataFrame()

    def __init__(self, dt: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))) -> None:
        self._dt = dt
        self.__set_qi_list()
        self._dt_start = self._qi_list[self.__quarters-1].StartDateTime
        self._dt_stop = self._qi_list[0].StopDateTime

    def __str__(self) -> str:
        self._pretty_table.field_names = self.__header
        self._pretty_table.add_row(['DateTimeStop', self._dt_stop])
        self._pretty_table.add_row(['DateTimeStart', self._dt_start])
        self._pretty_table.add_row(['Length', len(self._qi_list)])
        return self._pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            "dt_stop": str(self._dt_stop),
            "dt_start": str(self._dt_start),
            "length": len(self._qi_list)
        }.items()
        
    def __set_qi_list(self) -> None:
        for i in range(1, self.__quarters + 1):
            qi: QuarterInfo = QuarterInfo(self._dt - relativedelta(months=i*3))
            print("CACA", i*3, qi.StopDateTime)
            self._qi_list.append(qi)

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def set_balance_sheets_df(self, bs_df: DataFrame):
        self._balance_sheets_df = bs_df

    def set_cashflows_df(self, cf_df: DataFrame):
        self._cashflows_df = cf_df

    def set_earnings_df(self, e_df: DataFrame):
        self._earnings_df = e_df

    def set_financials_df(self, f_df: DataFrame):
        self._financials_df = f_df

    @property
    def DateTimeStop(self) -> datetime:
        return self._dt_stop

    @property
    def DateTimeStart(self) -> datetime:
        return self._dt_start

    @property
    def Quarters(self) -> int:
        return self.__quarters
