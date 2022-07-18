import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_asex

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class AsexExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_asex.ASEXExchangeCalendar = xcals.get_calendar('ASEX')

    def __init__(self) -> None:
        pass