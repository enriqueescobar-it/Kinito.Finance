import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_xtai

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class XtaiExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_xtai.XTAIExchangeCalendar = xcals.get_calendar('XTAI')

    def __init__(self) -> None:
        pass
