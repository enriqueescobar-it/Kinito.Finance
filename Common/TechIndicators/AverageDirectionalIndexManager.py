import pandas
import numpy as np

from Common.TechIndicators.AbstractIndicatorManager import AbstractIndicatorManager


class AverageDirectionalIndexManager(AbstractIndicatorManager):
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
        tr_n_list = []
        DMplus_n_list = []
        DMminus_n_list = []
        tr_list = df['TR'].tolist()
        DMplus_list = df['DMplus'].tolist()
        DMminus_list = df['DMminus'].tolist()
        for i in range(len(df)):
            if i < days_span:
                tr_n_list.append(np.NaN)
                DMplus_n_list.append(np.NaN)
                DMminus_n_list.append(np.NaN)
            elif i == days_span:
                tr_n_list.append(df['TR'].rolling(days_span).sum().tolist()[days_span])
                DMplus_n_list.append(df['DMplus'].rolling(days_span).sum().tolist()[days_span])
                DMminus_n_list.append(df['DMminus'].rolling(days_span).sum().tolist()[days_span])
            elif i > days_span:
                tr_n_list.append(tr_n_list[i - 1] - (tr_n_list[i - 1] / days_span) + tr_list[i])
                DMplus_n_list.append(DMplus_n_list[i - 1] - (DMplus_n_list[i - 1] / days_span) + DMplus_list[i])
                DMminus_n_list.append(DMminus_n_list[i - 1] - (DMminus_n_list[i - 1] / days_span) + DMminus_list[i])
        df['TRn'] = np.array(tr_n_list)
        df['DMplusN'] = np.array(DMplus_n_list)
        df['DMminusN'] = np.array(DMminus_n_list)
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
