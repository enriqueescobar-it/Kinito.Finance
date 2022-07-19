import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xbru

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XbruExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xbru.XBRUExchangeCalendar = xcals.get_calendar('XBRU')

    def __init__(self) -> None:
        pass
