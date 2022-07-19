import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xlon

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XlonExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xlon.XLONExchangeCalendar = xcals.get_calendar('XLON')

    def __init__(self) -> None:
        pass
