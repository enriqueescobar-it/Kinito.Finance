from abc import ABC
from typing import Tuple
import pandas as pd


class AbstractStrategyPlotter(ABC):
    __FIG_SIZE: Tuple[float, float]
    __LEGEND_PLACE: str
    __PLOT_STYLE: str
    __SOURCE: str
    __TITLE: str
    __TICKER: str
    __TICKER_LABEL: str
    __XLABEL: str
    __XTICKS_ANGLE: int
    __YLABEL: str
    __DATE_TIME_INDEX: pd.core.indexes.datetimes.DatetimeIndex
    __STRATEGY_DATA_FRAME: pd.DataFrame
    __STRATEGY_DATA_BUY: pd.core.series.Series
    __STRATEGY_DATA_SELL: pd.core.series.Series
    __STRATEGY_LABEL: str
    __STRATEGY_LABEL_BUY: str
    __STRATEGY_LABEL_SELL: str

