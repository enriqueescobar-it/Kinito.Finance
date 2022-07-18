import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_eurex

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class EurexEquityCale(AbstractEquityCalendar):
    __calendar: exchange_calendar_eurex.EUREXExchangeCalendar = mcal.get_calendar('EUREX')

    def __init__(self) -> None:
        pass