import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xwar

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XwarExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xwar.XWARExchangeCalendar = xcals.get_calendar('XWAR')

    def __init__(self) -> None:
        pass
