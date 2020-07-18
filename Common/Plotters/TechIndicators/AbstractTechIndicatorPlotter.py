from abc import ABC
from typing import Tuple
from pandas import DatetimeIndex
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class AbstractTechIndicatorPlotter(ABC):
    __FIG_SIZE: Tuple[float, float]
    __LEGEND_PLACE: str
    __PLOT_STYLE: str
    __SOURCE: str
    __TICKER: str
    _Indicator: AbstractTechIndicator
    __dateTimeIndex: DatetimeIndex
    __Label: str
    __timeSpan: TimeSpan
