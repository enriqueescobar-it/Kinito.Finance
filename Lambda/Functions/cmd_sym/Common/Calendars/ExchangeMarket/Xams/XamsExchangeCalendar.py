import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xams

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XamsExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xams.XAMSExchangeCalendar = xcals.get_calendar('XAMS')

    def __init__(self) -> None:
        pass
