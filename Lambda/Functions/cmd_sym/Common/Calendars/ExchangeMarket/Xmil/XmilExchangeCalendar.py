import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xmil

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XmilExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xmil.XMILExchangeCalendar = xcals.get_calendar('XMIL')

    def __init__(self) -> None:
        pass
