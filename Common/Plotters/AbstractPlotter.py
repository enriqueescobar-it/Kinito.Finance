from abc import ABC
import pandas as pd
from Common.Measures.Time.TimeSpan import TimeSpan


class AbstractPlotter(ABC):
    __dataFrame: pd.DataFrame
    __src: str
    __Col: str
    __legendPlace: str
    __ticker: str
    __timeSpan: TimeSpan

