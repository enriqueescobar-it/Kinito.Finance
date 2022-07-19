import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xswx

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XswxExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xswx.XSWXExchangeCalendar = xcals.get_calendar('XSWX')

    def __init__(self) -> None:
        pass
