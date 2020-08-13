from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from pyarrow.lib import null


class SnPTSXComposite(AbstractStockMarketIndex):

    def __init__(self, source: str = 'yahoo', ticker: str = '^GSPTSE', tm_spn: TimeSpan = null):
        self.__source = source
        self.__ticker = ticker
        self.__time_sp = tm_spn
        self._historical_data = PandaEngine(source, tm_spn, ticker).DataFrame
        self._historical_data.fillna(method='ffill', inplace=True)
        self._historical_data.fillna(method='bfill', inplace=True)
