from datetime import date
import numpy as np
from pandas import DataFrame
from pandas_datareader import get_data_yahoo
from stocktrends import Renko
import Data.Yahoo.YahooTicker as YahooTicker


class YahooPdrManager(object):
    """description of class"""
    DateTo: date
    DateFrom: date
    YahooData: DataFrame
    YahooDailyReturn: DataFrame

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
        ### self.__setAvgDirectionalIndeX(14)
        # self.__setRenko()

    def __updateDailyReturn(self):
        self.YahooDailyReturn = self.YahooData.pct_change()

    def FillNaWithNextValue(self):
        self.YahooData.fillna(method='bfill', axis=0, inplace=True)
        self.__updateDailyReturn()

    def DropRowsWithNan(self):
        self.YahooData.dropna(how='any', axis=0, inplace=True)
        self.__updateDailyReturn()

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

    def __setRenko(self):
        """function to convert ohlc data into renko bricks"""
        df: DataFrame = self.YahooData.copy()
        df.reset_index(inplace=True)
        df = df.iloc[:, [0, 1, 2, 3, 5, 6]]
        df.rename(columns={"Date": "date", "High": "high", "Low": "low", "Open": "open", "Adj Close": "close",
                           "Volume": "volume"}, inplace=True)
        df2 = Renko(df)
        df2.brick_size = round(self.__getAvgTrueRange(self.YahooData.copy(), 120)["AvgTrueRate"][-1], 0)
        # if get_bricks() does not work try using get_ohlc_data() instead
        # df2.get_bricks() error => using get_ohlc_data()
        # renkoDataFrame = df2.get_bricks()
        renkoDataFrame: DataFrame = df2.get_ohlc_data()
        self.YahooRenko = renkoDataFrame
