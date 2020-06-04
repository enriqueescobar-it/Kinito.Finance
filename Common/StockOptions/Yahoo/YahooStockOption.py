from Common.Drawers.HistoricalDrawer import HistoricalDrawer
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.StockOptions.AbstractStockOption import AbstractStockOption
from Common.WebScrappers.Yahoo.YahooSummaryScrapper import YahooSummaryScrapper
import pandas as pd


class YahooStockOption(AbstractStockOption):
    Ticker: str
    HistoricalData: pd.DataFrame
    YahooSummaryScrapper: YahooSummaryScrapper

    def __init__(self, a_ticker: str = 'CNI'):
        self.Source = 'yahoo'
        self.Ticker = a_ticker
        self._timeSpan = TimeSpan()
        self.YahooSummaryScrapper = YahooSummaryScrapper(a_ticker)
        self.YahooSummaryScrapper.ParseBody()
        self._GetData()
        self._DrawData()

    def _GetData(self):
        self.HistoricalData = PandaEngine(self.Source, self._timeSpan, self.Ticker).DataFrame

    def _DrawData(self):
        HistoricalDrawer(self.HistoricalData, self.Source, self.Ticker, self._timeSpan)
