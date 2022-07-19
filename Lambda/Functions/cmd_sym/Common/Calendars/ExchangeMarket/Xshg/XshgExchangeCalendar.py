import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xshg

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XshgExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xshg.XSHGExchangeCalendar = xcals.get_calendar('XSHG')

    def __init__(self) -> None:
        pass
