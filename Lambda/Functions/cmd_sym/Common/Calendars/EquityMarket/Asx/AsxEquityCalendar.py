import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_asx

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class AsxEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_asx.ASXExchangeCalendar = mcal.get_calendar('ASX')

    def __init__(self) -> None:
        pass