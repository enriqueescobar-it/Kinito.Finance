from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.RsiIndicator import RsiIndicator


class RsiStrategy(AbstractTechIndicatorStrategy):
    _rsi_indicator: RsiIndicator
    _col: str = 'Adj Close'
    _summary: pd.DataFrame
    __data: pd.DataFrame

    def __init__(self, rsi_indicator: RsiIndicator):
        self.__data = rsi_indicator.GetData()
        self.__data['UpMove'] = np.nan
        self.__data['DownMove'] = np.nan
        self.__setUpAndDown()
        self.__setAverages()
        self.__completeUpAndDown()
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

    def __setUpAndDown(self):
        for x in range(1, len(self.__data)):
            self.__data['UpMove'][x] = 0
            self.__data['DownMove'][x] = 0

            if self.__data[self._col][x] > self.__data[self._col][x - 1]:
                self.__data['UpMove'][x] = self.__data[self._col][x] - self.__data[self._col][x - 1]

            if self.__data[self._col][x] < self.__data[self._col][x - 1]:
                self.__data['DownMove'][x] = abs(self.__data[self._col][x] - self.__data[self._col][x - 1])

    def __setAverages(self):
        self.__data['AverageUp'] = np.nan
        self.__data['AverageDown'] = np.nan
        self.__data['AverageUp'][14] = self.__data['UpMove'][1:15].mean()
        self.__data['AverageDown'][14] = self.__data['DownMove'][1:15].mean()
        self.__data['RS'] = np.nan
        self.__data['RSI'] = np.nan
        self.__data['RS'][14] = self.__data['AverageUp'][14] / self.__data['AverageDown'][14]
        self.__data['RSI'][14] = 100 - (100 / (1 + self.__data['RS'][14]))

    def __completeUpAndDown(self):
        for x in range(15, len(self.__data)):
            self.__data['AverageUp'][x] = (self.__data['AverageUp'][x - 1] * 13 + self.__data['UpMove'][x]) / 14
            self.__data['AverageDown'][x] = (self.__data['AverageDown'][x - 1] * 13 + self.__data['DownMove'][x]) / 14
            self.__data['RS'][x] = self.__data['AverageUp'][x] / self.__data['AverageDown'][x]
            self.__data['RSI'][x] = 100 - (100 / (1 + self.__data['RS'][x]))
