import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_bmf

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class BmfEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_bmf.BMFExchangeCalendar = mcal.get_calendar('BMF')

    def __init__(self) -> None:
        pass
