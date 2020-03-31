import pandas
import numpy as np


class AverageDirectionalIndexManager(object):
    """ Average Directional Index manager class"""
    IndicatorDf: pandas.DataFrame

    def __init__(self, a_df: pandas.DataFrame, days_span: int = 14):
        self.__setIndicator(a_df, days_span)

    def __setIndicator(self, a_df: pandas.DataFrame, days_span: int = 14):
        """ Average Directional Index calculator function"""
        df: pandas.DataFrame = a_df.copy()
        df['TR'] = self.__getAvgTrueRange(a_df)['TrueRange']
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
        self.IndicatorDf = df

    def __getAvgTrueRange(self, a_df: pandas.DataFrame, days_span: int = 20):
        """function to calculate True Range and Average True Range"""
        df: pandas.DataFrame = a_df.copy()
        df['H-L'] = abs(df['High'] - df['Low'])
        df['H-PC'] = abs(df['High'] - df['Adj Close'].shift(1))
        df['L-PC'] = abs(df['Low'] - df['Adj Close'].shift(1))
        # some take average instead of max
        df['TrueRange'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
        df['AvgTrueRate'] = df['TrueRange'].rolling(days_span).mean()
        # some take average instead of max
        df['TrueRange'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
        df['AvgTrueRate'] = df['TrueRange'].rolling(days_span).mean()
        # some use exponential mean
        # df['AvgTrueRate'] = df['TrueRange'].ewm(span=days_span,adjust=False,min_periods=days_span).mean()
        # df = df.drop(['H-L', 'H-PC', 'L-PC'], axis=1) #
        return df
