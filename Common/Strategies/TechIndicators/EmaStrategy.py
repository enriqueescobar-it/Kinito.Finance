import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.EmaIndicator import EmaIndicator


class EmaStrategy(AbstractTechIndicatorStrategy):
    __ema_indicator: EmaIndicator

    def __init__(self, ema_indicator: EmaIndicator):
        self.__ema_indicator = ema_indicator
        a_df: pd.DataFrame = self.__ema_indicator.GetData()
        self._col = self.__ema_indicator.GetCol()
        self._lower_label = a_df.columns[self.__ema_indicator.GetLowHigh()[0]]
        self._middle_label = a_df.columns[self.__ema_indicator.GetLowHigh()[1]]
        self._upper_label = a_df.columns[self.__ema_indicator.GetLowHigh()[2]]
        self._data = a_df[self.__ema_indicator.GetCol()].to_frame()
        self._data[self._lower_label] = a_df[self._lower_label]
        self._data[self._middle_label] = a_df[self._middle_label]
        self._data[self._upper_label] = a_df[self._upper_label]
        self._buy_label = self.__ema_indicator.GetLabel() + self._buy_label
        self._sell_label = self.__ema_indicator.GetLabel() + self._sell_label
        buyNsellTuple = self._buyNsell()
        self._data[self._buy_label] = buyNsellTuple[0]
        self._data[self._sell_label] = buyNsellTuple[1]
        print(self._data)

    def _buyNsell(self):
        buySignal = []
        sellSignal = []
        flagLong = False
        flagShort = False

        for i in range(len(self._data)):
            if self._data[self._middle_label][i] < self._data[self._upper_label][i] and self._data[self._lower_label][i] < self._data[self._middle_label][i] and flagLong == False:
                buySignal.append(self._data[self._col][i])
                sellSignal.append(np.nan)
                flagShort = True
            elif flagShort == True and self._data[self._lower_label][i] > self._data[self._middle_label][i]:
                buySignal.append(np.nan)
                sellSignal.append(self._data[self._col][i])
                flagShort = False
            elif self._data[self._middle_label][i] > self._data[self._upper_label][i] and self._data[self._lower_label][i] > self._data[self._middle_label][i] and flagLong == False:
                buySignal.append(self._data[self._col][i])
                sellSignal.append(np.nan)
                flagLong = True
            elif flagLong == True and self._data[self._lower_label][i] < self._data[self._middle_label][i]:
                buySignal.append(np.nan)
                sellSignal.append(self._data[self._col][i])
                flagLong = False
            else:
                buySignal.append(np.nan)
                sellSignal.append(np.nan)

        return buySignal, sellSignal

    def Plot(self):
        self.__ema_indicator.PlotData().show()
        plt.figure(figsize=self.__ema_indicator.GetFigSize())
        plt.style.use(self.__ema_indicator.GetPlotStyle())
        for a_ind, col in enumerate(self._data.columns[0:4]):
            an_alpha: float = 1.0 if a_ind == 0 else 0.3
            self._data[col].plot(alpha=an_alpha)
            print('i', an_alpha)
        plt.scatter(self.__ema_indicator.GetData().index, self._data[self._buy_label], label=self._buy_label, marker='^', color='green')
        plt.scatter(self.__ema_indicator.GetData().index, self._data[self._sell_label], label=self._sell_label, marker='v', color='red')
        plt.title(self.__ema_indicator.GetMainLabel())
        plt.xlabel(self.__ema_indicator.GetXLabel())
        plt.xticks(rotation=self.__ema_indicator.GetXticksAngle())
        plt.ylabel(self.__ema_indicator.GetYLabel())
        plt.legend(loc=self.__ema_indicator.GetLegendPlace())
        return plt
