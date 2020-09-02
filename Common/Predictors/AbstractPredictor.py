from abc import ABC
from pandas import DataFrame
import numpy as np
from Common.Measures.Time.TimeSpan import TimeSpan


class AbstractPredictor(ABC):
    __forward_span: int
    __forward_array: np.ndarray
    __column: str
    __src_col: str
    __name: str
    __x_array: np.ndarray
    __y_array: np.ndarray
    __src_data: DataFrame
    Data: DataFrame
    Score: float
    Prediction: np.ndarray
    TimeSpan: TimeSpan
