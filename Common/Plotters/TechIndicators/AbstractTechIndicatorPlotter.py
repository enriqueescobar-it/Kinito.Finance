from abc import ABC
from pandas import DatetimeIndex
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class AbstractTechIndicatorPlotter(ABC):
    _Indicator: AbstractTechIndicator
    __dateTimeIndex: DatetimeIndex
    __Label: str
    __src: str
    __ticker: str
    __timeSpan: TimeSpan
