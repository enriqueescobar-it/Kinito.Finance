from numpy.core._multiarray_umath import ndarray

from Common.Predictors.AbstractPredictor import AbstractPredictor
from Common.Measures.Time.TimeSpan import TimeSpan
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt


class KerasPredictor(AbstractPredictor):
    __model: Sequential
    _name = 'Keras'

    def __init__(self, span: int = 60, a_col: str = 'Adj Close', a_df: DataFrame = DataFrame(), t_s: TimeSpan = TimeSpan()):
        self._forward_span = span
        print(self._label)
        self._column = self._label + self._name + str(span)
        print(self._column)
        self._src_col = a_col
        self._src_data = a_df
        self._setData()
        self._time_span = t_s
        dataSet: ndarray = self._data[self._src_col].values
        print(dataSet.shape)
        dataLength = np.math.ceil(len(dataSet) * 0.8)
        scale = MinMaxScaler(feature_range=(0, 1))
        dataScaled = scale.fit_transform(dataSet.reshape(-1, 1))
        dataTrained = dataScaled[0:dataLength, :]
        x_train = []
        y_train = []
        for i in range (self._forward_span, len(dataTrained)):
            x_train.append(dataTrained[i-self._forward_span:self._forward_span, 0])
            y_train.append(dataTrained[self._forward_span, 0])
        x_train, y_train = np.array(x_train), np.array(y_train)
        print('0', x_train.shape[0])
        print('1', x_train.shape)
        x_train = np.reshape(x_train, (x_train.shape[0], 1, 1))
        print('X_T shape', x_train.shape)
        self.__model = Sequential()
        self.__model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        self.__model.add(LSTM(50, return_sequences=False))
        self.__model.add(Dense(25))
        self.__model.add(Dense(1))
        self.__model.compile(optimizer='adam', loss='mean_squared_error')

    def _setData(self):
        print('col_src', self._src_col)
        print('col_new', self._column)
        self._data = self._src_data[self._src_col].to_frame()
        self._data[self._column] = self._src_data[[self._src_col]].shift(-self._forward_span)
        print('data_src', self._data.shape)
        print('data_new', self._data.head(1))

    def _setForecast(self):
        pass

    def _setIndependent(self):
        pass

    def _setDependent(self):
        pass
