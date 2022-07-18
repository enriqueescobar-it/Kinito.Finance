import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_ose

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class OseEquityCaalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_ose.OSEExchangeCalendar = mcal.get_calendar('OSE')

    def __init__(self) -> None:
        pass
