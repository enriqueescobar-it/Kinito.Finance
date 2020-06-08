from typing import List
from Common.Drawers.HistoricalDrawer import HistoricalDrawer
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.FinVizEngine import FinVizEngine
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.StockOptions.AbstractStockOption import AbstractStockOption
from Common.WebScrappers.Yahoo.YahooSummaryScrapper import YahooSummaryScrapper
import pandas as pd


class YahooStockOption(AbstractStockOption):
    FvBeta: float
    FvChangePercent: str
    FvCompanyCountry: str
    FvCompanyIndustry: str
    FvCompanyName: str
    FvCompanySector: str
    FvDividend: str
    FvDividendPercent: str
    FvEPS: float
    FvEarnings: str
    FvMarketCap: int
    FvPayout: str
    FvPeRatio: float
    FvLow52: str
    FvHigh52: str
    FvPrice: float
    FvRange52: List[float]
    FvRsi14: str
    FvVolume: int
    HistoricalData: pd.DataFrame
    Ticker: str
    YahooSummaryScrapper: YahooSummaryScrapper
    _fin_viz_engine: FinVizEngine

    def __init__(self, a_ticker: str = 'CNI'):
        self.Source = 'yahoo'
        self.Ticker = a_ticker
        self._timeSpan = TimeSpan()
        self.YahooSummaryScrapper = YahooSummaryScrapper(a_ticker)
        self.YahooSummaryScrapper.ParseBody()
        self._fin_viz_engine = FinVizEngine(a_ticker)
        self._GetName()
        self._GetSector()
        self._GetIndustry()
        self._GetBetaFv()
        self._GetChangePercent()
        self._GetCountry()
        self._GetData()
        self._GetDividend()
        self._GetDividendPercent()
        self._GetEpsTtmFv()
        self._GetEarningsFv()
        self._GetPeRatioFv()
        self._GetHigh52()
        self._GetLow52()
        self._GetMarketCapFv()
        self._GetPayout()
        self._GetPrice()
        self._GetRange52()
        self._GetRsi14()
        self._GetVolatility()
        self._GetVolume()
        #self._DrawData()

    def _GetData(self):
        self.HistoricalData = PandaEngine(self.Source, self._timeSpan, self.Ticker).DataFrame

    def _DrawData(self):
        HistoricalDrawer(self.HistoricalData, self.Source, self.Ticker, self._timeSpan)

    def _GetName(self):
        self.FvCompanyName = self._fin_viz_engine.StockName

    def _GetSector(self):
        self.FvCompanySector = self._fin_viz_engine.StockSector

    def _GetIndustry(self):
        self.FvCompanyIndustry = self._fin_viz_engine.StockIndustry

    def _GetCountry(self):
        self.FvCompanyCountry = self._fin_viz_engine.StockCountry

    def _GetPeRatioFv(self):
        self.FvPeRatio = self._fin_viz_engine.PeRatio

    def _GetMarketCapFv(self):
        self.FvMarketCap = self._fin_viz_engine.MarketCap

    def _GetEpsTtmFv(self):
        self.FvEPS = self._fin_viz_engine.EpsTtm

    def _GetBetaFv(self):
        self.FvBeta = self._fin_viz_engine.Beta

    def _GetEarningsFv(self):
        self.FvEarnings = self._fin_viz_engine.EarningDate

    def _GetLow52(self):
        self.FvLow52 = self._fin_viz_engine.Low52

    def _GetHigh52(self):
        self.FvHigh52 = self._fin_viz_engine.High52

    def _GetRange52(self):
        self.FvRange52 = self._fin_viz_engine.Range52

    def _GetRsi14(self):
        self.FvRsi14 = self._fin_viz_engine.Rsi14

    def _GetVolatility(self):
        self.FvVolatility = self._fin_viz_engine.Volatility

    def _GetPayout(self):
        self.FvPayout = self._fin_viz_engine.PayoutPcnt

    def _GetVolume(self):
        self.FvVolume = self._fin_viz_engine.Volume

    def _GetChangePercent(self):
        self.FvChangePercent = self._fin_viz_engine.ChangePcnt

    def _GetPrice(self):
        self.FvPrice = self._fin_viz_engine.Price

    def _GetDividend(self):
        self.FvDividend = self._fin_viz_engine.Dividend

    def _GetDividendPercent(self):
        self.FvDividendPercent = self._fin_viz_engine.DividendPcnt
