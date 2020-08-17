from abc import ABC
import pandas as pd

from Common.Measures.Time.TimeSpan import TimeSpan


class AbstractStockMarketIndex(ABC):
    __column: str
    __source: str
    __ticker: str
    __time_sp: TimeSpan
    HistoricalData: pd.DataFrame
