import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_cme

from Common.Calendars.FutureMarket.AbstractFutureCalendar import AbstractFutureCalendar


class CmeAgriculturalFutureCalendar(AbstractFutureCalendar):
    __calendar: exchange_calendar_cme.CMEAgricultureExchangeCalendar = mcal.get_calendar('CME_Agricultural')

    def __init__(self) -> None:
        pass