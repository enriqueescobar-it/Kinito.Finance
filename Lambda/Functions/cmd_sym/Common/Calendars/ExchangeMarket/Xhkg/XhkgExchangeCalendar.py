import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xhkg

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XhkgExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xhkg.XHKGExchangeCalendar = xcals.get_calendar('XHKG')

    def __init__(self) -> None:
        pass
