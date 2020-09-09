import pandas as pd
import numpy as np

from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.SmaIndicator import SmaIndicator


class SmaStrategy(AbstractTechIndicatorStrategy):

    def __init__(self, sma_indicator: SmaIndicator):
        a_df: pd.DataFrame = sma_indicator.GetData()
        self._col = sma_indicator.GetCol()
        self._lower_label = a_df.columns[sma_indicator.GetLowHigh()[0]]
        self._upper_label = a_df.columns[sma_indicator.GetLowHigh()[1]]
        self._data = a_df[sma_indicator.GetCol()].to_frame()
        self._data[self._lower_label] = a_df[self._lower_label]
        self._data[self._upper_label] = a_df[self._upper_label]
        self._buy_label += sma_indicator.GetLabel()
        self._sell_label += sma_indicator.GetLabel()
        buyNsellTuple = self.__buyNsell()
        self._data[self._buy_label] = buyNsellTuple[0]
        self._data[self._sell_label] = buyNsellTuple[1]
        print('DATA', self._data.describe())

    def __buyNsell(self):
        buySignal = []
        sellSignal = []
        flag = -1

        for i in range(len(self._data)):
            if self._data[self._lower_label][i] > self._data[self._upper_label][i]:#
                if flag != 1:
                    buySignal.append(self._data[self._col][i])
                    sellSignal.append(np.nan)
                    flag = 1
                else:
                    buySignal.append(np.nan)
                    sellSignal.append(np.nan)
            elif self._data[self._lower_label][i] < self._data[self._upper_label][i]:#
                if flag != 0:
                    buySignal.append(np.nan)
                    sellSignal.append(self._data[self._col][i])
                    flag = 0
                else:
                    buySignal.append(np.nan)
                    sellSignal.append(np.nan)
            else:
                buySignal.append(np.nan)
                sellSignal.append(np.nan)

        return buySignal, sellSignal
