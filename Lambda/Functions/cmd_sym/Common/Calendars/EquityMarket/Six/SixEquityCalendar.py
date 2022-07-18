import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_six

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class SixEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_six.SIXExchangeCalendar = mcal.get_calendar('SIX')

    def __init__(self) -> None:
        pass