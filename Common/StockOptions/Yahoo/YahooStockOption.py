from typing import List
from Common.Plotters.HistoricalPlotter import HistoricalDrawer
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.FinVizEngine import FinVizEngine
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine
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
    YeUrl: str
    YeLogoUrl: str
    YeAddress: str
    YeCity: str
    YePostalCode: str
    YeState: str
    YeCountry: str
    Ticker: str
    YssBeta: str
    YssEarningsDate: str
    YssLink: str
    YssMarketCap: str
    YssPeRatio: str
    __yahooSummaryScrapper: YahooSummaryScrapper
    __fin_viz_engine: FinVizEngine
    __y_finance_engine: YahooFinanceEngine

    def __init__(self, a_ticker: str = 'CNI'):
        self.Source = 'yahoo'
        self.Ticker = a_ticker
        self.__timeSpan = TimeSpan()
        self.__fin_viz_engine = FinVizEngine(a_ticker)
        self.__y_finance_engine = YahooFinanceEngine(a_ticker)
        self.__yahooSummaryScrapper = YahooSummaryScrapper(a_ticker)
        self.__yahooSummaryScrapper.ParseBody()
        self._GetName()
        self._GetSector()
        self._GetIndustry()
        self._GetBetaFv()
        self._GetBetaYss()
        self._GetChangePercent()
        self._GetCountry()
        self._GetData()
        self._GetDividend()
        self._GetDividendPercent()
        self._GetEpsTtmFv()
        self._GetEpsYss()
        self._GetEarningsFv()
        self._GetEarningsYss()
        self._GetPeRatioFv()
        self._GetPeRatioYss()
        self._GetHigh52()
        self._GetLinkYss()
        self._GetLow52()
        self._GetMarketCapFv()
        self._GetMarketCapYss()
        self._GetPayout()
        self._GetPrice()
        self._GetRange52()
        self._GetRsi14()
        self._GetVolatility()
        self._GetVolume()
        self._GetYePostalCode()
        #self._DrawData()
        self._GetYeUrl()
        self._GetYeLogoUrl()
        self._GetYeAddress()
        self._GetYeCity()
        self._GetYeState()
        self._GetYePostalCode()
        self._GetYeCountry()

    def _GetData(self):
        self.HistoricalData = PandaEngine(self.Source, self.__timeSpan, self.Ticker).DataFrame

    def _DrawData(self):
        HistoricalDrawer(self.HistoricalData, self.Source, self.Ticker, self.__timeSpan)

    def _GetName(self):
        self.FvCompanyName = self.__fin_viz_engine.StockName

    def _GetSector(self):
        self.FvCompanySector = self.__fin_viz_engine.StockSector

    def _GetIndustry(self):
        self.FvCompanyIndustry = self.__fin_viz_engine.StockIndustry

    def _GetCountry(self):
        self.FvCompanyCountry = self.__fin_viz_engine.StockCountry

    def _GetPeRatioFv(self):
        self.FvPeRatio = self.__fin_viz_engine.PeRatio

    def _GetPeRatioYss(self):
        self.YssPeRatio = self.__yahooSummaryScrapper.PEratio

    def _GetMarketCapFv(self):
        self.FvMarketCap = self.__fin_viz_engine.MarketCap

    def _GetMarketCapYss(self):
        self.YssMarketCap = self.__yahooSummaryScrapper.MarketCap

    def _GetEpsYss(self):
        self.YssEPS = self.__yahooSummaryScrapper.EPS

    def _GetEpsTtmFv(self):
        self.FvEPS = self.__fin_viz_engine.EpsTtm

    def _GetBetaFv(self):
        self.FvBeta = self.__fin_viz_engine.Beta

    def _GetBetaYss(self):
        self.YssBeta = self.__yahooSummaryScrapper.Beta

    def _GetEarningsFv(self):
        self.FvEarnings = self.__fin_viz_engine.EarningDate

    def _GetEarningsYss(self):
        self.YssEarningsDate = self.__yahooSummaryScrapper.EarningsDate

    def _GetLinkYss(self):
        self.YssLink = self.__yahooSummaryScrapper.Link

    def _GetLow52(self):
        self.FvLow52 = self.__fin_viz_engine.Low52

    def _GetHigh52(self):
        self.FvHigh52 = self.__fin_viz_engine.High52

    def _GetRange52(self):
        self.FvRange52 = self.__fin_viz_engine.Range52

    def _GetRsi14(self):
        self.FvRsi14 = self.__fin_viz_engine.Rsi14

    def _GetVolatility(self):
        self.FvVolatility = self.__fin_viz_engine.Volatility

    def _GetPayout(self):
        self.FvPayout = self.__fin_viz_engine.PayoutPcnt

    def _GetVolume(self):
        self.FvVolume = self.__fin_viz_engine.Volume

    def _GetChangePercent(self):
        self.FvChangePercent = self.__fin_viz_engine.ChangePcnt

    def _GetPrice(self):
        self.FvPrice = self.__fin_viz_engine.Price

    def _GetDividend(self):
        self.FvDividend = self.__fin_viz_engine.Dividend

    def _GetDividendPercent(self):
        self.FvDividendPercent = self.__fin_viz_engine.DividendPcnt

    def _GetYeUrl(self):
        self.YeUrl = self.__y_finance_engine.Url

    def _GetYeLogoUrl(self):
        self.YeLogoUrl = self.__y_finance_engine.LogoUrl

    def _GetYeAddress(self):
        self.YeAddress = self.__y_finance_engine.Address

    def _GetYeCity(self):
        self.YeCity = self.__y_finance_engine.City

    def _GetYePostalCode(self):
        self.YePostalCode = self.__y_finance_engine.PostalCode

    def _GetYeState(self):
        self.YeState = self.__y_finance_engine.State

    def _GetYeCountry(self):
        self.YeCountry = self.__y_finance_engine.Country
