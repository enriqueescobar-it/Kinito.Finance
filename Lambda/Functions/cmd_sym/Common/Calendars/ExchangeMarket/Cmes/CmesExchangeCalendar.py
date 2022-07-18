import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_cmes

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class CmesExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_cmes.CMESExchangeCalendar = xcals.get_calendar('CMES')

    def __init__(self) -> None:
        pass