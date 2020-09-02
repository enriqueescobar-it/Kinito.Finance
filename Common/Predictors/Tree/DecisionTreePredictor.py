from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Predictors.AbstractPredictor import AbstractPredictor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt


class DecisionTreePredictor(AbstractPredictor):
    __model: DecisionTreeRegressor
    __label: str = 'Prediction'
    __title: str = ' Model '
    __x_label: str = 'Days'
    __legendPlace: str = 'upper left'

    def __init__(self, span: int = 60, a_col: str = 'Adj Close', a_df: DataFrame = DataFrame(), t_s: TimeSpan = TimeSpan()):
        self.__name = 'DecisionTree'
        self.__model = DecisionTreeRegressor()
        self.__forward_span = span
        print(self.__label)
        self.__column = self.__label + self.__name + str(span)
        self.__src_col = a_col
        self.__src_data = a_df
        self.__setData()
        self.TimeSpan = t_s
        self.__forward_array = np.array(self.Data.drop([self.__column], 1))[-self.__forward_span:]
        self.__setIndependent()
        self.__setDependent()
        # split into 80% train / 20% test => 0.2
        X_train, X_test, Y_train, Y_test = train_test_split(self.__x_array, self.__y_array, test_size=0.2)
        # fit model
        self.__model.fit(self.__x_array, self.__y_array)
        self.Score = round(self.__model.score(X_test, Y_test), 7)
        self.Prediction = self.__model.predict(self.__forward_array)

    def __setData(self):
        self.Data = self.__src_data[self.__src_col].to_frame()
        self.Data[self.__column] = self.__src_data[[self.__src_col]].shift(-self.__forward_span)

    def __setForecast(self):
        self.Forecast = self.__src_data[self.__x_array.shape[0]:]
        self.Forecast[self.__label] = self.Prediction

    def __setIndependent(self):
        # convert to ndarray & remove last NaN rows
        self.__x_array = np.array(self.Data.drop([self.__column], 1))
        self.__x_array = self.__x_array[:-self.__forward_span]

    def __setDependent(self):
        # convert to ndarray & remove last NaN rows
        self.__y_array = np.array(self.Data[self.__column])
        self.__y_array = self.__y_array[:-self.__forward_span]

    def Plot(self):
        plt.figure(figsize=(3 * np.math.log(self.TimeSpan.MonthCount), 4.5))
        plt.tight_layout()
        plt.title(self.__name + ' ' + self.__label + self.__title + 'Score=' + str(self.Score))
        plt.xlabel(self.__x_label)
        plt.ylabel(self.__src_col)
        plt.scatter(self.__src_data.index, self.__src_data[self.__src_col], color='black')
        plt.plot(self.__src_data[self.__src_col])
        plt.plot(self.Forecast[[self.__src_col, self.__label]])
        plt.legend(loc=self.__legendPlace,
                   labels=[self.__src_col, self.__src_col + 'Training', self.__src_col + 'Predicted'])
        return plt
