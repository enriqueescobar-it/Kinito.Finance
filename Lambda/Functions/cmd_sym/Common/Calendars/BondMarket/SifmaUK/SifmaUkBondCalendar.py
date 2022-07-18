import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_sifma


from Common.Calendars.BondMarket.AbstractBondCalendar import AbstractBondCalendar


class SifmaUkBondCalendar(AbstractBondCalendar):
    __calendar: exchange_calendar_sifma.SIFMAUKExchangeCalendar = mcal.get_calendar('SIFMAJUK')

    def __init__(self) -> None:
        pass
