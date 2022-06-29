from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from Common.Markets.AbstractMarket import AbstractMarket


class AbstractMarketIndex(AbstractMarket):

    _column: str = ''
    _name: str = ''
    _source: str = ''
    _ticker: str = ''
    _to_usd: float = -1.1
    _data: DataFrame = DataFrame()
    _data_norm: DataFrame = DataFrame()
    _data_scaled: DataFrame = DataFrame()

    def __init__(self, source: str = 'yahoo', name: str = 'CboeVolat', column: str = 'Adj Close', ticker: str = "^VIX",
                 to_usd: float = 1.0) -> None:
        self._source = source
        self._name = name
        self._column = column
        self._ticker = ticker
        self._to_usd = to_usd
        self._set_data()
        self._set_data_norm()
        self._set_data_scaled()

    def _set_data(self):
        # self._data = PandaEngine(source, tm_spn, ticker).DataFrame
        self._data.fillna(method='ffill', inplace=True)
        self._data.fillna(method='bfill', inplace=True)
        self._data = self._data[self._column].to_frame() / self._to_usd
        self._data.columns = \
            [x.replace(self._column, self._name + self._column) for x in self._data.columns]

    def _set_data_norm(self):
        a_df: DataFrame = self._data / self._data.iloc[0]
        a_df.columns = [x.replace(self._column, 'Norm') for x in a_df.columns]
        self._data_norm = a_df

    def _set_data_scaled(self):
        # scale to compare array from 0.0 to 100.0
        min_max_scaler: MinMaxScaler = preprocessing.MinMaxScaler(feature_range=(0.0, 100.0))
        # scale to compare data frame
        min_max_scaled_array: ndarray = min_max_scaler.fit_transform(self._data)
        # to data frame
        a_df: DataFrame = DataFrame(min_max_scaled_array, columns=self._data.columns, index=self._data.index)
        a_df.columns = [x.replace(self._column, 'Scaled') for x in a_df.columns]
        self._data_scaled = a_df

    @property
    def Data(self) -> DataFrame:
        return self._data

    @property
    def DataNorm(self) -> DataFrame:
        return self._data_norm

    @property
    def DataScaled(self) -> DataFrame:
        return self._data_scaled
