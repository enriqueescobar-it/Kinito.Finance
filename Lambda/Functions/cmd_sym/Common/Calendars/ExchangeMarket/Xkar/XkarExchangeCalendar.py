import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xkar

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XkarExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xkar.XKARExchangeCalendar = xcals.get_calendar('XKAR')

    def __init__(self) -> None:
        pass
