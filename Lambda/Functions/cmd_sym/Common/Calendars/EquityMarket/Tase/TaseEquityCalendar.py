import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_tase

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class TaseEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_tase.TASEExchangeCalendar = mcal.get_calendar('TASE')

    def __init__(self) -> None:
        pass