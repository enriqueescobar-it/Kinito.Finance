from abc import ABC
from pandas import DataFrame
import numpy as np


class AbstractPredictor(ABC):
    __forward_span: int
    __forward_array: np.ndarray
    __column: str
    __name: str
    Data: DataFrame
