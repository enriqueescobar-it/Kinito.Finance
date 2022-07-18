import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_tsx, exchange_calendar_sifma

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class TsxEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_tsx.TSXExchangeCalendar = mcal.get_calendar('TSX')

    def __init__(self) -> None:
        pass