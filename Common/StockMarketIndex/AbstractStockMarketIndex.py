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
    HistoricalData: DataFrame = DataFrame()
    DataNorm: DataFrame = DataFrame()
    DataScaled: DataFrame = DataFrame()

    def __init__(self, source: str = 'yahoo', name: str = 'CboeVolat', column: str = 'Adj Close', ticker: str = "^VIX",
                 tm_spn: TimeSpan = null, to_usd: float = 1.0):
        self._source = source
        self._name = name
        self._column = column
        self._ticker = ticker
        self._time_sp = tm_spn
        self._toUsd = to_usd
        self.HistoricalData = PandaEngine(source, tm_spn, ticker).DataFrame
        self.HistoricalData.fillna(method='ffill', inplace=True)
        self.HistoricalData.fillna(method='bfill', inplace=True)
        self.HistoricalData = self.HistoricalData[self._column].to_frame()
        self.HistoricalData.columns =\
            [x.replace(self._column, self._name + self._column) for x in self.HistoricalData.columns]
        self.DataScaled = self._getDataScaled()
        self.DataNorm = self._getDataNorm()

    def _getDataScaled(self) -> DataFrame:
        # scale to compare array from 0.0 to 100.0
        minMaxScaler: MinMaxScaler = preprocessing.MinMaxScaler(feature_range=(0.0, 100.0))
        # scale to compare data frame
        stockArrayScaled: ndarray = minMaxScaler.fit_transform(self.HistoricalData)
        a_df: DataFrame =\
            DataFrame(stockArrayScaled, columns=self.HistoricalData.columns, index=self.HistoricalData.index)
        a_df.columns = [x.replace(self._column, 'Scaled') for x in a_df.columns]
        return a_df

    def _getDataNorm(self) -> DataFrame:
        a_df: DataFrame = self.HistoricalData / self.HistoricalData.iloc[0]
        a_df.columns = [x.replace(self._column, 'Norm') for x in a_df.columns]
        return a_df
