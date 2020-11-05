from abc import *
from pandas import DataFrame
from numpy import ndarray
from pyarrow.lib import null
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.PandaEngine import PandaEngine


class AbstractStockMarketIndex(ABC):
    _column: str = ''
    _name: str = ''
    _source: str = ''
    _ticker: str = ''
    _time_sp: TimeSpan
    _toUsd: float = -1.1
    _data: DataFrame = DataFrame()
    _data_norm: DataFrame = DataFrame()
    _data_scaled: DataFrame = DataFrame()

    def __init__(self, source: str = 'yahoo', name: str = 'CboeVolat', column: str = 'Adj Close', ticker: str = "^VIX",
                 tm_spn: TimeSpan = null, to_usd: float = 1.0):
        self._source = source
        self._name = name
        self._column = column
        self._ticker = ticker
        self._time_sp = tm_spn
        self._toUsd = to_usd
        self._data = PandaEngine(source, tm_spn, ticker).DataFrame
        self._data.fillna(method='ffill', inplace=True)
        self._data.fillna(method='bfill', inplace=True)
        self._data = self._data[self._column].to_frame() / self._toUsd
        self._data.columns =\
            [x.replace(self._column, self._name + self._column) for x in self._data.columns]
        self._data_scaled = self._getDataScaled()
        self._data_norm = self._getDataNorm()

    def _getDataScaled(self) -> DataFrame:
        # scale to compare array from 0.0 to 100.0
        minMaxScaler: MinMaxScaler = preprocessing.MinMaxScaler(feature_range=(0.0, 100.0))
        # scale to compare data frame
        stockArrayScaled: ndarray = minMaxScaler.fit_transform(self._data)
        a_df: DataFrame =\
            DataFrame(stockArrayScaled, columns=self._data.columns, index=self._data.index)
        a_df.columns = [x.replace(self._column, 'Scaled') for x in a_df.columns]
        return a_df

    def _getDataNorm(self) -> DataFrame:
        a_df: DataFrame = self._data / self._data.iloc[0]
        a_df.columns = [x.replace(self._column, 'Norm') for x in a_df.columns]
        return a_df

    def _getSimpleReturns(self, a_letter: str = '') -> DataFrame:
        new_df: DataFrame() = DataFrame()
        if a_letter == 'W':
            new_df = self._data[self._data.columns].resample('W').ffill().pct_change()
        elif a_letter == 'M':
            new_df = self._data[self._data.columns].resample('M').ffill().pct_change()
        elif a_letter == 'Q':
            new_df = self._data[self._data.columns].resample('Q').ffill().pct_change()
        elif a_letter == 'A':
            new_df = self._data[self._data.columns].resample('A').ffill().pct_change()
        else:
            new_df = self._data[self._data.columns].pct_change()
        new_df.columns = [x.replace(self._data.columns, a_letter.lower()) for x in self._data.columns]
        new_df.iloc[0, :] = 0
        return new_df

    @property
    def Data(self):
        return self._data

    @property
    def DataNorm(self):
        return self._data_norm

    @property
    def DataScaled(self):
        return self._data_scaled
