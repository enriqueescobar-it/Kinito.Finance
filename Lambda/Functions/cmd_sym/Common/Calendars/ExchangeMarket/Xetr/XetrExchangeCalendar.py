import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xetr

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XetrExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xetr.XETRExchangeCalendar = xcals.get_calendar('XETR')

    def __init__(self) -> None:
        pass
