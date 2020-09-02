from abc import *
from pandas import DataFrame
import numpy as np
from Common.Measures.Time.TimeSpan import TimeSpan


class AbstractPredictor(ABC):
    _column: str
    _src_col: str
    _name: str
    _forward_span: int
    _forward_array: np.ndarray
    _prediction: np.ndarray
    _x_array: np.ndarray
    _y_array: np.ndarray
    _data: DataFrame
    _forecast: DataFrame
    _src_data: DataFrame
    _title: str = ' Model '
    _label: str = 'Prediction'
    _x_label: str = 'Days'
    _legendPlace: str = 'upper left'
    _score: float
    _time_span: TimeSpan

    @abstractmethod
    def _setData(self):
        pass

    @abstractmethod
    def _setForecast(self):
        pass

    @abstractmethod
    def _setIndependent(self):
        pass

    @abstractmethod
    def _setDependent(self):
        pass

    def GetScore(self):
        return self._score

    def GetPrediction(self):
        return self._prediction
