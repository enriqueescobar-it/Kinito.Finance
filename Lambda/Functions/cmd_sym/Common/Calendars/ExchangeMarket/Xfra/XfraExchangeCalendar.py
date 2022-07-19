import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xfra

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XfraExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xfra.XFRAExchangeCalendar = xcals.get_calendar('XFRA')

    def __init__(self) -> None:
        pass
