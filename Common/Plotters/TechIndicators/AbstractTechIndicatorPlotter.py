from abc import ABC
from pandas import DatetimeIndex
from Common.Measures.Time.TimeSpan import TimeSpan


class AbstractTechIndicatorsPlotter(ABC):
    __dateTimeIndex: DatetimeIndex
    __Label: str
    __src: str
    __ticker: str
    __timeSpan: TimeSpan
