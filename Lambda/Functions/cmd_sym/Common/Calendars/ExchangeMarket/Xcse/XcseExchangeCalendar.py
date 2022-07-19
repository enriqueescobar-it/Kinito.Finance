import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xcse

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XcseExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xcse.XCSEExchangeCalendar = xcals.get_calendar('XCSE')

    def __init__(self) -> None:
        pass
