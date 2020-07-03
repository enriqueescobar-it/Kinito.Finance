import pandas
import pandas as pd
import numpy as np

from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class RelativeStrengthIndexIndicator(AbstractTechIndicator):
    """Relative Strength Index manager"""
    IndicatorDf: pandas.DataFrame

    def __init__(self, a_df: pandas.DataFrame):
        self.__setIndicator(a_df)
        # self.getIndicator(a_df, 20)

    def __setIndicator(self, a_df: pandas.DataFrame, days_span: int = 14):
        """function to calculate RSI with loop"""
        df: pandas.DataFrame = a_df.copy()
        df['RsiDelta'] = df['Adj Close'] - df['Adj Close'].shift(1)
        df['RsiGain'] = np.where(df['RsiDelta'] >= 0, df['RsiDelta'], 0)
        df['RsiLoss'] = np.where(df['RsiDelta'] < 0, abs(df['RsiDelta']), 0)
        avg_gain = []
        avg_loss = []
        gain_list = df['RsiGain'].tolist()
        loss_list = df['RsiLoss'].tolist()
        for i in range(len(df)):
            if i < days_span:
                avg_gain.append(np.NaN)
                avg_loss.append(np.NaN)
            elif i == days_span:
                avg_gain.append(df['RsiGain'].rolling(days_span).mean().tolist()[days_span])
                avg_loss.append(df['RsiLoss'].rolling(days_span).mean().tolist()[days_span])
            elif i > days_span:
                avg_gain.append(((days_span - 1) * avg_gain[i - 1] + gain_list[i]) / days_span)
                avg_loss.append(((days_span - 1) * avg_loss[i - 1] + loss_list[i]) / days_span)
        df['RsiAvgGain'] = np.array(avg_gain)
        df['RsiAvgLoss'] = np.array(avg_loss)
        df['RelativeStrength'] = df['RsiAvgGain'] / df['RsiAvgLoss']
        df['RelativeStrengthIndex'] = 100 - (100 / (1 + df['RelativeStrength']))
        self.IndicatorDf = df

    def getIndicator(self, a_df, days_span: int = 14):
        """function to calculate RSI without using loop"""
        df: pandas.DataFrame = a_df.copy()
        delta = df["Adj Close"].diff().dropna()
        up_delta = delta * 0
        down_delta = up_delta.copy()
        up_delta[delta > 0] = delta[delta > 0]
        down_delta[delta < 0] = -delta[delta < 0]
        # first value is sum of avg gains
        up_delta[up_delta.index[days_span - 1]] = np.mean(up_delta[:days_span])
        up_delta = up_delta.drop(up_delta.index[:(days_span - 1)])
        # first value is sum of avg losses
        down_delta[down_delta.index[days_span - 1]] = np.mean(down_delta[:days_span])
        down_delta = down_delta.drop(down_delta.index[:(days_span - 1)])
        rs = pd.stats.moments.ewma(up_delta, com=days_span - 1, adjust=False)\
             / pd.stats.moments.ewma(down_delta, com=days_span - 1, adjust=False)
        return 100 - 100 / (1 + rs)
