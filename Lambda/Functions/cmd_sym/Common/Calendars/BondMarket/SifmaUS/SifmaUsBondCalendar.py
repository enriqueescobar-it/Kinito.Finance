import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_sifma


from Common.Calendars.BondMarket.AbstractBondCalendar import AbstractBondCalendar


class SifmaUsBondCalendar(AbstractBondCalendar):
    __calendar: exchange_calendar_sifma.SIFMAUSExchangeCalendar = mcal.get_calendar('SIFMAJUS')

    def __init__(self) -> None:
        pass
