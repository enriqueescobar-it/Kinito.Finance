import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_sse

from Common.Calendars.EquityMarket.AbstractEquityCalendar import AbstractEquityCalendar


class SseEquityCalendar(AbstractEquityCalendar):
    __calendar: exchange_calendar_sse.SSEExchangeCalendar = mcal.get_calendar('SSE')

    def __init__(self) -> None:
        pass
