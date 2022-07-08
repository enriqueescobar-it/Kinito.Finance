import json
from datetime import datetime

from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable

from Common.InfoType.Times.AbstractTimeInfo import AbstractTimeInfo


class TimeSpanInfo(AbstractTimeInfo):

    __header: list = ['Field', 'FieldInfo']
    __past_months: int = 0
    _pretty_table: PrettyTable = PrettyTable()
    _dt_stop: datetime
    _dt_start: datetime
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
        self._pretty_table.field_names = self.__header
        return self._pretty_table.__str__()

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1]
        }.items()

    def __set_years(self):
        self._years = relativedelta(self._dt_stop, self._dt_start).years

    def __set_quarters(self):
        self._quarters = relativedelta(self._dt_stop, self._dt_start).months % 3

    def __set_months(self):
        self._months = self._years * 12
        self._months += relativedelta(self._dt_stop, self._dt_start).months

    def __set_weeks(self):
        self._weeks = self._years * 52
        self._weeks += relativedelta(self._dt_stop, self._dt_start).months

    def __set_w_days(self):
        pass

    def __set_t_days(self):
        pass

    def __set_days(self):
        self._days = int(round(self._years * 365.25))
        self._days += int(round(relativedelta(self._dt_stop, self._dt_start).months * 30.4375))

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
