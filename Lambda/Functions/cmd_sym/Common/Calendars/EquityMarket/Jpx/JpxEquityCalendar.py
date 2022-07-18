import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_jpx, exchange_calendar_sse

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class JpxEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_jpx.JPXExchangeCalendar = mcal.get_calendar('JPX')

    def __init__(self) -> None:
        pass
