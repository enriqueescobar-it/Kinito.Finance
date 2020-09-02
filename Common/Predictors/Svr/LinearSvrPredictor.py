from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Predictors.AbstractSvrPredictor import AbstractSvrPredictor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt


class LinearSvrPredictor(AbstractSvrPredictor):
    __model: SVR
    _name = 'LinearSVR'

    def __init__(self, span: int = 60, a_col: str = 'Adj Close', a_df: DataFrame = DataFrame(), t_s: TimeSpan = TimeSpan()):
        self.__model = SVR(kernel='linear', C=1e3)
        self._forward_span = span
        print(self._label)
        self._column = self._label + self._name + str(span)
        print(self._column)
        self._src_col = a_col
        self._src_data = a_df
        self._setData()
        self._time_span = t_s
        self._forward_array = np.array(self._data.drop([self._column], 1))[-self._forward_span:]
        self._setIndependent()
        self._setDependent()
        # split into 80% train / 20% test => 0.2
        X_train, X_test, Y_train, Y_test = train_test_split(self._x_array, self._y_array, test_size=0.2)
        print('train_test_split')
        # fit model TRAINED
        self.__model.fit(X_train, Y_train)
        print('train_test_fit')
        # score TESTED
        self._score = round(self.__model.score(X_test, Y_test), 7)
        self._prediction = self.__model.predict(self._forward_array)
        print('train_test_forecast')
        self._setForecast()

    def _setData(self):
        print('SET DATA')
        self._data = self._src_data[self._src_col].to_frame()
        self._data[self._column] = self._src_data[[self._src_col]].shift(-self._forward_span)

    def _setForecast(self):
        print('SET FORECAST')
        self._forecast = self._src_data[self._x_array.shape[0]:]
        self._forecast[self._label] = self._prediction

    def _setIndependent(self):
        print('SET INDEP')
        # convert to ndarray & remove last NaN rows
        self._x_array = np.array(self._data.drop([self._column], 1))
        self._x_array = self._x_array[:-self._forward_span]

    def _setDependent(self):
        print('SET DEP')
        # convert to ndarray & remove last NaN rows
        self._y_array = np.array(self._data[self._column])
        self._y_array = self._y_array[:-self._forward_span]

    def Plot(self):
        plt.figure(figsize=(3 * np.math.log(self._time_span.MonthCount), 4.5))
        plt.tight_layout()
        plt.title(self._name + ' ' + self._label + self._title + 'Score=' + str(self._score))
        plt.xlabel(self._x_label)
        plt.ylabel(self._src_col)
        plt.scatter(self._src_data.index, self._src_data[self._src_col], color='black')
        plt.plot(self._src_data[self._src_col])
        plt.plot(self._forecast[[self._src_col, self._label]])
        plt.legend(loc=self._legendPlace,
                   labels=[self._src_col, self._src_col + 'Training', self._src_col + 'Predicted'])
        return plt
