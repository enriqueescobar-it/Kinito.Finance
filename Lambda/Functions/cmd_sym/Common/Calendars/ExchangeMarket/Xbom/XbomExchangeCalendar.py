import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xbom

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XbomExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xbom.XBOMExchangeCalendar = xcals.get_calendar('XBOM')

    def __init__(self) -> None:
        pass
