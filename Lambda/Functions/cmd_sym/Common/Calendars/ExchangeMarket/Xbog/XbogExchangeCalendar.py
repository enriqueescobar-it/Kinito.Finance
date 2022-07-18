import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xbog

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XbogExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xbog.XBOGExchangeCalendar = xcals.get_calendar('XBOG')

    def __init__(self) -> None:
        pass
