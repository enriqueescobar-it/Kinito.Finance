from abc import ABC
from typing import Tuple
import pandas as pd


class AbstractStrategyPlotter(ABC):
    _FIG_SIZE: Tuple[float, float] = (8.2, 4.5)
    _LEGEND_PLACE: str = 'upper left'
    _PLOT_STYLE: str = 'fivethirtyeight'
    _XTICKS_ANGLE: int = 45
    __SOURCE: str
    __TICKER: str
    __TICKER_LABEL: str
    __TITLE: str
    __XLABEL: str
    __YLABEL: str
    __DATE_TIME_INDEX: pd.core.indexes.datetimes.DatetimeIndex
    __STRATEGY_DATA_FRAME: pd.DataFrame
    __STRATEGY_DATA_BUY: pd.core.series.Series
    __STRATEGY_DATA_SELL: pd.core.series.Series
    __STRATEGY_LABEL: str
    __STRATEGY_LABEL_BUY: str
    __STRATEGY_LABEL_SELL: str

