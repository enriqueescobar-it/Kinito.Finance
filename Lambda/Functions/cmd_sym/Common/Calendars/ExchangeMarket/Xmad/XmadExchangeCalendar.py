import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xmad

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XmadExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xmad.XMADExchangeCalendar = xcals.get_calendar('XMAD')

    def __init__(self) -> None:
        pass
