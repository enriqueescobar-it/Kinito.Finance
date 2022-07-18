import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_bse

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class BseEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_bse.BSEExchangeCalendar = mcal.get_calendar('BSE')

    def __init__(self) -> None:
        pass