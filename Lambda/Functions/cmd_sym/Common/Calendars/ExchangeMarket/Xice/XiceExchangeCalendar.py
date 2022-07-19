import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xice

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XiceExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xice.XICEExchangeCalendar = xcals.get_calendar('XICE')

    def __init__(self) -> None:
        pass
