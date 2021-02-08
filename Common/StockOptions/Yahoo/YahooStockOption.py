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


class YahooStockOption(AbstractStockOption):
    __snp_ratio: float = 0.0
    ForecastSpan: int = 30
    _train_size: int = -1
    _test_size: int = -1
    _length: int = -1
    _training_percent: int = 0.8
    _min_max_scaler: MinMaxScaler
    _column_series_loc: pd.Series
    _column_series: pd.Series
    _date_series: pd.Series
    _column_array: ndarray
    _column_train_array: ndarray
    _column_test_array: ndarray
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
    _x_scaled_array: np.ndarray
    _x_train_array: np.ndarray
    _x_test_array: np.ndarray
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
        self._data = self._historical[self._column].to_frame()
        self._data_range = self._getDataRange(1000, self._data[self._column])
        self._mu = round(self._historical[self._column].mean(), 2)
        self._sigma = round(self._historical[self._column].std(), 2)
        self._median = round(self._historical[self._column].median(), 2)
        self._norm_pdf = self._getProbabilityDensityFunction(self.DataRange, self._mu, self._sigma)
        self._data['Norm'] = self._setNormalizer(self._historical)
        self._data['NormL1'] = self._setNormalizerL1(self._historical)
        self._data['Binary'] = self._setBinarizer(self._historical)
        self._data['Sparse'] = self._setSparser(self._historical)
        self._data['Scaled'] = self._setScaler(self._historical)
        self._setPreProcessing(self._historical)
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
        (self.IsDaily, self.IsWeekly, self.IsMonthly, self.IsQuarterly, self.IsAnnually) = \
            self._setIsTimely(self.SimpleDailyReturnAvg, self.SimpleWeeklyReturnAvg,
                              self.SimpleMonthlyReturnAvg, self.SimpleQuarterlyReturnAvg, self.SimpleAnnuallyReturnAvg)
        self._setYahooFinance(a_ticker)
        self._setYahooSummary(a_ticker)

    @property
    def SnpRatio(self):
        return self.__snp_ratio

    @property
    def ArrayScaledX(self):
        return self._x_scaled_array

    @property
    def ArrayTestX(self):
        return self._x_test_array

    @property
    def ArrayTrainX(self):
        return self._x_train_array

    @property
    def ColumnLocSeries(self):
        return self._column_series_loc

    @property
    def ColumnSeries(self):
        return self._column_series

    @property
    def ColumnArray(self):
        return self._column_array

    @property
    def ColumnTestArray(self):
        return self._column_test_array

    @property
    def ColumnTrainArray(self):
        return self._column_train_array

    @property
    def DateSeries(self):
        return self._date_series

    @property
    def TrainPercent(self):
        return self._training_percent

    @property
    def TestSize(self):
        return self._test_size

    @property
    def TrainSize(self):
        return self._train_size

    @property
    def Length(self):
        return self._length

    @property
    def MinMaxScale(self):
        return self._min_max_scaler

    def SetSnpRatio(self, a_df: pd.DataFrame, a_col: str):
        a_series = round(self.Data['Norm'].divide(a_df[a_col].replace(0, 1)), 3)
        self.__snp_ratio = a_series[-1]

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
        return round(self.YeHigh52, 6)

    def __setLow52(self, a_df) -> float:
        return round(self.YeLow52, 6)

    def __setPrice(self, a_df) -> float:
        i = a_df['Adj Close'].iloc[-1]
        return round(i, 6)

    def _setNormalizer(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return (a_df / a_df.iloc[0])[self.Column]

    def _setNormalizerL1(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return \
            pd.DataFrame(preprocessing.normalize(a_df, norm='l1'), columns=a_df.columns, index=a_df.index)[self.Column]

    def _setBinarizer(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return \
            pd.DataFrame(preprocessing.Binarizer(threshold=1.4).transform(a_df), columns=a_df.columns,
                         index=a_df.index)[self.Column]

    def _setSparser(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return pd.DataFrame(preprocessing.scale(a_df), columns=a_df.columns, index=a_df.index)[self.Column]

    def _setScaler(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        # scale to compare array from 0.0 to 100.0
        minMaxScaler: MinMaxScaler = preprocessing.MinMaxScaler(feature_range=(0.0, 100.0))
        # scale to compare data frame
        stockArrayScaled: np.ndarray = minMaxScaler.fit_transform(a_df)
        return pd.DataFrame(stockArrayScaled, columns=a_df.columns, index=a_df.index)[self.Column]

    def _setPreProcessing(self, a_df: pd.DataFrame()):
        self._length = len(a_df)
        self._train_size = int(self._length * self._training_percent)
        self._test_size = self._length - self._train_size
        self._period_days = 60
        self._min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
        self._column_series_loc = self._historical.loc[:, self._column]
        self._column_series = self._historical.reset_index()[self._column]
        self._date_series = self._historical.reset_index()['Date']
        self._column_array = self._min_max_scaler.fit_transform(np.array(self._column_series).reshape(-1, 1))
        self._column_train_array = self._column_array[0:self._train_size, :]
        self._column_test_array = self._column_array[self._train_size:len(self._column_array), :1]
        '''df = a_df.copy()
        data_training = df[:self._train_size].copy()
        data_training = data_training.drop(self.Column, inplace=False, axis=1)
        data_training = minMaxScaler.fit_transform(data_training)
        print(data_training)
        data_testing = df[self._train_size: self._length].copy()
        print(data_testing.head())
        print(len(data_training))
        print(len(data_testing))
        x_train = []
        y_train = []
        for i in range(60, data_training.shape[0]):
            x_train.append(data_training[i - 60:i])
            y_train.append(data_training[i, 0])
        x_train, y_train = np.array(x_train), np.array(y_train)
        print(x_train.shape)
        # Build LSTM
        from tensorflow.keras import Sequential
        from tensorflow.keras.layers import Dense, LSTM, Dropout
        import matplotlib as plt
        regressor = Sequential()
        regressor.add(LSTM(units=60, activation='relu', return_sequences=True, input_shape=(x_train.shape[1], 5)))
        regressor.add(Dropout(0.2))
        regressor.add(LSTM(units=60, activation='relu', return_sequences=True))
        regressor.add(Dropout(0.2))
        regressor.add(LSTM(units=80, activation='relu', return_sequences=True))
        regressor.add(Dropout(0.2))
        regressor.add(LSTM(units=120, activation='relu'))
        regressor.add(Dropout(0.2))
        regressor.add(Dense(units=1))
        regressor.compile(optimizer='adam', loss='mean_squared_error')
        regressor.fit(x_train, y_train, epochs=50, batch_size=32)
        # prepare date set
        print(data_testing.head())
        past_60_days = data_training[-61:]#  .tail(60)
        new_df = past_60_days.append(data_testing, ignore_index=True)
        new_df = new_df.drop(['Date', 'Adj Close'], axis=1)
        print(new_df.head())
        inputs = minMaxScaler.transform(df)
        print(inputs)
        x_test = []
        y_test = []

        for i in range(60, inputs.shape[0]):
            x_test.append(inputs[i-60:i])
            y_test.append(inputs[i, 0])

        X_test, y_test = np.array(x_test), np.array(y_test)
        x_test.shape, y_test.shape
        y_pred = regressor.predict(x_test)
        print(minMaxScaler.scale_)
        scale = 1/8.18605127e-04
        print(scale)
        y_pred = y_pred*scale
        y_test = y_test*scale
        # viz
        # Visualising the results
        plt.figure(figsize=(14,5))
        plt.plot(y_test, color = 'red', label = 'Real Google Stock Price')
        plt.plot(y_pred, color = 'blue', label = 'Predicted Google Stock Price')
        plt.title('Google Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Google Stock Price')
        plt.legend()
        plt.show()
        exit(123)
        df_train = df[:1]
        df = np.reshape(df.values, (-1, 1))
        self._x_scaled_array = minMaxScaler.fit_transform(df)
        self._x_train_array = self._x_scaled_array[:self._train_size]
        self._x_test_array = self._x_scaled_array[self._train_size: self._length]
        self._x_train_array, self._x_test_array = self._x_scaled_array[0: self._train_size, :], self._x_scaled_array[
                                                                                                self._train_size:self._length,
                                                                                                :]
        print(len(self._x_train_array))
        print(len(self._x_test_array))
        exit(123)
        # self._x_test_array = self._x_scaled_array[self._split : self._length]
        exit(123)'''

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
        dfLength80 = int(round(dfLength * 0.8))
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
            a = train[self.Column][len(train) - dfLength20 + i:].sum() + sum(preds)
            b = a / dfLength20
            preds.append(b)
        self.RMSE = np.sqrt(np.mean(np.power((np.array(test[self.Column]) - preds), 2)))
        print('\n RMSE value on validation set:', self.RMSE)
        lin_svr = SVR(kernel='linear', C=1000.0)
        # lin_svr.fit(self.HistoricalSimpleReturns.index, self.HistoricalSimpleReturns[self.SourceColumn])
        ##
        # T = len(test)
        # N = len(test)
        # S_0 = df[train.index[-1]]#.date()]
        # N_SIM = 100
        # mu = train.mean()
        # sigma = train.std()
        # gbm_simulations: ndarray = self.simulate_gbm(S_0, mu, sigma, N_SIM, T, N)
        # gbm_simulationsT: ndarray = np.transpose(gbm_simulations)
        # print('gbm_simulationsT', gbm_simulationsT.shape)
        # prepare objects for plotting
        # LAST_TRAIN_DATE = train.index[-1].date()
        # FIRST_TEST_DATE = test.index[0].date()
        # LAST_TEST_DATE = test.index[-1].date()
        # PLOT_TITLE = f'{self.Ticker} Simulation ({FIRST_TEST_DATE}:{LAST_TEST_DATE})'
        # selected_indices = self.HistoricalData[self.SourceColumn][LAST_TRAIN_DATE:LAST_TEST_DATE].index
        # a_index = [date.date() for date in selected_indices]
        # print('a_index', len(a_index))
        # gbm_simulationsDf = pd.DataFrame(data=gbm_simulationsT, index=a_index)
        # print('gbm_simulationsDf', gbm_simulationsDf.shape)
        # plotting
        # ax = gbm_simulationsDf.plot(alpha=0.2, legend=False)
        # line_1, = ax.plot(a_index, gbm_simulationsDf.mean(axis=1), color='red')
        # line_2, = ax.plot(a_index, self.HistoricalData[self.SourceColumn][LAST_TRAIN_DATE:LAST_TEST_DATE], color='blue')
        # ax.set_title(PLOT_TITLE, fontsize=16)
        # ax.legend((line_1, line_2), ('mean', 'actual'))
        # plt.show()
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
        print(self._y_finance_engine)
        print(self._y_finance_engine.StockType)
        exit(-222)
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
        self.YeHigh52 = self._y_finance_engine.High52
        self.YeLow52 = self._y_finance_engine.Low52
        self.YeAverage50 = self._y_finance_engine.Average50
        self.YeAverage200 = self._y_finance_engine.Average200
        self.YeMarketCap = self._y_finance_engine.MarketCap
        self.YePayoutRatio = self._y_finance_engine.RatioPayout
        self.YePeForward = self._y_finance_engine.PeForward
        self.YePeTrailing = self._y_finance_engine.PeTrailing
        self.YePegRatio = self._y_finance_engine.RatioPeg
        self.YeShortRatio = self._y_finance_engine.RatioShort
        self.YeBookValue = self._y_finance_engine.BookValue
        self.YePriceToBook = self._y_finance_engine.BookPriceTo
        self.YeExDividendDate = self._y_finance_engine.DateExDividend

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
        dt = T / N
        dW = np.random.normal(scale=np.sqrt(dt), size=(n_sims, N))
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
        return (day_avg >= a_median, week_avg >= a_median, month_avg >= a_median, quarter_avg >= a_median,
                annual_avg >= a_median)

    def _getDataRange(self, spread_span: int = 1000, pd_series: pd.Series = pd.Series()) -> np.ndarray:
        return np.linspace(min(pd_series), max(pd_series), num=spread_span)

    def _getProbabilityDensityFunction(self, nd_array: ndarray, mu_float: float, sigma_float: float):
        return scs.norm.pdf(nd_array, loc=mu_float, scale=sigma_float)

    def _updateTimeSpan(self, t_s: TimeSpan, a_df: pd.DataFrame = pd.DataFrame()) -> TimeSpan:
        t_s.setStartDateStr(a_df.index.to_pydatetime()[0].strftime('%Y-%m-%d'))
        return t_s
