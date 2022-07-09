import json

from dateutil.relativedelta import relativedelta

from Common.InfoType.Times.Spans.AbstractTimeSpanInfo import AbstractTimeSpanInfo


class TimeSpanInfo(AbstractTimeSpanInfo):
    __past_months: int = 0
    _years: int = 0
    _quarters: int = 0
    _months: int = 0
    _weeks: int = 0
    _w_days: int = 0
    _t_days: int = 0
    _days: int = 0

    def __init__(self, past_months: int = 5):
        self.__past_months = past_months
        self.__set_years()
        self.__set_quarters()
        self.__set_months()
        self.__set_weeks()
        self.__set_w_days()
        self.__set_t_days()
        self.__set_days()

    def __str__(self) -> str:
        self._pretty_table.field_names = self._header
        return self._pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self._header[0]: self._header[1]
        }.items()

    def __set_years(self):
        self._years = relativedelta(self._stop_dt, self._start_dt).years

    def __set_quarters(self):
        self._quarters = relativedelta(self._stop_dt, self._start_dt).months % 3

    def __set_months(self):
        self._months = self._years * 12
        self._months += relativedelta(self._stop_dt, self._start_dt).months

    def __set_weeks(self):
        self._weeks = self._years * 52
        self._weeks += relativedelta(self._stop_dt, self._start_dt).months

    def __set_w_days(self):
        pass

    def __set_t_days(self):
        pass

    def __set_days(self):
        self._days = int(round(self._years * 365.25))
        self._days += int(round(relativedelta(self._stop_dt, self._start_dt).months * 30.4375))

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
