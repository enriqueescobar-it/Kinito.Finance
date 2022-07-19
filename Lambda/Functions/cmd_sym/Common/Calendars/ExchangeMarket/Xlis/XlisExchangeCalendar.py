import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xlis

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XlisExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xlis.XLISExchangeCalendar = xcals.get_calendar('XLIS')

    def __init__(self) -> None:
        pass
