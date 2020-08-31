from typing import List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.core._multiarray_umath import ndarray
from pyarrow.lib import null

from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.FinVizEngine import FinVizEngine
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine
from Common.StockMarketIndex import AbstractStockMarketIndex
from Common.StockOptions.AbstractStockOption import AbstractStockOption
from Common.WebScrappers.Yahoo.YahooSummaryScrapper import YahooSummaryScrapper
#For Prediction
from sklearn import preprocessing
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR


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
    ForecastArray: ndarray
    HistoricalColumn: str = 'Prediction'
    HistoricalBinary: ndarray
    HistoricalData: pd.DataFrame
    HistoricalDaily: pd.DataFrame
    HistoricalDailyCum: pd.core.series.Series
    HistoricalL1Normalized: ndarray
    HistoricalLinReg: LinearRegression
    HistoricalLinRegScore: float = -1.1
    HistoricalLinRegPrediction: ndarray
    HistoricalLogReturns: pd.DataFrame
    HistoricalMarketIndex: AbstractStockMarketIndex
    HistoricalMonthly: pd.DataFrame
    HistoricalMonthlyCum: pd.core.series.Series
    HistoricalPrediction: pd.DataFrame
    HistoricalScaled: ndarray
    HistoricalSimpleReturns: pd.DataFrame
    HistoricalStandardized: ndarray
    HistoricalSVRLinear: SVR
    HistoricalSVRLinearScore: float = -1.1
    HistoricalSVRLinearPrediction: ndarray
    HistoricalSVRPoly: SVR
    HistoricalSVRPolyScore: float = -1.1
    HistoricalSVRPolyPrediction: ndarray
    HistoricalSVRRbf: SVR
    HistoricalSVRRbfScore: float = -1.1
    HistoricalSVRRbfPrediction: ndarray
    HistoricalTreeReg: DecisionTreeRegressor
    HistoricalTreeRegScore: float = -1.1
    HistoricalTreeRegPrediction: ndarray
    RMSE: float = -1.1
    Source: str = 'yahoo'
    SourceColumn: str = 'Adj Close'
    Ticker: str = 'TD'
    TimeSpan: TimeSpan
    Xarray: ndarray
    Yarray: ndarray
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
        self.__GetDataPrediction()
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

    def __GetDataPrediction(self):
        #into the future
        self.ForecastSpan = 30
        self.HistoricalColumn = 'Prediction' + str(self.ForecastSpan)
        self.HistoricalPrediction = self.HistoricalData[self.SourceColumn].to_frame()
        self.HistoricalPrediction[self.HistoricalColumn] = self.HistoricalData[[self.SourceColumn]].shift(-self.ForecastSpan)
        self.HistoricalTreeReg = DecisionTreeRegressor()
        self.HistoricalLinReg = LinearRegression()
        self.HistoricalSVRLinear = SVR(kernel='linear', C=1e3)
        self.HistoricalSVRPoly = SVR(kernel='poly', C=1e3, degree=2)
        self.HistoricalSVRRbf = SVR(kernel='rbf', C=1e3, gamma=0.2)#percent 80/20 = 0.2
        self.ForecastArray = np.array(self.HistoricalPrediction.drop([self.HistoricalColumn], 1))[-self.ForecastSpan:]
        #independent X
        #convert to ndarray & remove last NaN rows
        self.Xarray = np.array(self.HistoricalPrediction.drop([self.HistoricalColumn], 1))
        self.Xarray = self.Xarray[:-self.ForecastSpan]
        #dependent Y
        #convert to ndarray & remove last NaN rows
        self.Yarray = np.array(self.HistoricalPrediction[self.HistoricalColumn])
        self.Yarray = self.Yarray[:-self.ForecastSpan]
        #split into 80% train / 20% test => 0.2
        X_train, X_test, Y_train, Y_test = train_test_split(self.Xarray, self.Yarray, test_size=0.2)
        #TREE
        self.HistoricalTreeReg.fit(self.Xarray, self.Yarray)
        self.HistoricalTreeRegScore = self.HistoricalTreeReg.score(X_test, Y_test)
        print('TREE confidence', self.HistoricalTreeRegScore)
        #LIN
        self.HistoricalLinReg.fit(X_train, Y_train)
        self.HistoricalLinRegScore = self.HistoricalLinReg.score(X_test, Y_test)
        print('CLF confidence', self.HistoricalLinRegScore)
        #SVR_LIN
        self.HistoricalSVRLinear.fit(X_test, Y_test)
        self.HistoricalSVRLinearScore = self.HistoricalSVRLinear.score(X_test, Y_test)
        print('SVR_LIN confidence', self.HistoricalSVRLinearScore)
        #SVR_POLY
        self.HistoricalSVRPoly.fit(X_test, Y_test)
        self.HistoricalSVRPolyScore = self.HistoricalSVRPoly.score(X_test, Y_test)
        print('SVR_POLY confidence', self.HistoricalSVRPolyScore)
        #SVR_RBF
        self.HistoricalSVRRbf.fit(X_test, Y_test)
        self.HistoricalSVRRbfScore = self.HistoricalSVRRbf.score(X_test, Y_test)
        print('SVR_RBF confidence', self.HistoricalSVRRbfScore)
        # x_forecast equal to last 30 days
        #TREE predict n days
        self.HistoricalTreeRegPrediction = self.HistoricalTreeReg.predict(self.ForecastArray)
        print('tree_prediction', self.HistoricalTreeRegPrediction)
        #LIN predict n days
        self.HistoricalLinRegPrediction = self.HistoricalLinReg.predict(self.ForecastArray)
        print('clf_prediction', self.HistoricalLinRegPrediction)
        #SVR_LIN predict n days
        self.HistoricalSVRLinearPrediction = self.HistoricalSVRLinear.predict(self.ForecastArray)
        print('svr_rbf_prediction', self.HistoricalSVRLinearPrediction)
        #SVR_POLY predict n days
        self.HistoricalSVRPolyPrediction = self.HistoricalSVRPoly.predict(self.ForecastArray)
        print('svr_poly_prediction', self.HistoricalSVRPolyPrediction)
        #SVR_RBF predict n days
        self.HistoricalSVRRbfPrediction = self.HistoricalSVRRbf.predict(self.ForecastArray)
        print('svr_rbf_prediction', self.HistoricalSVRRbfPrediction)
        #plot(days, self.HistoricalSVRRbf.predict(days), color='green', label='RBFmodel')
        #print('SVR RBF preiced', self.HistoricalSVRRbf.predict(self.ForecastArray))
        #exit(-111)
        valid = self.HistoricalData[self.Xarray.shape[0]:]
        valid['Predictions'] = self.HistoricalTreeRegPrediction
        plt.figure(figsize=(8, 6))
        plt.title('Model')
        plt.xlabel('Days')
        plt.ylabel(self.SourceColumn)
        plt.scatter(self.HistoricalData.index, self.HistoricalData[self.SourceColumn], color='black')
        plt.plot(self.HistoricalData[self.SourceColumn])
        plt.plot(valid[[self.SourceColumn, 'Predictions']])
        plt.legend([self.SourceColumn, self.SourceColumn + 'Training', self.SourceColumn + 'Predicted'])
        plt.show()
        exit(220)

    def __GetDataSimpleReturns(self):
        self.HistoricalSimpleReturns = self.HistoricalData[self.SourceColumn].pct_change().to_frame()
        df_rolling = self.HistoricalSimpleReturns[self.SourceColumn].rolling(window=21).agg(['mean', 'std'])
        self.HistoricalSimpleReturns = self.HistoricalSimpleReturns.join(df_rolling)
        self.HistoricalSimpleReturns = self.__GetOutliers(self.HistoricalSimpleReturns)
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

    def simulate_gbm(self, s_0, mu, sigma, n_sims, T, N):
        dt = T/N
        dW = np.random.normal(scale = np.sqrt(dt), size=(n_sims, N))
        W = np.cumsum(dW, axis=1)
        time_step = np.linspace(dt, T, N)
        time_steps = np.broadcast_to(time_step, (n_sims, N))
        S_t = s_0 * np.exp((mu - 0.5 * sigma ** 2) * time_steps + sigma * W)
        S_t = np.insert(S_t, 0, s_0, axis=1)
        return S_t

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
