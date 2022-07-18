import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_lse

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class LseCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_lse.LSEExchangeCalendar = mcal.get_calendar('LSE')

    def __init__(self) -> None:
        pass
