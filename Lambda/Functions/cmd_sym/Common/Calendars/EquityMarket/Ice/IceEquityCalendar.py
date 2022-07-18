import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_ice

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class IceEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_ice.ICEExchangeCalendar = mcal.get_calendar('ICE')

    def __init__(self) -> None:
        pass
