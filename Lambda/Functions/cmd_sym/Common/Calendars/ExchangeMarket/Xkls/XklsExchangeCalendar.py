import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xkls

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XklsExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xkls.XKLSExchangeCalendar = xcals.get_calendar('XKLS')

    def __init__(self) -> None:
        pass
