from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from pandas import DataFrame, np
from sklearn import preprocessing
import matplotlib.pyplot as plt


class PortfolioBasics(AbstractPortfolioMeasure):
    _a_title: str = ''
    _a_float: float = -1.1
    _a_suffix: str = ''
    _legend_place: str = ''
    _data: DataFrame = DataFrame()
    _dataBin: DataFrame = DataFrame()
    _dataNorm: DataFrame = DataFrame()
    _dataSparse: DataFrame = DataFrame()
    _dataNormL1: DataFrame = DataFrame()
    _dataScaled: DataFrame = DataFrame()
    _dataLogReturns: DataFrame = DataFrame()

    def __init__(self, y_stocks: list, a_float: float, legend_place: str):
        self._a_float = a_float
        self._legend_place = legend_place
        self._a_suffix = y_stocks[0].SourceColumn
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
        self._dataLogReturns = self._getLogReturns(self._data)

    def Plot(self) -> plt:
        plt.style.use('seaborn')
        plt.rcParams['date.epoch'] = '0000-12-31'
        fig, ax = plt.subplots(5, 1, figsize=(self._a_float, self._a_float/2.0), sharex=True)
        fig.suptitle(self._a_title)
        self._data.plot(ax=ax[0], label=self._data.columns)
        ax[0].set(ylabel='Price $USD')
        ax[0].legend(loc=self._legend_place, fontsize=8)
        self._dataNorm.plot(ax=ax[1], label=self._dataNorm.columns)
        ax[1].set(ylabel='Norm base t(0)')
        ax[1].legend(loc=self._legend_place, fontsize=8)
        self._dataNormL1.plot(ax=ax[2], label=self._dataNormL1.columns)
        ax[2].set(ylabel='Norm L1 base t(0)')
        ax[2].legend(loc=self._legend_place, fontsize=8)
        self._dataScaled.plot(ax=ax[3], label=self._dataScaled.columns)
        ax[3].set(ylabel='Scaled values [0 - 1]')
        ax[3].legend(loc=self._legend_place, fontsize=8)
        self._dataSparse.plot(ax=ax[4], label=self._dataSparse.columns)
        ax[4].set(ylabel='Sparsed values')
        ax[4].legend(loc=self._legend_place, fontsize=8)
        plt.tight_layout()
        return plt

    def _getLogReturns(self, a_df: DataFrame = DataFrame()) -> DataFrame:
        new_df: DataFrame = np.log(a_df/a_df.shift(1))
        new_df.columns = new_df.columns.str.replace(self._a_suffix, 'LogReturn')
        return new_df

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

    @property
    def DataLogReturns(self):
        return self._dataLogReturns
