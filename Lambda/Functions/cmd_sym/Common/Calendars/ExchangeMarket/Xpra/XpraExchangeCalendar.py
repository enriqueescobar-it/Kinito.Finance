import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xpra

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XpraExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xpra.XPRAExchangeCalendar = xcals.get_calendar('XPRA')

    def __init__(self) -> None:
        pass
