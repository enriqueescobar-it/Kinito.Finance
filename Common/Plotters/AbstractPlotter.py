from abc import *
from pandas import DataFrame
from Common.Measures.Time.TimeSpan import TimeSpan


class AbstractPlotter(ABC):
    _data_frame: DataFrame
    _src: str
    _col: str
    _legend_place: str
    _ticker: str
    _time_span: TimeSpan

