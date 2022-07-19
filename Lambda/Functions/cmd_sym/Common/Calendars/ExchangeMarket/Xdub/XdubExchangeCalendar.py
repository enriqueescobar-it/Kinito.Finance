import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xdub

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XdubExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xdub.XDUBExchangeCalendar = xcals.get_calendar('XDUB')

    def __init__(self) -> None:
        pass
