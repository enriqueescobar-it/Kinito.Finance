import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xist

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XistExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xist.XISTExchangeCalendar = xcals.get_calendar('XIST')

    def __init__(self) -> None:
        pass
