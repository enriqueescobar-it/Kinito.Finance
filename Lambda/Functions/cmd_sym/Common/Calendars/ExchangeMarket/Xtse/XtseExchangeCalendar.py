import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xtse

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XtseExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xtse.XTSEExchangeCalendar = xcals.get_calendar('XTSE')

    def __init__(self) -> None:
        pass
