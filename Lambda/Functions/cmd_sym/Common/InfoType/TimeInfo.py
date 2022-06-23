import json
import math
from datetime import datetime, timezone, timedelta, tzinfo
from backports.zoneinfo import ZoneInfo

from prettytable import PrettyTable

from Common.InfoType.AbstractInfo import AbstractInfo


class TimeInfo(AbstractInfo):
    __header: list = ['Field', 'FieldInfo']
    _pretty_table: PrettyTable = PrettyTable()
    _d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))
    _d_t_time: datetime.time = _d_t.time()
    _d_t_tz_info: tzinfo = ZoneInfo("America/Toronto")
    _d_t_format: str = "%Y-%m-%d %H:%M:%S"
    _d_t_tz_str: str = "EST"
    _d_t_to_day: int = 11
    _d_t_to_week: int = 1
    _d_t_to_month: int = 9
    _d_t_to_q: int = 3
    _d_t_to_q_num: str = 'Q3'
    _d_t_to_quarter: str = '2001Q3'
    _d_t_to_year: int = 2001

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))):
        self._d_t = d_t
        self._d_t_time = d_t.time()
        self._d_t_tz_info = d_t.tzinfo
        self._d_t_tz_str = d_t.tzname()
        self._d_t_to_day = d_t.day
        self._d_t_to_week = d_t.isocalendar()[1]
        self._d_t_to_month = d_t.month
        self._d_t_to_q = math.ceil(d_t.month / 3.)
        self._d_t_to_year = d_t.year
        self._d_t_to_q_num = 'Q' + str(self._d_t_to_q)
        self._d_t_to_quarter = str(self._d_t_to_year) + self._d_t_to_q_num

    def __str__(self) -> str:
        self._pretty_table.field_names = self.__header
        self._pretty_table.add_row(['DateTime', self._d_t])
        self._pretty_table.add_row(['Time', self._d_t_time])
        self._pretty_table.add_row(['ZoneInfo', self._d_t_tz_info])
        self._pretty_table.add_row(['TimeFormat', self._d_t_format])
        self._pretty_table.add_row(['TimeZone', self._d_t_tz_str])
        self._pretty_table.add_row(['DateDay', self._d_t_to_day])
        self._pretty_table.add_row(['DateWeek', self._d_t_to_week])
        self._pretty_table.add_row(['DateMonth', self._d_t_to_month])
        self._pretty_table.add_row(['DateQ', self._d_t_to_q])
        self._pretty_table.add_row(['DateQNumber', self._d_t_to_q_num])
        self._pretty_table.add_row(['DateQuarter', self._d_t_to_quarter])
        self._pretty_table.add_row(['DateYear', self._d_t_to_year])
        return self._pretty_table.__str__()

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield from {
            self.__header[0]: self.__header[1],
            #"date_time": self._d_t,
            "time": str(self._d_t_time),
            "zone_info": str(self._d_t_tz_info),
            "time_format": self._d_t_format,
            "time_zone": self._d_t_tz_str,
            "date_day": self._d_t_to_day,
            "date_week": self._d_t_to_week,
            "date_month": self._d_t_to_month,
            "date_q": self._d_t_to_q,
            "date_q_num": self._d_t_to_q_num,
            "date_quarter": self._d_t_to_quarter,
            "date_year": self._d_t_to_year
        }.items()

    def to_json(self):
        return json.dumps(dict(self), ensure_ascii=False)
