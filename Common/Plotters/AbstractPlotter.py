from abc import ABC
import pandas as pd
from pyarrow.lib import null
from Common.Measures.Time.TimeSpan import TimeSpan


class AbstractPlotter(ABC):
    _dataFrame: pd.DataFrame
    _src: str
    _draw_col: str
    _legend_place: str
    _ticker: str
    _timeSpan: TimeSpan

    def __init__(self, df: pd.DataFrame, src: str = 'yahoo', tick: str = 'CNI', ts: TimeSpan = null):
        self._dataFrame = df
        self._src = src
        self._legend_place = 'upper left'
        self._ticker = tick
        self._timeSpan = ts

    def Plot(self):
        pass
