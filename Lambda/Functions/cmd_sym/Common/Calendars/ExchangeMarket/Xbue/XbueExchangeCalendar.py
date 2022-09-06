import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xbue

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XbueExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xbue.XBUEExchangeCalendar = xcals.get_calendar('XBUE')

    def __init__(self) -> None:
        pass