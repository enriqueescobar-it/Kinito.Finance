import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xcbf

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XcbfExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xcbf.XCBFExchangeCalendar = xcals.get_calendar('XCBF')

    def __init__(self) -> None:
        pass
