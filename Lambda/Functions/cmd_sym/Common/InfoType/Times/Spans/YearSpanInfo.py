from datetime import datetime

import dateutil
from backports.zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta
from pandas import DataFrame
from prettytable import PrettyTable

from Common.InfoType.Times.Spans.AbstractTimeSpanInfo import AbstractTimeSpanInfo
from Common.InfoType.Times.Spans.QuarterSpanInfo import QuarterSpanInfo


class YearSpanInfo(AbstractTimeSpanInfo):
    __pretty_table: PrettyTable = PrettyTable()
    _quarters: int = 4
    _balance_sheets_df: DataFrame = DataFrame()
    _cashflows_df: DataFrame = DataFrame()
    _earnings_df: DataFrame = DataFrame()
    _financials_df: DataFrame = DataFrame()

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))) -> None:
        super().__init__(date_time_start=self._get_current_quarter_start(d_t))

    def __str__(self) -> str:
        self.__pretty_table.field_names = [self._header[0] + 'YearSpan', self._header[1] + 'YearSpan']
        self.__pretty_table.add_row(['DateTimeStart', self._start_dti.datetime])
        self.__pretty_table.add_row(['DateTimeStop', self._stop_dti.datetime])
        return self.__pretty_table.__str__()

    def __iter__(self):
        yield from {
            self._header[0] + 'YearSpan': self._header[1] + 'YearSpan',
            "date_time_start": str(self._start_dti.datetime),
            "date_time_stop": str(self._stop_dti.datetime)
        }.items()

    def _get_current_quarter_start(self, d_t: datetime) -> datetime:
        return QuarterSpanInfo(d_t).start_datetime_info.datetime - dateutil.relativedelta.relativedelta(months=12)

    def set_balance_sheets_df(self, b_df: DataFrame):
        self._balance_sheets_df = b_df

    def set_cashflows_df(self, c_df: DataFrame):
        self._cashflows_df = c_df

    def set_earnings_df(self, e_df: DataFrame):
        self._earnings_df = e_df

    def set_financials_df(self, f_df: DataFrame):
        self._financials_df = f_df
