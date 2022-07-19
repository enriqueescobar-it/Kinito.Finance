import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xjse

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XjseExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xjse.XJSEExchangeCalendar = xcals.get_calendar('XJSE')

    def __init__(self) -> None:
        pass
