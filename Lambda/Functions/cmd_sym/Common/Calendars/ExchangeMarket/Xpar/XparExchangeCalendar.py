import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xpar

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XparExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xpar.XPARExchangeCalendar = xcals.get_calendar('XPAR')

    def __init__(self) -> None:
        pass
