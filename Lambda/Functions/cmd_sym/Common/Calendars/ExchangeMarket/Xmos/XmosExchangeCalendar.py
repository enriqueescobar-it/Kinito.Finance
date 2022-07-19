import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xmos

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XmosExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xmos.XMOSExchangeCalendar = xcals.get_calendar('XMOS')

    def __init__(self) -> None:
        pass
