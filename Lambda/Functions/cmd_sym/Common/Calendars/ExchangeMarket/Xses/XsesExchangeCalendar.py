import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xses

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XsesExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xses.XSESExchangeCalendar = xcals.get_calendar('XSES')

    def __init__(self) -> None:
        pass
