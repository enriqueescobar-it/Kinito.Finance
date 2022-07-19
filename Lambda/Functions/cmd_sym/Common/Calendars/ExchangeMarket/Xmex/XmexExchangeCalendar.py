import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xmex

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XmexExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xmex.XMEXExchangeCalendar = xcals.get_calendar('XMEX')

    def __init__(self) -> None:
        pass
