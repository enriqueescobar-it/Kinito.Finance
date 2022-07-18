import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_hkex

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class HkexEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_hkex.HKEXExchangeCalendar = mcal.get_calendar('HKEX')

    def __init__(self) -> None:
        pass