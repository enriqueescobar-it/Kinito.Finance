from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.EmaIndicator import EmaIndicator


class EmaStrategy(AbstractTechIndicatorStrategy):
    _ema_indicator: EmaIndicator

    def __init__(self, ema_indicator: EmaIndicator):
        self._ema_indicator = ema_indicator
        a_df: pd.DataFrame = self._ema_indicator.DataFrame
        self._col = self._ema_indicator.Column
        self._lower_label = a_df.columns[self._ema_indicator.GetLowHigh()[0]]
        self._middle_label = a_df.columns[self._ema_indicator.GetLowHigh()[1]]
        self._upper_label = a_df.columns[self._ema_indicator.GetLowHigh()[2]]
        self._data = a_df[self._ema_indicator.Column].to_frame()
        self._data[self._lower_label] = a_df[self._lower_label]
        self._data[self._middle_label] = a_df[self._middle_label]
        self._data[self._upper_label] = a_df[self._upper_label]
        self._buy_label = self._ema_indicator.Label + self._buy_label
        self._sell_label = self._ema_indicator.Label + self._sell_label
        buyNsellTuple = self._buyNsell()
        self._data[self._buy_label] = buyNsellTuple[0]
        self._data[self._sell_label] = buyNsellTuple[1]
        print('DATA', self._data.describe())

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
        self._ema_indicator.PlotData().show()
        plt.figure(figsize=self._ema_indicator.GetFigSize())
        plt.style.use(self._ema_indicator.FigStyle)
        for a_ind, col in enumerate(self._data.columns[0:4]):
            an_alpha: float = 1.0 if a_ind == 0 else 0.3
            self._data[col].plot(alpha=an_alpha)
            print('i', an_alpha)
        plt.scatter(self._ema_indicator.DataFrame.index, self._data[self._buy_label], label=self._buy_label, marker='^', color='green')
        plt.scatter(self._ema_indicator.DataFrame.index, self._data[self._sell_label], label=self._sell_label, marker='v', color='red')
        plt.title(self._ema_indicator.LabelMain)
        plt.xlabel(self._ema_indicator.LabelX)
        plt.xticks(rotation=self._ema_indicator.LabelXangle)
        plt.ylabel(self._ema_indicator.LabelY)
        plt.legend(loc=self._ema_indicator.LegendPlace)
        return plt

    def PlotAll(self) -> plt:
        n_col: int = 1
        n_row: int = 2
        a_title: str = self._ema_indicator.LabelMain
        x_title: str = self._ema_indicator.LabelX
        y_title: str = self._ema_indicator.LabelY
        f_size: Tuple[float, float] = (self._ema_indicator.GetFigSize()[0], self._ema_indicator.GetFigSize()[0])
        fig, ax = plt.subplots(n_row, n_col, figsize=f_size, sharex=True)
        plt.style.use(self._ema_indicator.FigStyle)
        #ax0 strategy
        for a_ind, col in enumerate(self._data.columns[0:1]):
            an_alpha: float = 1.0 if a_ind == 0 else 0.3
            ax[0].plot(self._data[col], alpha=an_alpha, label=col)
        ax[0].scatter(self._ema_indicator.DataFrame.index, self._data[self._buy_label], marker='^', color='green', label=self._buy_label)
        ax[0].scatter(self._ema_indicator.DataFrame.index, self._data[self._sell_label], marker='v', color='red', label=self._sell_label)
        ax[0].set(ylabel=y_title, title=a_title)
        ax[0].legend(loc=self._ema_indicator.LegendPlace)
        #ax1 strategy
        for a_ind, col in enumerate(self._ema_indicator.DataFrame.columns[-2:self._ema_indicator.DataFrame.columns.size]):
            an_alpha: float = 0.5 if a_ind != 0 else 1.0
            ax[1].plot(self._ema_indicator.DataFrame[col], alpha=an_alpha, label=col)
        ax[1].xaxis.set_tick_params(rotation=self._ema_indicator.LabelXangle)
        ax[1].set(ylabel='Index', xlabel=x_title)
        ax[1].legend(loc=self._ema_indicator.LegendPlace)
        return plt
