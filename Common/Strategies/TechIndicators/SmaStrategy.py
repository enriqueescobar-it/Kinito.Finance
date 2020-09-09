import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Common.Plotters.Strategies.AbstractStrategyPlotter import AbstractStrategyPlotter
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.SmaIndicator import SmaIndicator


class SmaStrategy(AbstractTechIndicatorStrategy, AbstractStrategyPlotter):
    __sma_indicator: SmaIndicator

    def __init__(self, sma_indicator: SmaIndicator):
        self.__sma_indicator = sma_indicator
        a_df: pd.DataFrame = self.__sma_indicator.GetData()
        self._col = self.__sma_indicator.GetCol()
        self._lower_label = a_df.columns[self.__sma_indicator.GetLowHigh()[0]]
        self._upper_label = a_df.columns[self.__sma_indicator.GetLowHigh()[1]]
        self._data = a_df[self.__sma_indicator.GetCol()].to_frame()
        self._data[self._lower_label] = a_df[self._lower_label]
        self._data[self._upper_label] = a_df[self._upper_label]
        self._buy_label = self.__sma_indicator.GetLabel() + self._buy_label
        self._sell_label = self.__sma_indicator.GetLabel() + self._sell_label
        buyNsellTuple = self._buyNsell()
        self._data[self._buy_label] = buyNsellTuple[0]
        self._data[self._sell_label] = buyNsellTuple[1]
        print('DATA', self._data.describe())

    def _buyNsell(self):
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

    def Plot(self):
        plt.figure(figsize=self.__sma_indicator.GetFigSize())
        plt.style.use(self.__sma_indicator.GetPlotStyle())
        plt.plot(self._data[self._col], label=self._col, alpha=0.7)
        '''
        plt.plot(self._data[self.__sma_indicator.GetLabel() + '005'], label=self.__sma_indicator.GetLabel() + '005', alpha=0.50, color='lightblue')
        plt.plot(self._data[self.__sma_indicator.GetLabel() + '009'], label=self.__sma_indicator.GetLabel() + '009', alpha=0.50, color='lightgray')
        plt.plot(self._data[self.__sma_indicator.GetLabel() + '010'], label=self.__sma_indicator.GetLabel() + '010', alpha=0.50, color='green')
        plt.plot(self._data[self.__sma_indicator.GetLabel() + '020'], label=self.__sma_indicator.GetLabel() + '020', alpha=0.50, color='orange')
        plt.plot(self._data[self.__sma_indicator.GetLabel() + '030'], label=self.__sma_indicator.GetLabel() + '030', alpha=0.50, color='violet')
        plt.plot(self._data[self.__sma_indicator.GetLabel() + '050'], label=self.__sma_indicator.GetLabel() + '050', alpha=0.50, color='pink')
        plt.plot(self._data[self.__sma_indicator.GetLabel() + '100'], label=self.__sma_indicator.GetLabel() + '100', alpha=0.50, color='red')
        plt.plot(self._data[self.__sma_indicator.GetLabel() + '200'], label=self.__sma_indicator.GetLabel() + '200', alpha=0.50, color='yellow')
        '''
        plt.scatter(self.__sma_indicator.GetData().index, self._data[self._buy_label], label=self._buy_label, marker='^', color='green')
        plt.scatter(self.__sma_indicator.GetData().index, self._data[self._sell_label], label=self._sell_label, marker='v', color='red')
        plt.title(self.__sma_indicator.GetMainLabel())
        plt.xlabel(self.__sma_indicator.GetXLabel())
        plt.xticks(rotation=self.__sma_indicator.GetXticksAngle())
        plt.ylabel(self.__sma_indicator.GetYLabel())
        plt.legend(loc=self.__sma_indicator.GetLegendPlace())
        return plt
