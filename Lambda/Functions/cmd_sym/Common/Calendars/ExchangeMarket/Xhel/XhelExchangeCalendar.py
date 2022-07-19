import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xhel

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XhelExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xhel.XHELExchangeCalendar = xcals.get_calendar('XHEL')

    def __init__(self) -> None:
        pass
