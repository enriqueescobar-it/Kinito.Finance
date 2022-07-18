import pandas_market_calendars as mcal
from pandas_market_calendars import exchange_calendar_sifma


from Common.Calendars.BondMarket.AbstractBondCalendar import AbstractBondCalendar


class SifmaJpBondCalendar(AbstractBondCalendar):
    __calendar: exchange_calendar_sifma.SIFMAJPExchangeCalendar = mcal.get_calendar('SIFMAJP')

    def __init__(self) -> None:
        pass
