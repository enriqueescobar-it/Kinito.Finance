import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xnze

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XnzeExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xnze.XNZEExchangeCalendar = xcals.get_calendar('XNZE')

    def __init__(self) -> None:
        pass
