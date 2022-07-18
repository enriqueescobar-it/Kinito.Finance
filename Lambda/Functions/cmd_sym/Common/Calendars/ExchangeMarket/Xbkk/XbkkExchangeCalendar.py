import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xbkk

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XbkkExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xbkk.XBKKExchangeCalendar = xcals.get_calendar('XBKK')

    def __init__(self) -> None:
        pass
