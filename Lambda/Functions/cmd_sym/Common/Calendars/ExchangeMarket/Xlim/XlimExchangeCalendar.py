import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xlim

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XlimExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xlim.XLIMExchangeCalendar = xcals.get_calendar('XLIM')

    def __init__(self) -> None:
        pass
