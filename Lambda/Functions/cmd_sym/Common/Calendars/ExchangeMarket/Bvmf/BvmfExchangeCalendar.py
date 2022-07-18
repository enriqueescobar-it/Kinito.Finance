import exchange_calendars as xcals
from exchange_calendars import exchange_calendar_bvmf

from Common.Calendars.ExchangeMarket.AbstractExchangeCalendar import AbstractExchangeCalendar


class BvmfExchangeCalendar(AbstractExchangeCalendar):
    __calendar: exchange_calendar_bvmf.BVMFExchangeCalendar = xcals.get_calendar('BVMF')

    def __init__(self) -> None:
        pass