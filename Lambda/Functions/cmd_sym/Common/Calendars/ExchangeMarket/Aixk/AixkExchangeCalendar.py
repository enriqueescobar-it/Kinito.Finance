import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_aixk

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class AixkExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_aixk.AIXKExchangeCalendar = xcals.get_calendar('AIXK')

    def __init__(self) -> None:
        pass