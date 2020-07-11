from abc import ABC
import pandas as pd
from pyarrow.lib import null
from Common.Measures.Time.TimeSpan import TimeSpan


class AbstractPlotter(ABC):
    _dataFrame: pd.DataFrame
    _source: str
    _draw_col: str
    _legend_place: str
    _ticker: str
    _time_span: TimeSpan

    def __init__(self, df: pd.DataFrame, src: str = 'yahoo', tick: str = 'CNI', ts: TimeSpan = null):
        self._dataFrame = df
        self._source = src
        self._legend_place = 'upper left'
        self._ticker = tick
        self._time_span = ts

    def Plot(self):
        pass
