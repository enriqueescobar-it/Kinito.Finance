import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_cme

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class CmeCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_cme.CMEEquityExchangeCalendar = mcal.get_calendar('CME')

    def __init__(self) -> None:
        pass