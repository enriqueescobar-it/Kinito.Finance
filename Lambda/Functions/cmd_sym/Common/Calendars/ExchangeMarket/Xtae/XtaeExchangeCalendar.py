import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xtae

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XtaeExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xtae.XTAEExchangeCalendar = xcals.get_calendar('XTAE')

    def __init__(self) -> None:
        pass
