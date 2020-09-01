from Common.Predictors.AbstractPredictor import AbstractPredictor
from sklearn.linear_model import LinearRegression
from pandas import DataFrame
import numpy as np


class LinearPredictor(AbstractPredictor):
    __model: LinearRegression

    def __init__(self, span: int = 60, a_col: str = 'Adj Close', a_df: DataFrame = DataFrame()):
        self.__forward_span = span
        self.__name = 'LinReg'
        self.__column = 'Prediction' + self.__name + str(span)
        self.Data = a_df[a_col].to_frame()
        self.Data[self.__column] = a_df[[a_col]].shift(-self.__forward_span)
        self.__model = LinearRegression()
        self.__forward_array = np.array(self.Data.drop([self.__column], 1))[-self.__forward_span:]
