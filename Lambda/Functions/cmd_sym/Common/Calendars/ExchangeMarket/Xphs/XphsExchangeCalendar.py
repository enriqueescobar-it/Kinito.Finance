import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xphs

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XphsExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xphs.XPHSExchangeCalendar = xcals.get_calendar('XPHS')

    def __init__(self) -> None:
        pass
