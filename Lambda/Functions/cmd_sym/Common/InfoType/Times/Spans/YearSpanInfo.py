import json
from datetime import datetime
from typing import List

from backports.zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta
from pandas import DataFrame

from Common.InfoType.Times.Spans.AbstractTimeSpanInfo import AbstractTimeSpanInfo
from Common.InfoType.Times.Spans.QuarterSpanInfo import QuarterSpanInfo


class YearSpanInfo(AbstractTimeSpanInfo):
    _quarters: int = 4
    _dt: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))
    _qi_list: List[QuarterSpanInfo] = []
    _balance_sheets_df: DataFrame = DataFrame()
    _cashflows_df: DataFrame = DataFrame()
    _earnings_df: DataFrame = DataFrame()
    _financials_df: DataFrame = DataFrame()

    def __init__(self, dt: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))) -> None:
        self._dt = dt
        self.__set_qi_list()
        self._start_dt = self._qi_list[self._quarters - 1].start_datetime
        self._stop_dt = self._qi_list[0].stop_datetime

    def __str__(self) -> str:
        self._pretty_table.field_names = self._header
        self._pretty_table.add_row(['DateTimeStop', self._stop_dt])
        self._pretty_table.add_row(['DateTimeStart', self._start_dt])
        self._pretty_table.add_row(['Length', len(self._qi_list)])
        return self._pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "dt_stop": str(self._stop_dt),
            "dt_start": str(self._start_dt),
            "length": len(self._qi_list)
        }.items()
        
    def __set_qi_list(self) -> None:
        for i in range(1, self._quarters + 1):
            qi: QuarterSpanInfo = QuarterSpanInfo(self._dt - relativedelta(months=i * 3))
            print("CACA", i * 3, qi.stop_datetime)
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
    def quarters(self) -> int:
        return self._quarters
