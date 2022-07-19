import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xwbo

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XwboExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xwbo.XWBOExchangeCalendar = xcals.get_calendar('XWBO')

    def __init__(self) -> None:
        pass
