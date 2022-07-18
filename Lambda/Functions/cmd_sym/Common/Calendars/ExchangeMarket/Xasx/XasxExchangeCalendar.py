import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xasx

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XasxExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xasx.XASXExchangeCalendar = xcals.get_calendar('XASX')

    def __init__(self) -> None:
        pass
    