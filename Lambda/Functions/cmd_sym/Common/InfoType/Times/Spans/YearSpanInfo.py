from datetime import datetime
from typing import List

from backports.zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta
from pandas import DataFrame
from prettytable import PrettyTable

from Common.InfoType.Times.Spans.AbstractTimeSpanInfo import AbstractTimeSpanInfo
from Common.InfoType.Times.Spans.QuarterSpanInfo import QuarterSpanInfo


class YearSpanInfo(AbstractTimeSpanInfo):
    __pretty_table: PrettyTable = PrettyTable()
    _quarters: int = 4
    _qsi_list: List[QuarterSpanInfo] = []
    _balance_sheets_df: DataFrame = DataFrame()
    _cashflows_df: DataFrame = DataFrame()
    _earnings_df: DataFrame = DataFrame()
    _financials_df: DataFrame = DataFrame()

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))) -> None:
        super().__init__(date_time_start=d_t)
        self.__set_qsi_list(d_t)
        self._start_dti = self._qsi_list[self._quarters - 1].start_datetime_info
        self._stop_dti = self._qsi_list[0].stop_datetime_info

    def __str__(self) -> str:
        self.__pretty_table.field_names = self._header
        self.__pretty_table.add_row(['Length', len(self._qsi_list)])
        self.__pretty_table.add_row(['DateTimeStart', self._start_dti.datetime])
        self.__pretty_table.add_row(['DateTimeStop', self._stop_dti.datetime])
        return self.__pretty_table.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1],
            "length": len(self._qsi_list),
            "date_time_start": str(self._start_dti.datetime),
            "date_time_stop": str(self._stop_dti.datetime)
        }.items()
        
    def __set_qsi_list(self, dt: datetime) -> None:
        for i in range(1, self._quarters + 1):
            qi: QuarterSpanInfo = QuarterSpanInfo(dt - relativedelta(months=i * 3))
            print("CACA", i * 3, qi.stop_datetime_info.datetime)
            self._qsi_list.append(qi)

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
