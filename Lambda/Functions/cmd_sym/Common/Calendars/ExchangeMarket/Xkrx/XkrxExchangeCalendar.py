import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xkrx

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XkrxExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xkrx.XKRXExchangeCalendar = xcals.get_calendar('XKRX')

    def __init__(self) -> None:
        pass
