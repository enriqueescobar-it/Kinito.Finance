import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xsto

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XstoExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xsto.XSTOExchangeCalendar = xcals.get_calendar('XSTO')

    def __init__(self) -> None:
        pass
