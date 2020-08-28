from typing import List
import pandas as pd
import numpy as np
from numpy.core._multiarray_umath import ndarray
from sklearn import preprocessing
from pyarrow.lib import null
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.FinVizEngine import FinVizEngine
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine
from Common.StockMarketIndex import AbstractStockMarketIndex
from Common.StockOptions.AbstractStockOption import AbstractStockOption
from Common.WebScrappers.Yahoo.YahooSummaryScrapper import YahooSummaryScrapper


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
    HistoricalSimpleReturns: pd.DataFrame
    HistoricalLogReturns: pd.DataFrame
    HistoricalDaily: pd.DataFrame
    HistoricalDailyCum: pd.core.series.Series
    HistoricalMonthly: pd.DataFrame
    HistoricalMonthlyCum: pd.core.series.Series
    HistoricalStandardized: ndarray
    HistoricalScaled: ndarray
    HistoricalL1Normalized: ndarray
    HistoricalBinary: ndarray
    HistoricalMarketIndex: AbstractStockMarketIndex
    Ticker: str
    TimeSpan: TimeSpan
    Source: str
    SourceColumn: str
    YeUrl: str = 'NA'
    YeLogoUrl: str = 'NA'
    YeAddress: str = 'NA'
    YeCity: str = 'NA'
    YePostalCode: str = 'NA'
    YeState: str = 'NA'
    YeCountry: str = 'NA'
    YeBeta: float = -1.1
    YeMarket: str = 'NA'
    YeCurrency: str = 'NA'
    YeExchange: str = 'NA'
    YeHigh52: float = -1.1
    YeLow52: float = -1.1
    YeAverage50: float = -1.1
    YeAverage200: float = -1.1
    YeMarketCap: float = -1.1
    YePayoutRatio: float = -1.1
    YePeForward: float = -1.1
    YePeTrailing: float = -1.1
    YePegRatio: float = -1.1
    YeShortRatio: float = -1.1
    YeBookValue: float = -1.1
    YePriceToBook: float = -1.1
    YssBeta: str
    YssEarningsDate: str
    YssLink: str
    YssMarketCap: str
    YssPeRatio: str
    __fin_viz_engine: FinVizEngine
    __y_finance_engine: YahooFinanceEngine
    __yahooSummaryScrapper: YahooSummaryScrapper

    def __init__(self, a_ticker: str = 'CNI'):
        self.Source = 'yahoo'
        self.SourceColumn = 'Adj Close'
        self.Ticker = a_ticker
        self.TimeSpan = TimeSpan()
        self.__GetData()
        self.__GetDataSimpleReturns()
        self.__GetDataLogReturns()
        self.__GetDataDaily()
        self.__GetDataDailyCum()
        self.__GetDataMonthly()
        self.__GetDataMonthlyCum()
        self.__GetDataPreProcMeanRemove()
        self.__GetDataPreProcScale()
        self.__GetDataPreProcNormL1()
        self.__GetDataPreProcBinary()
        self.__GetFv()
        self.__GetYe()
        self.__GetYss()

    def __GetOutliers(self, a_df: pd.DataFrame, n_sigmas: int = 3):
        a_df['IsOutlier'] = pd.Series(dtype=int)
        a_df['Outliers'] = pd.Series(dtype=float)
        for ind in a_df.index:
            x = a_df[self.SourceColumn][ind]
            mu = a_df['mean'][ind]
            sigma = a_df['std'][ind]
            a_df['IsOutlier'][ind] = 1 if (x > mu + n_sigmas * sigma) | (x < mu - n_sigmas * sigma) else 0
            if a_df['IsOutlier'][ind] == 1:
                a_df['Outliers'][ind] = x
        return a_df

    def __GetData(self):
        self.HistoricalData = PandaEngine(self.Source, self.TimeSpan, self.Ticker).DataFrame
        self.HistoricalData.fillna(method='ffill', inplace=True)
        self.HistoricalData.fillna(method='bfill', inplace=True)
        # self.HistoricalData.columns = self.Ticker + self.HistoricalData.columns

    def __GetDataSimpleReturns(self):
        self.HistoricalSimpleReturns = self.HistoricalData[self.SourceColumn].pct_change().to_frame()
        df_rolling = self.HistoricalSimpleReturns[self.SourceColumn].rolling(window=21).agg(['mean', 'std'])
        self.HistoricalSimpleReturns = self.HistoricalSimpleReturns.join(df_rolling)
        self.HistoricalSimpleReturns = self.__GetOutliers(self.HistoricalSimpleReturns)

    def __GetDataLogReturns(self):
        a_var = np.log(self.HistoricalData[self.SourceColumn] / self.HistoricalData[self.SourceColumn].shift(1))
        self.HistoricalLogReturns = a_var.to_frame()
        self.HistoricalLogReturns['MovingStd252'] = self.HistoricalLogReturns[self.SourceColumn].rolling(
            window=252).std().to_frame()
        self.HistoricalLogReturns['MovingStd21'] = self.HistoricalLogReturns[self.SourceColumn].rolling(
            window=21).std().to_frame()

    def __GetDataDaily(self):
        self.HistoricalDaily = self.HistoricalData[self.SourceColumn].pct_change().to_frame()

    def __GetDataDailyCum(self):
        self.HistoricalDailyCum = (self.HistoricalDaily + 1).cumprod()

    def __GetDataMonthly(self):
        self.HistoricalMonthly = self.HistoricalData[self.SourceColumn].resample('M').ffill().pct_change().to_frame()

    def __GetDataMonthlyCum(self):
        self.HistoricalMonthlyCum = (self.HistoricalMonthly + 1).cumprod()

    def __GetDataPreProcMeanRemove(self):
        self.HistoricalStandardized = preprocessing.scale(self.HistoricalData)

    def __GetDataPreProcScale(self):
        self.HistoricalScaled = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(self.HistoricalData)

    def __GetDataPreProcNormL1(self):
        self.HistoricalL1Normalized = preprocessing.normalize(self.HistoricalData, norm='l1')

    def __GetDataPreProcBinary(self):
        self.HistoricalBinary = preprocessing.Binarizer(threshold=1.4).transform(self.HistoricalData)

    def __GetFv(self):
        self.__fin_viz_engine = FinVizEngine(self.Ticker)
        self.FvCompanyName = self.__fin_viz_engine.StockName
        self.FvCompanySector = self.__fin_viz_engine.StockSector
        self.FvCompanyIndustry = self.__fin_viz_engine.StockIndustry
        self.FvCompanyCountry = self.__fin_viz_engine.StockCountry
        self.FvPeRatio = self.__fin_viz_engine.PeRatio
        self.FvMarketCap = self.__fin_viz_engine.MarketCap
        self.FvEPS = self.__fin_viz_engine.EpsTtm
        self.FvBeta = self.__fin_viz_engine.Beta
        self.FvEarnings = self.__fin_viz_engine.EarningDate
        self.FvLow52 = self.__fin_viz_engine.Low52
        self.FvHigh52 = self.__fin_viz_engine.High52
        self.FvRange52 = self.__fin_viz_engine.Range52
        self.FvRsi14 = self.__fin_viz_engine.Rsi14
        self.FvVolatility = self.__fin_viz_engine.Volatility
        self.FvPayout = self.__fin_viz_engine.PayoutPcnt
        self.FvVolume = self.__fin_viz_engine.Volume
        self.FvChangePercent = self.__fin_viz_engine.ChangePcnt
        self.FvPrice = self.__fin_viz_engine.Price
        self.FvDividend = self.__fin_viz_engine.Dividend
        self.FvDividendPercent = self.__fin_viz_engine.DividendPcnt

    def __GetYe(self):
        self.__y_finance_engine = YahooFinanceEngine(self.Ticker)
        self.YeUrl = self.__y_finance_engine.Url
        self.YeLogoUrl = self.__y_finance_engine.LogoUrl
        self.YeAddress = self.__y_finance_engine.Address
        self.YeCity = self.__y_finance_engine.City
        self.YePostalCode = self.__y_finance_engine.PostalCode
        self.YeState = self.__y_finance_engine.State
        self.YeCountry = self.__y_finance_engine.Country
        self.YeBeta = self.__y_finance_engine.Beta
        self.YeMarket = self.__y_finance_engine.Market
        self.YeCurrency = self.__y_finance_engine.Currency
        self.YeQuoteType = self.__y_finance_engine.QuoteType
        self.YeExchange = self.__y_finance_engine.Exchange
        self.YeCountry = self.__y_finance_engine.Country
        self.YeBeta = self.__y_finance_engine.Beta
        self.YeMarket = self.__y_finance_engine.Market
        self.YeCurrency = self.__y_finance_engine.Currency
        self.YeQuoteType = self.__y_finance_engine.QuoteType
        self.YeExchange = self.__y_finance_engine.Exchange
        self.YeHigh52 = self.__y_finance_engine.High52
        self.YeLow52 = self.__y_finance_engine.Low52
        self.YeAverage50 = self.__y_finance_engine.Average50
        self.YeAverage200 = self.__y_finance_engine.Average200
        self.YeMarketCap = self.__y_finance_engine.MarketCap
        self.YePayoutRatio = self.__y_finance_engine.PayoutRatio
        self.YePeForward = self.__y_finance_engine.PEforward
        self.YePeTrailing = self.__y_finance_engine.PEtrailing
        self.YePegRatio = self.__y_finance_engine.PegRatio
        self.YeShortRatio = self.__y_finance_engine.ShortRatio
        self.YeBookValue = self.__y_finance_engine.BookValue
        self.YePriceToBook = self.__y_finance_engine.PriceToBook
        self.YeExDividendDate = self.__y_finance_engine.ExDividendDate

    def __GetYss(self):
        self.__yahooSummaryScrapper = YahooSummaryScrapper(self.Ticker)
        self.__yahooSummaryScrapper.ParseBody()
        self.YssPeRatio = self.__yahooSummaryScrapper.PEratio
        self.YssMarketCap = self.__yahooSummaryScrapper.MarketCap
        self.YssEPS = self.__yahooSummaryScrapper.EPS
        self.YssBeta = self.__yahooSummaryScrapper.Beta
        self.YssEarningsDate = self.__yahooSummaryScrapper.EarningsDate
        self.YssLink = self.__yahooSummaryScrapper.Link
