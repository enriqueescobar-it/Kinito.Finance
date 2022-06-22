from datetime import datetime, timezone, timedelta, tzinfo
from backports.zoneinfo import ZoneInfo

from Common.InfoType.AbstractInfo import AbstractInfo


class TimeInfo(AbstractInfo):
    _d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))
    _d_t_time: datetime.time = _d_t.time()
    _d_t_tz_info: tzinfo = ZoneInfo("America/Toronto")
    _d_t_format: str = "%Y-%m-%d %H:%M:%S"
    _d_t_tz_str: str = "EST"
    _d_t_to_day: int = 11
    _d_t_to_week: int = 1
    _d_t_to_month: int = 9
    _d_t_to_year: int = 2001

    def __init__(self, d_t: datetime = datetime.now().replace(tzinfo=ZoneInfo("America/Toronto"))):
        self._d_t = d_t
        self._d_t_time = d_t.time()
        self._d_t_tz_info = d_t.tzinfo
        self._d_t_tz_str = d_t.tzname()
        self._d_t_to_day = d_t.day
        self._d_t_to_week = d_t.isocalendar()[1]
        self._d_t_to_month = d_t.month
        self._d_t_to_year = d_t.year
