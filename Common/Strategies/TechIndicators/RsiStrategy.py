from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.RsiIndicator import RsiIndicator


class RsiStrategy(AbstractTechIndicatorStrategy):
    _rsi_indicator: RsiIndicator
    _summary: pd.DataFrame
    __data: pd.DataFrame

    def __init__(self, rsi_indicator: RsiIndicator):
        self._rsi_indicator = rsi_indicator
        a_df: pd.DataFrame = self._rsi_indicator.GetData()
        self._col = self._rsi_indicator.Column
        print(a_df.columns)
        #
        #
        #
        self._data = a_df[self._rsi_indicator.Column].to_frame()
        #
        #
        #
        self._buy_label = self._rsi_indicator.Label + self._buy_label
        self._sell_label = self._rsi_indicator.Label + self._sell_label
        print(self._data.columns)
        self.__setData()
        exit(88)
        self.__data = rsi_indicator.GetData()
        self.__setUpAndDown()
        self.__setAverages()
        self.__completeAverages()
        self._setSummary()

    @property
    def Summary(self):
        return self._summary

    def PlotAx(self, ax: object) -> object:
        return ax

    def Plot(self) -> plt:
        pass

    def PlotAll(self) -> plt:
        pass

    def _buyNsell(self):
        pass

    def __setData(self):
        self._data['UpMove'] = np.nan
        self._data['DownMove'] = np.nan
        self._data = self.__setUpAndDown(self._data)
        self._data['UpAverage'] = np.nan
        self._data['DownAverage'] = np.nan
        self._data['RS'] = np.nan
        self._data['RSI'] = np.nan
        self._data = self.__setAverages(self._data)
        self._data = self.__completeAverages(self._data)
        print(self._data.UpAverage)
        self._data['LongTomorrow'] = np.nan
        self._data['Buy'] = np.nan
        self._data['Sell'] = np.nan
        self._data['BuyRSI'] = np.nan
        self._data['SellRSI'] = np.nan
        self._data['BuyAndSell'] = np.nan

    def __setUpAndDown(self, a_df: pd.DataFrame) -> pd.DataFrame:
        for x in range(1, len(a_df)):
            a_df['UpMove'][x] = 0
            a_df['DownMove'][x] = 0

            if a_df[self._col][x] > a_df[self._col][x - 1]:
                a_df['UpMove'][x] = a_df[self._col][x] - a_df[self._col][x - 1]

            if a_df[self._col][x] < a_df[self._col][x - 1]:
                a_df['DownMove'][x] = abs(a_df[self._col][x] - a_df[self._col][x - 1])
        return a_df

    def __setAverages(self, a_df: pd.DataFrame) -> pd.DataFrame:
        a_df['UpAverage'][14] = a_df['UpMove'][1:15].mean()
        a_df['DownAverage'][14] = a_df['DownMove'][1:15].mean()
        a_df['RS'][14] = a_df['UpAverage'][14] / a_df['DownAverage'][14]
        a_df['RSI'][14] = 100 - (100 / (1 + a_df['RS'][14]))
        return a_df

    def __completeAverages(self, a_df: pd.DataFrame) -> pd.DataFrame:
        for x in range(15, len(a_df)):
            a_df['UpAverage'][x] = (a_df['UpAverage'][x - 1] * 13 + a_df['UpMove'][x]) / 14
            a_df['DownAverage'][x] = (a_df['DownAverage'][x - 1] * 13 + a_df['DownMove'][x]) / 14
            a_df['RS'][x] = a_df['UpAverage'][x] / a_df['DownAverage'][x]
            a_df['RSI'][x] = 100 - (100 / (1 + a_df['RS'][x]))
        return a_df

    def _setSummary(self):
        self._summary = pd.DataFrame(index=self.__data.index)
        self._summary['LongTomorrow'] = np.nan
        self._summary['Buy'] = np.nan
        self._summary['Sell'] = np.nan
        self._summary['BuyRSI'] = np.nan
        self._summary['SellRSI'] = np.nan
        self._summary['BuyAndSell'] = np.nan
        for x in range(15, len(self.__data)):
            # long tomorrow
            if (self.__data['RSI'][x] <= 40) & (self.__data['RSI'][x - 1] > 40):
                self._summary['LongTomorrow'][x] = True
            elif (self._summary['LongTomorrow'][x - 1] == True) & (self.__data['RSI'][x] <= 70):
                self._summary['LongTomorrow'][x] = True
            else:
                self._summary['LongTomorrow'][x] = False
            # buy
            if (self._summary['LongTomorrow'][x] == True) & (self._summary['LongTomorrow'][x - 1] == False):
                self._summary['Buy'][x] = self.__data[self._col][x]
                self._summary['BuyRSI'][x] = self.__data['RSI'][x]
            # sell
            if (self._summary['LongTomorrow'][x] == False) & (self._summary['LongTomorrow'][x - 1] == True):
                self._summary['Sell'][x] = self.__data[self._col][x]
                self._summary['SellRSI'][x] = self.__data['RSI'][x]
        self._summary['BuyAndSell'][15] = self.__data[self._col][15]
        for x in range(16, len(self.__data)):
            if self._summary['LongTomorrow'][x - 1] == True:
                self._summary['BuyAndSell'][x] = self._summary['BuyAndSell'][x - 1] * (
                            self.__data[self._col][x] / self.__data[self._col][x - 1])
            else:
                self._summary['BuyAndSell'][x] = self._summary['BuyAndSell'][x - 1]
        '''self._summary['Buy'] = self._data[self._buy_label].replace(np.nan, 0)
        self._summary['Buy'][self._summary['Buy'] > 0] = 1
        self._summary['Sell'] = self._data[self._sell_label].replace(np.nan, 0)
        self._summary['Sell'][self._summary['Sell'] > 0] = 1
        self._summary['BuyAndSell'] = 0
        last_float: float = 0.0
        for ind in self._summary.index:
            if self._summary['Buy'][ind] > self._summary['Sell'][ind]:
                self._summary['BuyAndSell'][ind] = 1.0
                last_float = 1.0
            elif self._summary['Buy'][ind] < self._summary['Sell'][ind]:
                self._summary['BuyAndSell'][ind] = -1.0
                last_float = -1.0
            else: # row['Buy'] == row['Sell']
                self._summary['BuyAndSell'][ind] = last_float'''
