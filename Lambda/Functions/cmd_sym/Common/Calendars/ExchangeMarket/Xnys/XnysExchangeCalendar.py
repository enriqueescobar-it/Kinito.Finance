import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xnys

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XnysExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xnys.XNYSExchangeCalendar = xcals.get_calendar('XNYS')

    def __init__(self) -> None:
        pass
