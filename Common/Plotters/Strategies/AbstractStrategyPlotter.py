from abc import ABC


class AbstractStrategyPlotter(ABC):
    __LEGEND_PLACE: str
    __SOURCE: str
    __TICKER: str
    __XTICKS_ANGLE: int

