import statistics

import numpy as np
import pandas as pd
import scipy.stats as scs
from numpy import ndarray
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVR

from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine
from Common.StockOptions.AbstractStockOption import AbstractStockOption
from Common.WebScrappers.Yahoo.YahooSummaryScrapper import YahooSummaryScrapper
from prettytable import PrettyTable


class YahooStockOption(AbstractStockOption):
    ForecastSpan: int = 30
    DataSimpleReturns: pd.DataFrame
    DataLogReturns: pd.DataFrame
    SimpleAnnually: pd.DataFrame
    SimpleAnnuallyCum: pd.Series
    SimpleDaily: pd.DataFrame
    SimplyDailyCum: pd.Series
    SimpleMonthly: pd.DataFrame
    SimpleMonthlyCum: pd.Series
    SimpleQuarterly: pd.DataFrame
    SimpleQuarterlyCum: pd.Series
    SimpleWeekly: pd.DataFrame
    SimpleWeeklyCum: pd.Series
    SimpleDailyReturnAvg: float = -1.1
    SimpleWeeklyReturnAvg: float = -1.1
    SimpleMonthlyReturnAvg: float = -1.1
    SimpleQuarterlyReturnAvg: float = -1.1
    SimpleAnnuallyReturnAvg: float = -1.1
    RMSE: float = -1.1
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
    YssBeta: str = ''
    YssEarningsDate: str = ''
    YssLink: str = ''
    YssMarketCap: str = ''
    YssPeRatio: str = ''

    def __init__(self, a_ticker: str = 'CNI', a_src: str = 'yahoo', a_col: str = 'Adj Close'):
        self._source = a_src
        self._column = a_col
        self._ticker = a_ticker
        self._historical = self._setData()
        self._t_s = self._updateTimeSpan(self._t_s, self._historical)
        self._data = self._historical[self.Column].to_frame()
        self._data_range = self._getDataRange(1000, self._data[self.Column])
        self._mu = round(self._historical[self.Column].mean(), 2)
        self._sigma = round(self._historical[self.Column].std(), 2)
        self._median = round(self._historical[self.Column].median(), 2)
        self._norm_pdf = self._getProbabilityDensityFunction(self.DataRange, self._mu, self._sigma)
        self._data['Norm'] = self._setNormalizer(self._historical)
        self._data['NormL1'] = self._setNormalizerL1(self._historical)
        self._data['Binary'] = self._setBinarizer(self._historical)
        self._data['Sparse'] = self._setSparser(self._historical)
        self._data['Scaled'] = self._setScaler(self._historical)
        self.DataSimpleReturns = self._setSimpleReturns('', self._historical)
        self.DataSimpleReturns = self._setSimpleReturnsPlus(self.DataSimpleReturns)
        self._data['IsOutlier'] = self.DataSimpleReturns.IsOutlier.astype(bool)
        self.DataLogReturns = self._setLogReturns(self._historical)
        self.DataLogReturns = self._setLogReturnsPlus(self.DataLogReturns)
        self.SimpleDaily = self._setSimpleReturns('', self._historical)
        self.SimplyDailyCum = self._setSimpleCumulative(self.SimpleDaily)
        self.SimpleDailyReturnAvg = self._setSimpleReturnAverage(self.SimplyDailyCum)
        self.SimpleWeekly = self._setSimpleReturns('W', self._historical)
        self.SimpleWeeklyCum = self._setSimpleCumulative(self.SimpleWeekly)
        self.SimpleWeeklyReturnAvg = self._setSimpleReturnAverage(self.SimpleWeeklyCum)
        self.SimpleMonthly = self._setSimpleReturns('M', self._historical)
        self.SimpleMonthlyCum = self._setSimpleCumulative(self.SimpleMonthly)
        self.SimpleMonthlyReturnAvg = self._setSimpleReturnAverage(self.SimpleMonthlyCum)
        self.SimpleQuarterly = self._setSimpleReturns('Q', self._historical)
        self.SimpleQuarterlyCum = self._setSimpleCumulative(self.SimpleQuarterly)
        self.SimpleQuarterlyReturnAvg = self._setSimpleReturnAverage(self.SimpleQuarterlyCum)
        self.SimpleAnnually = self._setSimpleReturns('A', self._historical)
        self.SimpleAnnuallyCum = self._setSimpleCumulative(self.SimpleAnnually)
        self.SimpleAnnuallyReturnAvg = self._setSimpleReturnAverage(self.SimpleAnnuallyCum)
        (self.IsDaily, self.IsWeekly, self.IsMonthly, self.IsQuarterly, self.IsAnnually) =\
            self._setIsTimely(self.SimpleDailyReturnAvg, self.SimpleWeeklyReturnAvg,
                          self.SimpleMonthlyReturnAvg, self.SimpleQuarterlyReturnAvg,
                          self.SimpleAnnuallyReturnAvg)
        print('D', self.IsDaily)
        print('W', self.IsWeekly)
        print('M', self.IsMonthly)
        print('Q', self.IsQuarterly)
        print('A', self.IsAnnually)
        self._setYahooFinance(a_ticker)
        self._setYahooSummary(a_ticker)

    def _getOutliers(self, a_df: pd.DataFrame, n_sigmas: int = 3):
        a_df['IsOutlier'] = pd.Series(dtype=int)
        a_df['Outliers'] = pd.Series(dtype=float)
        for ind in a_df.index:
            x = a_df[self.Column][ind]
            mu = a_df['mean'][ind]
            sigma = a_df['std'][ind]
            a_df['IsOutlier'][ind] = 1 if (x > mu + n_sigmas * sigma) | (x < mu - n_sigmas * sigma) else 0
            if a_df['IsOutlier'][ind] == 1:
                a_df['Outliers'][ind] = x
        return a_df

    def _setData(self) -> pd.DataFrame:
        a_df: pd.DataFrame = PandaEngine(self.Source, self._t_s, self._ticker).DataFrame
        a_df.fillna(method='ffill', inplace=True)
        a_df.fillna(method='bfill', inplace=True)
        # self.HistoricalData.columns = self.Ticker + self.HistoricalData.columns
        self._high52 = self.__setHigh52(a_df)
        self._low52 = self.__setLow52(a_df)
        self._range52 = [self._low52, self._high52]
        self._price = self.__setPrice(a_df)
        return a_df

    def __setHigh52(self, a_df) -> float:
        i = a_df['High'].head(252).max()
        return round(i, 6)

    def __setLow52(self, a_df) -> float:
        i = a_df['Low'].head(252).min()
        return round(i, 6)

    def __setPrice(self, a_df) -> float:
        i = a_df['Adj Close'].iloc[-1]
        return round(i, 6)

    def _setNormalizer(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return (a_df / a_df.iloc[0])[self.Column]

    def _setNormalizerL1(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return\
            pd.DataFrame(preprocessing.normalize(a_df, norm='l1'), columns=a_df.columns, index=a_df.index)[self.Column]

    def _setBinarizer(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return\
            pd.DataFrame(preprocessing.Binarizer(threshold=1.4).transform(a_df), columns=a_df.columns, index=a_df.index)[self.Column]

    def _setSparser(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return pd.DataFrame(preprocessing.scale(a_df), columns=a_df.columns, index=a_df.index)[self.Column]

    def _setScaler(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        # scale to compare array from 0.0 to 100.0
        minMaxScaler: MinMaxScaler = preprocessing.MinMaxScaler(feature_range=(0.0, 100.0))
        # scale to compare data frame
        stockArrayScaled: np.ndarray = minMaxScaler.fit_transform(a_df)
        return pd.DataFrame(stockArrayScaled, columns=a_df.columns, index=a_df.index)[self.Column]

    def _setSimpleReturns(self, a_letter: str = '', a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        new_df: pd.DataFrame() = pd.DataFrame()
        if a_letter == 'W':
            new_df = a_df[self.Column].resample('W').ffill().pct_change().to_frame()
        elif a_letter == 'M':
            new_df = a_df[self.Column].resample('M').ffill().pct_change().to_frame()
        elif a_letter == 'Q':
            new_df = a_df[self.Column].resample('Q').ffill().pct_change().to_frame()
        elif a_letter == 'A':
            new_df = a_df[self.Column].resample('A').ffill().pct_change().to_frame()
        else:
            new_df = a_df[self.Column].pct_change().to_frame()
        new_df.iloc[0, :] = 0
        return new_df

    def _setSimpleReturnsPlus(self, simple_returns: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        df_rolling = simple_returns[self.Column].rolling(window=21).agg(['mean', 'std'])
        simple_returns = simple_returns.join(df_rolling)
        simple_returns = self._getOutliers(simple_returns)
        df = simple_returns[self.Column].dropna()
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
            a = train[self.Column][len(train)-dfLength20+i:].sum() + sum(preds)
            b = a/dfLength20
            preds.append(b)
        self.RMSE = np.sqrt(np.mean(np.power((np.array(test[self.Column])-preds), 2)))
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
        return simple_returns

    def _setLogReturns(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        a_var = np.log(a_df[self.Column] / a_df[self.Column].shift(1))
        new_df: pd.DataFrame = a_var.to_frame()
        new_df.iloc[0, :] = 0
        return new_df

    def _setLogReturnsPlus(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        a_df['MovingStd252'] = a_df[self.Column].rolling(window=252).std().to_frame()
        a_df['MovingStd21'] = a_df[self.Column].rolling(window=21).std().to_frame()
        return a_df

    def _setSimpleCumulative(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.Series:
        return (a_df + 1).cumprod()

    def _setYahooFinance(self, a_ticker: str = 'TD'):
        self._y_finance_engine = YahooFinanceEngine(a_ticker)
        t = PrettyTable()
        t.add_column(a_ticker, self._y_finance_engine.InfoList)
        print(t)
        self.YeUrl = self._y_finance_engine.Url
        self.YeLogoUrl = self._y_finance_engine.UrlLogo
        self.YeAddress = self._y_finance_engine.AddressFirst
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
        self.YeHigh52 = self._y_finance_engine._high52
        self.YeLow52 = self._y_finance_engine._low52
        self.YeAverage50 = self._y_finance_engine._avg50
        self.YeAverage200 = self._y_finance_engine._avg200
        self.YeMarketCap = self._y_finance_engine.MarketCap
        self.YePayoutRatio = self._y_finance_engine._ratio_payout
        self.YePeForward = self._y_finance_engine._pe_forward
        self.YePeTrailing = self._y_finance_engine._pe_trailing
        self.YePegRatio = self._y_finance_engine._ratio_peg
        self.YeShortRatio = self._y_finance_engine._ratio_short
        self.YeBookValue = self._y_finance_engine._book_value
        self.YePriceToBook = self._y_finance_engine._book_price_to
        self.YeExDividendDate = self._y_finance_engine.ExDividendDate

    def _setYahooSummary(self, a_ticker: str = 'TD'):
        self._yahooSummaryScrapper = YahooSummaryScrapper(a_ticker)
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

    def _setSimpleReturnAverage(self, a_series: pd.Series = pd.Series()) -> float:
        a_series = a_series.dropna()
        return round(100 * a_series.mean()[0], 2)

    def _setIsTimely(self, day_avg: float, week_avg: float, month_avg: float, quarter_avg: float, annual_avg: float):
        a_median: float = statistics.median([day_avg, week_avg, month_avg, quarter_avg, annual_avg])
        return (day_avg >= a_median, week_avg >= a_median, month_avg >= a_median, quarter_avg >= a_median, annual_avg >= a_median)

    def _getDataRange(self, spread_span: int = 1000, pd_series: pd.Series = pd.Series()) -> np.ndarray:
        return np.linspace(min(pd_series), max(pd_series), num=spread_span)

    def _getProbabilityDensityFunction(self, nd_array: ndarray, mu_float: float, sigma_float: float):
        return scs.norm.pdf(nd_array, loc=mu_float, scale=sigma_float)

    def _updateTimeSpan(self, t_s: TimeSpan, a_df: pd.DataFrame = pd.DataFrame()) -> TimeSpan:
        t_s.setStartDateStr(a_df.index.to_pydatetime()[0].strftime('%Y-%m-%d'))
        return t_s
