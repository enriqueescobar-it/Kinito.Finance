from Common.Predictors.AbstractPredictor import AbstractPredictor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
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
        #independent X
        #convert to ndarray & remove last NaN rows
        self.__x_array = np.array(self.Data.drop([self.__column], 1))
        self.__x_array = self.__x_array[:-self.__forward_span]
        #dependent Y
        #convert to ndarray & remove last NaN rows
        self.__y_array = np.array(self.Data[self.__column])
        self.__y_array = self.__y_array[:-self.__forward_span]
        #split into 80% train / 20% test => 0.2
        X_train, X_test, Y_train, Y_test = train_test_split(self.__x_array, self.__y_array, test_size=0.2)
        #LIN
        self.__model.fit(X_train, Y_train)
        self.Score = self.__model.score(X_test, Y_test)
        print(self.__name + ' Score=', self.Score)
        #LIN predict n days
        self.Prediction = self.__model.predict(self.__forward_array)
