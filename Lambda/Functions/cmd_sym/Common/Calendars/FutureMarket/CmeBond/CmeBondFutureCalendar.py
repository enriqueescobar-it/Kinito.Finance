import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_cme

from Common.Calendars.FutureMarket.AbstractFutureCalendar import AbstractFutureCalendar


class CmeBondFutureCalendar(AbstractFutureCalendar):
    __calendar: exchange_calendar_cme.CMEBondExchangeCalendar = mcal.get_calendar('CME_Bond')

    def __init__(self) -> None:
        pass