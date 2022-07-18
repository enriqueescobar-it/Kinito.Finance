import json
from datetime import datetime

import dateutil
from backports.zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable

from Common.InfoType.Times.Spans.AbstractTimeSpanInfo import AbstractTimeSpanInfo


class TimeSpanInfo(AbstractTimeSpanInfo):
    __pretty_table: PrettyTable = PrettyTable()
    _past_months: int = 0
    _years: int = 0
    _quarters: int = 0
    _months: int = 0
    _weeks: int = 0
    _w_days: int = 0
    _t_days: int = 0
    _days: int = 0

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto")),
                 past_months: int = 5):
        super().__init__(date_time_start=(d_t - dateutil.relativedelta.relativedelta(months=past_months)))
        self._past_months = past_months
        self.__set_years()
        self.__set_quarters()
        self.__set_months()
        self.__set_weeks()
        self.__set_w_days()
        self.__set_t_days()
        self.__set_days()

    def __str__(self) -> str:
        self.__pretty_table.field_names = [self._header[0] + 'Span', self._header[1] + 'Span']
        self.__pretty_table.add_row(['DateTimeStart', self._start_dti.datetime])
        self.__pretty_table.add_row(['DateTimeStop', self._stop_dti.datetime])
        self.__pretty_table.add_row(['DayCount', self._delta_days])
        self.__pretty_table.add_row(['HourCount', self._delta_hours])
        self.__pretty_table.add_row(['MinuteCount', self._delta_minutes])
        self.__pretty_table.add_row(['SecondCount', self._delta_seconds])
        return self.__pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self._header[0] + 'Span': self._header[1] + 'Span',
            "date_time_start": str(self._start_dti.datetime),
            "date_time_stop": str(self.stop_datetime_info.datetime),
            "delta_days": self._delta_days,
            "delta_hours": self._delta_hours,
            "delta_minutes": self._delta_minutes,
            "delta_seconds": self._delta_seconds
        }.items()

    def __set_years(self):
        self._years = relativedelta(self._stop_dti.datetime, self._start_dti.datetime).years

    def __set_quarters(self):
        self._quarters = relativedelta(self._stop_dti.datetime, self._start_dti.datetime).months % 3

    def __set_months(self):
        self._months = self._years * 12
        self._months += relativedelta(self._stop_dti.datetime, self._start_dti.datetime).months

    def __set_weeks(self):
        self._weeks = self._years * 52
        self._weeks += relativedelta(self._stop_dti.datetime, self._start_dti.datetime).months

    def __set_w_days(self):
        pass

    def __set_t_days(self):
        pass

    def __set_days(self):
        self._days = int(round(self._years * 365.25))
        self._days += int(round(relativedelta(self._stop_dti.datetime, self._start_dti.datetime).months * 30.4375))

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
