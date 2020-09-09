from abc import ABC
import pandas as pd


class AbstractStrategyPlotter(ABC):
    _PLOT_STYLE: str = 'fivethirtyeight'
    __SOURCE: str
    __TICKER: str
    __TICKER_LABEL: str
    __DATE_TIME_INDEX: pd.core.indexes.datetimes.DatetimeIndex
    __STRATEGY_DATA_BUY: pd.core.series.Series
    __STRATEGY_DATA_SELL: pd.core.series.Series
    __STRATEGY_LABEL: str
    __STRATEGY_LABEL_BUY: str
    __STRATEGY_LABEL_SELL: str

