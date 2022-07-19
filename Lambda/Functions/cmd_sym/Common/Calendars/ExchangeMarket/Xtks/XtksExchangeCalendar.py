import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xtks

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XtksExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xtks.XTKSExchangeCalendar = xcals.get_calendar('XTKS')

    def __init__(self) -> None:
        pass
