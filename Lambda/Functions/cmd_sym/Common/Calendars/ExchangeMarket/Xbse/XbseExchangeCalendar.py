import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xbse

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XbseExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xbse.XBSEExchangeCalendar = xcals.get_calendar('XBSE')

    def __init__(self) -> None:
        pass
