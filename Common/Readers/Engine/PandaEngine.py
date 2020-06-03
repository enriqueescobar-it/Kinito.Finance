from pyarrow.lib import null
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.AbstractEngine import AbstractEngine
import pandas as pd
from pandas_datareader import data


class PandaEngine(AbstractEngine):
    _source: str
    DataFrame: pd.DataFrame

    def __init__(self, source: str = 'yahoo', tm_spn: TimeSpan = null, a_ticker: str = 'CNI'):
        self._source = source
        data_f: pd.DataFrame = data.DataReader(a_ticker, self._source, tm_spn.StartDateStr, tm_spn.EndDateStr)
        data_f.dropna(inplace=True)
        self.DataFrame = data_f
