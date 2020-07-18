from abc import ABC
from typing import Tuple
from pandas import DatetimeIndex
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class AbstractTechIndicatorPlotter(ABC):
    __ABSTRACT_INDICATOR: AbstractTechIndicator
    __DATE_TIME_INDEX: DatetimeIndex
    __FIG_SIZE: Tuple[float, float]
    __LEGEND_PLACE: str
    __PLOT_STYLE: str
    __SOURCE: str
    __TICKER: str
    __TICKER_LABEL: str
    __TITLE: str
    __XLABEL: str
    __XTICKS_ANGLE: int
    __YLABEL: str
