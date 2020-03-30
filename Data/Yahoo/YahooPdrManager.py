from datetime import date
import datetime
from stocktrends import Renko

import numpy as np
import pandas as pd
import statsmodels.api as sm
from pandas import DataFrame
from pandas_datareader import get_data_yahoo

import Data.Yahoo.YahooTicker as YahooTicker


class YahooPdrManager(object):
    """description of class"""
    DateTo: date
    DateFrom: date
    YahooATR: DataFrame
    YahooBollingerBang: DataFrame
    YahooData: DataFrame
    YahooDailyReturn: DataFrame
    YahooOnBalanceDemand: DataFrame
    YahooMACD: DataFrame
    YahooSlopes: DataFrame

    def __init__(self, yahoo_ticker: YahooTicker, from_date: date, to_date: date, y_data=None):
        self.DateTo = to_date
        self.DateFrom = from_date
        self.__ticker = yahoo_ticker
        if y_data is None:
            gdy = get_data_yahoo(self.__ticker.TickerName, from_date, to_date)
            gdy.dropna(inplace=True)
            self.YahooData = gdy
        else:
            self.YahooData = y_data
        self.__updateDailyReturn()
        self.__setMovAvgConvDiv()
        self.__setAvgTrueRate(20)
        self.__SetBollingerBang(20)
        # self.__serRsi(14)
        self.__setRsiLoop(14)
        self.__setAvgDirectionalIndeX(14)
        self.__setOnBalanceDemand()
        self.__setSlope()
        # self.__setRenko()

    def __updateDailyReturn(self):
        self.YahooDailyReturn = self.YahooData.pct_change()

    def FillNaWithNextValue(self):
        self.YahooData.fillna(method='bfill', axis=0, inplace=True)
        self.__updateDailyReturn()

    def DropRowsWithNan(self):
        self.YahooData.dropna(how='any', axis=0, inplace=True)
        self.__updateDailyReturn()

    def __setMovAvgConvDiv(self, a: int = 12, b: int = 26, c: int = 9):
        """function to calculate Moving Average Conversion Divergence"""
        df: DataFrame = self.YahooData.copy()
        df["MA_Fast"] = df["Adj Close"].ewm(span=a, min_periods=a).mean()
        df["MA_Slow"] = df["Adj Close"].ewm(span=b, min_periods=b).mean()
        df["MACD"] = df["MA_Fast"] - df["MA_Slow"]
        df["Signal"] = df["MACD"].ewm(span=c, min_periods=c).mean()
        df.dropna(inplace=True)
        self.YahooMACD = df

    def __setAvgTrueRate(self, days_span: int = 20):
        """function to calculate True Range and Average True Range"""
        df: DataFrame = self.YahooData.copy()
        df['H-L'] = abs(df['High'] - df['Low'])
        df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))
        df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1))
        # some take average instead of max
        df['TrueRange'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
        df['AvgTrueRate'] = df['TrueRange'].rolling(days_span).mean()
        # some use exponential mean
        # df['AvgTrueRate'] = df['TrueRange'].ewm(span=days_span,adjust=False,min_periods=days_span).mean()
        self.YahooATR = df.drop(['H-L', 'H-PC', 'L-PC'], axis=1)

    def __getAvgTrueRate(self, DF: DataFrame, n: int):
        """function to calculate True Range and Average True Range"""
        df: DataFrame = DF.copy()
        df['H-L'] = abs(df['High'] - df['Low'])
        df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))
        df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1))
        df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
        df['ATR'] = df['TR'].rolling(n).mean()
        df2 = df.drop(['H-L', 'H-PC', 'L-PC'], axis=1)
        return df2

    def __SetBollingerBang(self, days_span: int = 20):
        """function to calculate Bollinger Band"""
        df: DataFrame = self.YahooData.copy()
        df["MA"] = df['Adj Close'].rolling(days_span).mean()
        # ddof=0 is required since we want to take the standard deviation of the population and not sample
        df["BB_up"] = df["MA"] + 2 * df['Adj Close'].rolling(days_span).std(ddof=0)
        # ddof=0 is required since we want to take the standard deviation of the population and not sample
        df["BB_dn"] = df["MA"] - 2 * df['Adj Close'].rolling(days_span).std(ddof=0)
        df["BB_width"] = df["BB_up"] - df["BB_dn"]
        df.dropna(inplace=True)
        self.YahooBollingerBang = df

    def __serRsi(self, days_span: int = 14):
        """function to calculate RSI without using loop"""
        df: DataFrame = self.YahooData.copy()
        delta = df["Adj Close"].diff().dropna()
        u = delta * 0
        d = u.copy()
        u[delta > 0] = delta[delta > 0]
        d[delta < 0] = -delta[delta < 0]
        # first value is sum of avg gains
        u[u.index[days_span - 1]] = np.mean(u[:days_span])
        u = u.drop(u.index[:(days_span - 1)])
        # first value is sum of avg losses
        d[d.index[days_span - 1]] = np.mean(d[:days_span])
        d = d.drop(d.index[:(days_span - 1)])
        rs = pd.stats.moments.ewma(u, com=days_span - 1, adjust=False) / pd.stats.moments.ewma(d, com=days_span - 1,
                                                                                               adjust=False)
        self.YahooRsi = (100 - 100 / (1 + rs))

    def __setRsiLoop(self, days_span: int = 14):
        """function to calculate RSI with loop"""
        df: DataFrame = self.YahooData.copy()
        df['delta'] = df['Adj Close'] - df['Adj Close'].shift(1)
        df['gain'] = np.where(df['delta'] >= 0, df['delta'], 0)
        df['loss'] = np.where(df['delta'] < 0, abs(df['delta']), 0)
        avg_gain = []
        avg_loss = []
        gain_list = df['gain'].tolist()
        loss_list = df['loss'].tolist()
        for i in range(len(df)):
            if i < days_span:
                avg_gain.append(np.NaN)
                avg_loss.append(np.NaN)
            elif i == days_span:
                avg_gain.append(df['gain'].rolling(days_span).mean().tolist()[days_span])
                avg_loss.append(df['loss'].rolling(days_span).mean().tolist()[days_span])
            elif i > days_span:
                avg_gain.append(((days_span - 1) * avg_gain[i - 1] + gain_list[i]) / days_span)
                avg_loss.append(((days_span - 1) * avg_loss[i - 1] + loss_list[i]) / days_span)
        df['avg_gain'] = np.array(avg_gain)
        df['avg_loss'] = np.array(avg_loss)
        df['RS'] = df['avg_gain'] / df['avg_loss']
        df['RSI'] = 100 - (100 / (1 + df['RS']))
        self.YahooRsiLoop = df['RSI']

    def __setAvgDirectionalIndeX(self, days_span: int = 14):
        """function to calculate RSI with loop"""
        df: DataFrame = self.YahooData.copy()
        # the period parameter of ATR function does not matter because period does not influence TR calculation
        df['TR'] = self.YahooATR['TrueRange']
        df['DMplus'] = np.where((df['High'] - df['High'].shift(1)) > (df['Low'].shift(1) - df['Low']),
                                df['High'] - df['High'].shift(1), 0)
        df['DMplus'] = np.where(df['DMplus'] < 0, 0, df['DMplus'])
        df['DMminus'] = np.where((df['Low'].shift(1) - df['Low']) > (df['High'] - df['High'].shift(1)),
                                 df['Low'].shift(1) - df['Low'], 0)
        df['DMminus'] = np.where(df['DMminus'] < 0, 0, df['DMminus'])
        TRn = []
        DMplusN = []
        DMminusN = []
        TR = df['TR'].tolist()
        DMplus = df['DMplus'].tolist()
        DMminus = df['DMminus'].tolist()
        for i in range(len(df)):
            if i < days_span:
                TRn.append(np.NaN)
                DMplusN.append(np.NaN)
                DMminusN.append(np.NaN)
            elif i == days_span:
                TRn.append(df['TR'].rolling(days_span).sum().tolist()[days_span])
                DMplusN.append(df['DMplus'].rolling(days_span).sum().tolist()[days_span])
                DMminusN.append(df['DMminus'].rolling(days_span).sum().tolist()[days_span])
            elif i > days_span:
                TRn.append(TRn[i - 1] - (TRn[i - 1] / days_span) + TR[i])
                DMplusN.append(DMplusN[i - 1] - (DMplusN[i - 1] / days_span) + DMplus[i])
                DMminusN.append(DMminusN[i - 1] - (DMminusN[i - 1] / days_span) + DMminus[i])
        df['TRn'] = np.array(TRn)
        df['DMplusN'] = np.array(DMplusN)
        df['DMminusN'] = np.array(DMminusN)
        df['DIplusN'] = 100 * (df['DMplusN'] / df['TRn'])
        df['DIminusN'] = 100 * (df['DMminusN'] / df['TRn'])
        df['DIdiff'] = abs(df['DIplusN'] - df['DIminusN'])
        df['DIsum'] = df['DIplusN'] + df['DIminusN']
        df['DX'] = 100 * (df['DIdiff'] / df['DIsum'])
        adx_list = []
        dx_list = df['DX'].tolist()
        for j in range(len(df)):
            if j < 2 * days_span - 1:
                adx_list.append(np.NaN)
            elif j == 2 * days_span - 1:
                adx_list.append(df['DX'][j - days_span + 1:j + 1].mean())
            elif j > 2 * days_span - 1:
                adx_list.append(((days_span - 1) * adx_list[j - 1] + dx_list[j]) / days_span)
        df['ADX'] = np.array(adx_list)
        self.YahooADX = df['ADX']

    def __setOnBalanceDemand(self):
        """function to calculate On Balance Volume"""
        df: DataFrame = self.YahooData.copy()
        df['daily_ret'] = df['Adj Close'].pct_change()
        df['direction'] = np.where(df['daily_ret'] >= 0, 1, -1)
        df['direction'][0] = 0
        df['vol_adj'] = df['Volume'] * df['direction']
        df['obv'] = df['vol_adj'].cumsum()
        self.YahooOnBalanceDemand = df

    def __setSlope(self, nb_points: int = 5):
        """function to calculate the slope of n consecutive points on a plot"""
        df: DataFrame = self.YahooData.copy()
        n: int = nb_points  # you can use 20 or more
        slopes = [i * 0 for i in range(n - 1)]
        ser = df['Adj Close']
        i: int
        for i in range(n, len(ser) + 1):
            y = ser[i - n:i]
            x = np.array(range(n))
            y_scaled = (y - y.min()) / (y.max() - y.min())
            x_scaled = (x - x.min()) / (x.max() - x.min())
            # y = mx+c this is c
            x_scaled = sm.add_constant(x_scaled)
            model = sm.OLS(y_scaled, x_scaled)
            results = model.fit()
            slopes.append(results.params[-1])
        slope_angle = (np.rad2deg(np.arctan(np.array(slopes))))
        df['Slopes'] = np.array(slope_angle)
        self.YahooSlopes = df

    def __setRenko(self):
        """function to convert ohlc data into renko bricks"""
        df: DataFrame = self.YahooData.copy()
        df.reset_index(inplace=True)
        df = df.iloc[:, [0, 1, 2, 3, 5, 6]]
        df.rename(columns={"Date": "date", "High": "high", "Low": "low", "Open": "open", "Adj Close": "close",
                           "Volume": "volume"}, inplace=True)
        df2 = Renko(df)
        df2.brick_size = round(self.__getAvgTrueRate(self.YahooData.copy(), 120)["AvgTrueRate"][-1], 0)
        # if get_bricks() does not work try using get_ohlc_data() instead
        # df2.get_bricks() error => using get_ohlc_data()
        # renkoDataFrame = df2.get_bricks()
        renkoDataFrame: DataFrame = df2.get_ohlc_data()
        self.YahooRenko = renkoDataFrame
