from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame
from sklearn import preprocessing


class PortfolioBasics(AbstractPortfolioMeasure):
    _a_title: str = ''
    _data: DataFrame = DataFrame()
    _dataBin: DataFrame = DataFrame()
    _dataNorm: DataFrame = DataFrame()
    _dataSparse: DataFrame = DataFrame()
    _dataNormL1: DataFrame = DataFrame()
    _dataScaled: DataFrame = DataFrame()

    def __init__(self, y_stocks: list):
        for y_stock in y_stocks:
            self._a_title += y_stock.Ticker + ' '
            self._data[y_stock.Ticker + y_stock.SourceColumn] = y_stock.Data[y_stock.SourceColumn]
            self._dataBin[y_stock.Ticker + 'Binary'] = y_stock.Data['Binary']
            self._dataNorm[y_stock.Ticker + 'Norm'] = y_stock.Data['Norm']
            # self._dataNormL1[y_stock.Ticker + 'NormL1'] = y_stock.Data['NormL1']
            self._dataSparse[y_stock.Ticker + 'Sparse'] = y_stock.Data['Sparse']
            # self._dataScaled[y_stock.Ticker + 'Scaled'] = y_stock.Data['Scaled']

        arrayNormL1 = preprocessing.normalize(self._data, norm='l1')
        self._dataNormL1 = DataFrame(arrayNormL1, columns=self._data.columns, index=self._data.index)
        self._dataNormL1.columns = self._dataNormL1.columns.str.replace(y_stocks[0].SourceColumn, 'NormL1')
        arrayScaled = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(self._data)
        self._dataScaled = DataFrame(arrayScaled, columns=self._data.columns, index=self._data.index)
        self._dataScaled.columns = self._dataScaled.columns.str.replace(y_stocks[0].SourceColumn, 'Scaled')
        self._dataSparse = DataFrame(preprocessing.scale(self._data), columns=self._data.columns,
                                     index=self._data.index)
        self._dataSparse.columns = self._dataSparse.columns.str.replace(y_stocks[0].SourceColumn, 'Sparse')

    @property
    def Title(self):
        return self._a_title

    @property
    def Data(self):
        return self._data

    @property
    def DataBin(self):
        return self._dataBin

    @property
    def DataNorm(self):
        return self._dataNorm

    @property
    def DataNormL1(self):
        return self._dataNormL1

    @property
    def DataSparse(self):
        return self._dataSparse

    @property
    def DataScaled(self):
        return self._dataScaled
