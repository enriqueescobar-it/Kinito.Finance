from typing import List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyarrow.lib import null
import math
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Predictors.Linear.LinearPredictor import LinearPredictor
from Common.Predictors.Svr.LinearSvrPredictor import LinearSvrPredictor
from Common.Predictors.Svr.PolySvrPredictor import PolySvrPredictor
from Common.Predictors.Svr.RbfSvrPredictor import RbfSvrPredictor
from Common.Predictors.Tree.DecisionTreePredictor import DecisionTreePredictor
from Common.Readers.Engine.FinVizEngine import FinVizEngine
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine
from Common.StockMarketIndex import AbstractStockMarketIndex
from Common.StockOptions.AbstractStockOption import AbstractStockOption
from Common.WebScrappers.Yahoo.YahooSummaryScrapper import YahooSummaryScrapper
#For Prediction
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from keras.models import Sequential
from keras.layers import Dense, LSTM


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
    ForecastSpan: int = 30
    HistoricalBinary: np.ndarray
    HistoricalData: pd.DataFrame
    HistoricalDaily: pd.DataFrame
    HistoricalDailyCum: pd.core.series.Series
    HistoricalNormalized: pd.DataFrame
    HistoricalL1Normalized: np.ndarray
    HistoricalLinRegScore: float = -1.1
    HistoricalLinRegPrediction: np.ndarray
    HistoricalLogReturns: pd.DataFrame
    HistoricalMarketIndex: AbstractStockMarketIndex
    HistoricalMonthly: pd.DataFrame
    HistoricalMonthlyCum: pd.core.series.Series
    HistoricalScaled: np.ndarray
    HistoricalSimpleReturns: pd.DataFrame
    HistoricalSparse: np.ndarray
    HistoricalSVRLinearScore: float = -1.1
    HistoricalSVRLinearPrediction: np.ndarray
    HistoricalSVRPolyScore: float = -1.1
    HistoricalSVRPolyPrediction: np.ndarray
    HistoricalSVRRbfScore: float = -1.1
    HistoricalSVRRbfPrediction: np.ndarray
    HistoricalTreeRegScore: float = -1.1
    HistoricalTreeRegPrediction: np.ndarray
    RMSE: float = -1.1
    Source: str = 'yahoo'
    SourceColumn: str = 'Adj Close'
    Ticker: str = 'TD'
    TimeSpan: TimeSpan
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
    _fin_viz_engine: FinVizEngine
    _y_finance_engine: YahooFinanceEngine
    _yahooSummaryScrapper: YahooSummaryScrapper

    def __init__(self, a_ticker: str = 'CNI'):
        self.Source = 'yahoo'
        self.SourceColumn = 'Adj Close'
        self.Ticker = a_ticker
        self.TimeSpan = TimeSpan()
        self.HistoricalData = self._setData()
        self.HistoricalNormalized = self._setNormalizer(self.HistoricalData)
        self.HistoricalL1Normalized = self._setNormalizerL1(self.HistoricalData)
        self.HistoricalBinary = self._setBinarizer(self.HistoricalData)
        self._setSimpleReturns()
        self._setLogReturns()
        self._setDataDaily()
        self._setDataMonthly()
        self._setSparser()
        self._setScaler()
        self._setDataPrediction()
        self._setFinViz()
        self._setYahooFinance()
        self._setYahooSummary()

    def _getOutliers(self, a_df: pd.DataFrame, n_sigmas: int = 3):
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

    def _setData(self) -> pd.DataFrame:
        a_df: pd.DataFrame = PandaEngine(self.Source, self.TimeSpan, self.Ticker).DataFrame
        a_df.fillna(method='ffill', inplace=True)
        a_df.fillna(method='bfill', inplace=True)
        # self.HistoricalData.columns = self.Ticker + self.HistoricalData.columns
        return a_df

    def _setNormalizer(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return a_df / a_df.iloc[0]

    def _setNormalizerL1(self, a_df: pd.DataFrame = pd.DataFrame()) -> np.ndarray:
        return preprocessing.normalize(a_df, norm='l1')

    def _setBinarizer(self, a_df: pd.DataFrame = pd.DataFrame()) -> np.ndarray:
        return preprocessing.Binarizer(threshold=1.4).transform(a_df)

    def _setSparser(self):
        self.HistoricalSparse = preprocessing.scale(self.HistoricalData)

    def _setScaler(self):
        self.HistoricalScaled = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(self.HistoricalData)

    def _setSimpleReturns(self):
        self.HistoricalSimpleReturns = self.HistoricalData[self.SourceColumn].pct_change().to_frame()
        df_rolling = self.HistoricalSimpleReturns[self.SourceColumn].rolling(window=21).agg(['mean', 'std'])
        self.HistoricalSimpleReturns = self.HistoricalSimpleReturns.join(df_rolling)
        self.HistoricalSimpleReturns = self._getOutliers(self.HistoricalSimpleReturns)
        df = self.HistoricalSimpleReturns[self.SourceColumn].dropna()
        dfLength = len(df)
        dfLength80 = int(round(dfLength*0.8))
        dfLength20 = dfLength - dfLength80
        train = df[:dfLength80].to_frame()
        test = df[dfLength80:].to_frame()
        ##
        print(train.shape)
        print(dfLength80)
        print(test.shape)
        print(dfLength20)
        preds = []
        for i in range(0, test.shape[0]):
            a = train[self.SourceColumn][len(train)-dfLength20+i:].sum() + sum(preds)
            b = a/dfLength20
            preds.append(b)
        self.RMSE = np.sqrt(np.mean(np.power((np.array(test[self.SourceColumn])-preds), 2)))
        print('\n RMSE value on validation set:', self.RMSE)
        lin_svr = SVR(kernel='linear', C=1000.0)
        #lin_svr.fit(self.HistoricalSimpleReturns.index, self.HistoricalSimpleReturns[self.SourceColumn])
        ##
        #T = len(test)
        #N = len(test)
        #S_0 = df[train.index[-1]]#.date()]
        #N_SIM = 100
        #mu = train.mean()
        #sigma = train.std()
        #gbm_simulations: ndarray = self.simulate_gbm(S_0, mu, sigma, N_SIM, T, N)
        #gbm_simulationsT: ndarray = np.transpose(gbm_simulations)
        #print('gbm_simulationsT', gbm_simulationsT.shape)
        # prepare objects for plotting
        #LAST_TRAIN_DATE = train.index[-1].date()
        #FIRST_TEST_DATE = test.index[0].date()
        #LAST_TEST_DATE = test.index[-1].date()
        #PLOT_TITLE = f'{self.Ticker} Simulation ({FIRST_TEST_DATE}:{LAST_TEST_DATE})'
        #selected_indices = self.HistoricalData[self.SourceColumn][LAST_TRAIN_DATE:LAST_TEST_DATE].index
        #a_index = [date.date() for date in selected_indices]
        #print('a_index', len(a_index))
        #gbm_simulationsDf = pd.DataFrame(data=gbm_simulationsT, index=a_index)
        #print('gbm_simulationsDf', gbm_simulationsDf.shape)
        # plotting
        #ax = gbm_simulationsDf.plot(alpha=0.2, legend=False)
        #line_1, = ax.plot(a_index, gbm_simulationsDf.mean(axis=1), color='red')
        #line_2, = ax.plot(a_index, self.HistoricalData[self.SourceColumn][LAST_TRAIN_DATE:LAST_TEST_DATE], color='blue')
        #ax.set_title(PLOT_TITLE, fontsize=16)
        #ax.legend((line_1, line_2), ('mean', 'actual'))
        #plt.show()

    def _setLogReturns(self):
        a_var = np.log(self.HistoricalData[self.SourceColumn] / self.HistoricalData[self.SourceColumn].shift(1))
        self.HistoricalLogReturns = a_var.to_frame()
        self.HistoricalLogReturns['MovingStd252'] =\
            self.HistoricalLogReturns[self.SourceColumn].rolling(window=252).std().to_frame()
        self.HistoricalLogReturns['MovingStd21'] =\
            self.HistoricalLogReturns[self.SourceColumn].rolling(window=21).std().to_frame()

    def _setDataDaily(self):
        self.HistoricalDaily = self.HistoricalData[self.SourceColumn].pct_change().to_frame()
        self.HistoricalDailyCum = (self.HistoricalDaily + 1).cumprod()

    def _setDataMonthly(self):
        self.HistoricalMonthly = self.HistoricalData[self.SourceColumn].resample('M').ffill().pct_change().to_frame()
        self.HistoricalMonthlyCum = (self.HistoricalMonthly + 1).cumprod()

    def _setFinViz(self):
        self._fin_viz_engine = FinVizEngine(self.Ticker)
        self.FvCompanyName = self._fin_viz_engine.StockName
        self.FvCompanySector = self._fin_viz_engine.StockSector
        self.FvCompanyIndustry = self._fin_viz_engine.StockIndustry
        self.FvCompanyCountry = self._fin_viz_engine.StockCountry
        self.FvPeRatio = self._fin_viz_engine.PeRatio
        self.FvMarketCap = self._fin_viz_engine.MarketCap
        self.FvEPS = self._fin_viz_engine.EpsTtm
        self.FvBeta = self._fin_viz_engine.Beta
        self.FvEarnings = self._fin_viz_engine.EarningDate
        self.FvLow52 = self._fin_viz_engine.Low52
        self.FvHigh52 = self._fin_viz_engine.High52
        self.FvRange52 = self._fin_viz_engine.Range52
        self.FvRsi14 = self._fin_viz_engine.Rsi14
        self.FvVolatility = self._fin_viz_engine.Volatility
        self.FvPayout = self._fin_viz_engine.PayoutPcnt
        self.FvVolume = self._fin_viz_engine.Volume
        self.FvChangePercent = self._fin_viz_engine.ChangePcnt
        self.FvPrice = self._fin_viz_engine.Price
        self.FvDividend = self._fin_viz_engine.Dividend
        self.FvDividendPercent = self._fin_viz_engine.DividendPcnt

    def _setYahooFinance(self):
        self._y_finance_engine = YahooFinanceEngine(self.Ticker)
        self.YeUrl = self._y_finance_engine.Url
        self.YeLogoUrl = self._y_finance_engine.LogoUrl
        self.YeAddress = self._y_finance_engine.Address
        self.YeCity = self._y_finance_engine.City
        self.YePostalCode = self._y_finance_engine.PostalCode
        self.YeState = self._y_finance_engine.State
        self.YeCountry = self._y_finance_engine.Country
        self.YeBeta = self._y_finance_engine.Beta
        self.YeMarket = self._y_finance_engine.Market
        self.YeCurrency = self._y_finance_engine.Currency
        self.YeQuoteType = self._y_finance_engine.QuoteType
        self.YeExchange = self._y_finance_engine.Exchange
        self.YeCountry = self._y_finance_engine.Country
        self.YeBeta = self._y_finance_engine.Beta
        self.YeMarket = self._y_finance_engine.Market
        self.YeCurrency = self._y_finance_engine.Currency
        self.YeQuoteType = self._y_finance_engine.QuoteType
        self.YeExchange = self._y_finance_engine.Exchange
        self.YeHigh52 = self._y_finance_engine.High52
        self.YeLow52 = self._y_finance_engine.Low52
        self.YeAverage50 = self._y_finance_engine.Average50
        self.YeAverage200 = self._y_finance_engine.Average200
        self.YeMarketCap = self._y_finance_engine.MarketCap
        self.YePayoutRatio = self._y_finance_engine.PayoutRatio
        self.YePeForward = self._y_finance_engine.PEforward
        self.YePeTrailing = self._y_finance_engine.PEtrailing
        self.YePegRatio = self._y_finance_engine.PegRatio
        self.YeShortRatio = self._y_finance_engine.ShortRatio
        self.YeBookValue = self._y_finance_engine.BookValue
        self.YePriceToBook = self._y_finance_engine.PriceToBook
        self.YeExDividendDate = self._y_finance_engine.ExDividendDate

    def _setYahooSummary(self):
        self._yahooSummaryScrapper = YahooSummaryScrapper(self.Ticker)
        self._yahooSummaryScrapper.ParseBody()
        self.YssPeRatio = self._yahooSummaryScrapper.PEratio
        self.YssMarketCap = self._yahooSummaryScrapper.MarketCap
        self.YssEPS = self._yahooSummaryScrapper.EPS
        self.YssBeta = self._yahooSummaryScrapper.Beta
        self.YssEarningsDate = self._yahooSummaryScrapper.EarningsDate
        self.YssLink = self._yahooSummaryScrapper.Link

    def simulate_gbm(self, s_0, mu, sigma, n_sims, T, N):
        dt = T/N
        dW = np.random.normal(scale = np.sqrt(dt), size=(n_sims, N))
        W = np.cumsum(dW, axis=1)
        time_step = np.linspace(dt, T, N)
        time_steps = np.broadcast_to(time_step, (n_sims, N))
        S_t = s_0 * np.exp((mu - 0.5 * sigma ** 2) * time_steps + sigma * W)
        S_t = np.insert(S_t, 0, s_0, axis=1)
        return S_t

    def _setDataPrediction(self):
        #into the future
        self.ForecastSpan = 30
        #TREE
        '''decisionTreePredictor: DecisionTreePredictor =\
            DecisionTreePredictor(self.ForecastSpan, self.SourceColumn, self.HistoricalData)
        self.HistoricalTreeRegScore = decisionTreePredictor.GetScore()
        print('TREE confidence', self.HistoricalTreeRegScore)
        #TREE predict n days
        self.HistoricalTreeRegPrediction = decisionTreePredictor.GetPrediction()
        print(self.HistoricalTreeRegPrediction.shape[0])
        decisionTreePredictor.Plot().show()
        #LIN
        linearPredictor: LinearPredictor =\
            LinearPredictor(self.ForecastSpan, self.SourceColumn, self.HistoricalData)
        self.HistoricalLinRegScore = linearPredictor.GetScore()
        print('LINEAR confidence', self.HistoricalLinRegScore)
        #LIN predict n days
        self.HistoricalLinRegPrediction = linearPredictor.GetPrediction()
        print(self.HistoricalLinRegPrediction.shape[0])
        linearPredictor.Plot().show()
        #SVR_LIN
        linearSvrPredictor: LinearSvrPredictor =\
            LinearSvrPredictor(self.ForecastSpan, self.SourceColumn, self.HistoricalData)
        self.HistoricalSVRLinearScore = linearSvrPredictor.GetScore()
        print('SVR_LIN confidence', self.HistoricalSVRLinearScore)
        #SVR_LIN predict n days
        self.HistoricalSVRLinearPrediction = linearSvrPredictor.GetPrediction()
        print(self.HistoricalSVRLinearPrediction.shape[0])
        linearSvrPredictor.Plot().show()
        #SVR_POLY
        polySvrPredictor: PolySvrPredictor =\
            PolySvrPredictor(self.ForecastSpan, self.SourceColumn, self.HistoricalData)
        self.HistoricalSVRPolyScore = polySvrPredictor.GetScore()
        print('SVR_POLY confidence', self.HistoricalSVRPolyScore)
        #SVR_POLY predict n days
        self.HistoricalSVRPolyPrediction = polySvrPredictor.GetPrediction()
        print(self.HistoricalSVRPolyPrediction.shape[0])
        polySvrPredictor.Plot().show()
        #SVR_RBF
        rbfSvrPredictor: RbfSvrPredictor =\
            RbfSvrPredictor(self.ForecastSpan, self.SourceColumn, self.HistoricalData)
        self.HistoricalSVRRbfScore = rbfSvrPredictor.GetScore()
        print('SVR_RBF confidence', self.HistoricalSVRRbfScore)
        #SVR_RBF predict n days
        self.HistoricalSVRRbfPrediction = rbfSvrPredictor.GetPrediction()
        print(self.HistoricalSVRRbfPrediction.shape[0])
        rbfSvrPredictor.Plot().show()
        #
        training_len: int = math.ceil(self.HistoricalScaled.shape[0] * 0.8)
        print(training_len)
        scaled_data = self.HistoricalScaled
        train_data = scaled_data[0:training_len, :]
        X_train = []
        Y_train = []
        for i in range(60, len(train_data)):
            X_train.append(train_data[i-60:i, 0])
            Y_train.append(train_data[i, 0])
        X_train, Y_train = np.array(X_train), np.array(Y_train)
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
        #LSTM model
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
        model.add(LSTM(50, return_sequences=False))
        model.add(Dense(25))
        model.add(Dense(1))
        exit(-111)'''
