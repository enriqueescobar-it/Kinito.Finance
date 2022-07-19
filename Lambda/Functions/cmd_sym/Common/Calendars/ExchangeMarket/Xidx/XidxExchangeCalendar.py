import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xidx

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XidxExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xidx.XIDXExchangeCalendar = xcals.get_calendar('XIDX')

    def __init__(self) -> None:
        pass
