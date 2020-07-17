from abc import ABC
from typing import Tuple


class AbstractStrategyPlotter(ABC):
    __FIG_SIZE: Tuple[float, float]
    __LEGEND_PLACE: str
    __PLOT_STYLE: str
    __SOURCE: str
    __TITLE: str
    __TICKER: str
    __XLABEL: str
    __XTICKS_ANGLE: int
    __YLABEL: str

