from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Predictors.AbstractPredictor import AbstractPredictor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from pandas import DataFrame
from numpy import ndarray
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt


class DecisionTreePredictor(AbstractPredictor):
    __model: DecisionTreeRegressor
    Xarray: ndarray
    Yarray: ndarray

    def __init__(self, span: int = 60, a_col: str = 'Adj Close', a_df: DataFrame = DataFrame()):
        self.__name = 'DecisionTree'
        self.__model = DecisionTreeRegressor()
        self.__forward_span = span
        self.__column = self.__label + self.__name + str(span)
        self.__src_col = a_col
        self.Data = a_df[a_col].to_frame()
        self.Data[self.__column] = a_df[[a_col]].shift(-span)
        self.__forward_array = np.array(self.Data.drop([self.__column], 1))[-self.__forward_span:]
        self.__setIndependant()
        self.__setDependant()
        #split into 80% train / 20% test => 0.2
        X_train, X_test, Y_train, Y_test = train_test_split(self.Xarray, self.Yarray, test_size=0.2)
        #fit model
        self.__model.fit(self.Xarray, self.Yarray)
        self.Score = round(self.__model.score(X_test, Y_test), 5)
        self.Prediction = self.__model.predict(self.__forward_array)

    def __setIndependant(self):
        #convert to ndarray & remove last NaN rows
        self.Xarray = np.array(self.Data.drop([self.__column], 1))
        self.Xarray = self.Xarray[:-self.__forward_span]

    def __setDependant(self):
        #convert to ndarray & remove last NaN rows
        self.Yarray = np.array(self.Data[self.__column])
        self.Yarray = self.Yarray[:-self.__forward_span]

    def Plot(self, t_s: TimeSpan = TimeSpan()):
        plt.figure(figsize=(3 * np.math.log(t_s.MonthCount), 4.5))
        plt.tight_layout()
        plt.title(self.__name + ' ' + self.__label + self.__title + 'Score=' + str(self.Score))
        plt.xlabel(self.__x_label)
        plt.ylabel(self.__src_col)
        return plt
