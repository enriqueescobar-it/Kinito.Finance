from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from pyarrow.lib import null


class Nikkei225Index(AbstractStockMarketIndex):

    def __init__(self, source: str = 'yahoo', ticker: str = "^N225", tm_spn: TimeSpan = null):
        self.__column = 'Adj Close'
        self.__name = 'Nikkei 225'
        self.__source = source
        self.__ticker = "^N225" if source == 'yahoo' else ticker
        self.__time_sp = tm_spn
        self.__toUsd = 0.009
        self.HistoricalData = PandaEngine(source, tm_spn, ticker).DataFrame
        self.HistoricalData.fillna(method='ffill', inplace=True)
        self.HistoricalData.fillna(method='bfill', inplace=True)
        self.HistoricalData = self.HistoricalData[self.__column].to_frame()
        self.HistoricalData = self.HistoricalData * self.__toUsd
        self.HistoricalData.columns = [x.replace(self.__column, self.__name + self.__column) for x in self.HistoricalData.columns]
