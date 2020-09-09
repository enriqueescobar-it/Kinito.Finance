from abc import ABC
import pandas as pd


class AbstractStrategyPlotter(ABC):
    __DATE_TIME_INDEX: pd.core.indexes.datetimes.DatetimeIndex

