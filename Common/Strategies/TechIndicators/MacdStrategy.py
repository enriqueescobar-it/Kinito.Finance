from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.MacdIndicator import MacdIndicator


class MacdStrategy(AbstractTechIndicatorStrategy):
    __macd_indicator: MacdIndicator

    def __init__(self, macd_indicator: MacdIndicator):
        self.__macd_indicator = macd_indicator
        a_df: pd.DataFrame = self.__macd_indicator.GetData()
        self._col = self.__macd_indicator.GetCol()
        self._lower_label = a_df.columns[self.__macd_indicator.GetLowHigh()[0]]
        self._upper_label = a_df.columns[self.__macd_indicator.GetLowHigh()[1]]
        self._data = a_df[self.__macd_indicator.GetCol()].to_frame()
        self._data[self._lower_label] = a_df[self._lower_label]
        self._data[self._upper_label] = a_df[self._upper_label]
        self._buy_label = self.__macd_indicator.GetLabel() + self._buy_label
        self._sell_label = self.__macd_indicator.GetLabel() + self._sell_label
        buyNsellTuple = self._buyNsell()
        self._data[self._buy_label] = buyNsellTuple[0]
        self._data[self._sell_label] = buyNsellTuple[1]
        print('DATA', self._data.describe())

    def _buyNsell(self):
        buySignal = []
        sellSignal = []
        flag = -1

        for i in range(len(self._data)):
            if self._data[self._lower_label][i] > self._data[self._upper_label][i]:
                sellSignal.append(np.nan)
                if flag != 1:
                    buySignal.append(self._data[self._col][i])
                    flag = 1
                else:
                    buySignal.append(np.nan)
            elif self._data[self._lower_label][i] < self._data[self._upper_label][i]:
                buySignal.append(np.nan)
                if flag != 0:
                    sellSignal.append(self._data[self._col][i])
                    flag = 0
                else:
                    sellSignal.append(np.nan)
            else:
                buySignal.append(np.nan)
                sellSignal.append(np.nan)

        return buySignal, sellSignal

    def Plot(self) -> plt:
        self.__macd_indicator.PlotData().show()
        plt.figure(figsize=self.__macd_indicator.GetFigSize())
        plt.style.use(self.__macd_indicator.GetPlotStyle())
        for a_ind, col in enumerate(self._data.columns[0:1]):
            an_alpha: float = 1.0 if a_ind == 0 else 0.3
            self._data[col].plot(alpha=an_alpha)
            print('i', an_alpha)
        plt.scatter(self.__macd_indicator.GetData().index, self._data[self._buy_label], label=self._buy_label, marker='^', color='green')
        plt.scatter(self.__macd_indicator.GetData().index, self._data[self._sell_label], label=self._sell_label, marker='v', color='red')
        plt.title(self.__macd_indicator.GetMainLabel())
        plt.xlabel(self.__macd_indicator.GetXLabel())
        plt.xticks(rotation=self.__macd_indicator.GetXticksAngle())
        plt.ylabel(self.__macd_indicator.GetYLabel())
        plt.legend(loc=self.__macd_indicator.GetLegendPlace())
        return plt

    def PlotAll(self) -> plt:
        n_col: int = 1
        n_row: int = 2
        a_title: str = self.__macd_indicator.GetMainLabel()
        x_title: str = self.__macd_indicator.GetXLabel()
        y_title: str = self.__macd_indicator.GetYLabel()
        f_size: Tuple[float, float] = (self.__macd_indicator.GetFigSize()[0], self.__macd_indicator.GetFigSize()[0])
        fig, ax = plt.subplots(n_row, n_col, figsize=f_size, sharex=True)
        plt.style.use(self.__macd_indicator.GetPlotStyle())
        #ax0 strategy
        for a_ind, col in enumerate(self._data.columns[0:1]):
            an_alpha: float = 1.0 if a_ind == 0 else 0.3
            ax[0].plot(self._data[col], alpha=an_alpha, label=col)
        ax[0].scatter(self.__macd_indicator.GetData().index, self._data[self._buy_label], marker='^', color='green', label=self._buy_label)
        ax[0].scatter(self.__macd_indicator.GetData().index, self._data[self._sell_label], marker='v', color='red', label=self._sell_label)
        ax[0].set(ylabel=y_title, title=a_title)
        ax[0].legend(loc=self.__macd_indicator.GetLegendPlace())
        #ax1 index
        for a_ind, col in enumerate(self.__macd_indicator.GetData().columns[-2:self.__macd_indicator.GetData().columns.size]):
            an_alpha: float = 0.5 if a_ind != 0 else 1.0
            ax[1].plot(self.__macd_indicator.GetData()[col], alpha=an_alpha, label=col)
        ax[1].xaxis.set_tick_params(rotation=self.__macd_indicator.GetXticksAngle())
        ax[1].set(ylabel='Index', xlabel=x_title)
        ax[1].legend(loc=self.__macd_indicator.GetLegendPlace())
        return plt
