import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_nyse

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class NyseEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_nyse.NYSEExchangeCalendar = mcal.get_calendar('NYSE')

    def __init__(self) -> None:
        pass