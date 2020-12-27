from keras.models import Sequential

from Common.Predictors.AbstractPredictor import AbstractPredictor
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class MlPredictor(AbstractPredictor):
    __model: Sequential
    __y_stock: YahooStockOption
    _name = 'MachineLearning'

    def __init__(self, stock_option: YahooStockOption, span: int = 60):
        self._forward_span = span
        print(self._label)
        self._column = self._label + self._name + str(span)
        print(self._column)
        self._src_col = stock_option.Column
        self._src_data = stock_option.DataFrame
        self._setData()

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
