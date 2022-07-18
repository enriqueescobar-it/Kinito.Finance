import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_iepa

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class IepaExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_iepa.IEPAExchangeCalendar = xcals.get_calendar('IEPA')

    def __init__(self) -> None:
        pass