from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.RsiIndicator import RsiIndicator


class RsiStrategy(AbstractTechIndicatorStrategy):
    _rsi_indicator: RsiIndicator
    _summary: pd.DataFrame

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
        print(self._data.head(3))
        self._setSummary()

    @property
    def Summary(self):
        return self._summary

    def PlotAx(self, ax: object) -> object:
        an_alpha: float = 1.0
        ax.plot(self._data[self._col], alpha=an_alpha, label=self._col)
        ax.scatter(self._rsi_indicator.GetData().index, self._data['Buy'], marker='^', color='green', label=self._buy_label)
        ax.scatter(self._rsi_indicator.GetData().index, self._data['Sell'], marker='v', color='red', label=self._sell_label)
        return ax

    def Plot(self) -> plt:
        plt.tight_layout()
        return plt

    def PlotAll(self) -> plt:
        n_col: int = 1
        n_row: int = 3
        an_alpha: float = 1.0
        a_title: str = self._rsi_indicator.LabelMain
        x_title: str = self._rsi_indicator.LabelX
        y_title: str = self._rsi_indicator.LabelY
        f_size: Tuple[float, float] = (self._rsi_indicator.FigSizeTuple[0], self._rsi_indicator.FigSizeTuple[0])
        fig, ax = plt.subplots(n_row, n_col, figsize=f_size, sharex=True)
        plt.style.use(self._rsi_indicator.FigStyle)
        # ax0 strategy
        ax[0].plot(self._data[self._col], alpha=an_alpha, label=self._col)
        ax[0].scatter(self._rsi_indicator.GetData().index, self._data['Buy'], marker='^', color='green', label=self._buy_label)
        ax[0].scatter(self._rsi_indicator.GetData().index, self._data['Sell'], marker='v', color='red', label=self._sell_label)
        ax[0].set(ylabel=y_title, title=a_title)
        ax[0].legend(loc=self._rsi_indicator.LegendPlace)
        # ax1 index
        ax[1] = self._rsi_indicator.PlotAx(ax[1])
        ax[1].scatter(self._rsi_indicator.GetData().index, self._data['BuyRSI'], marker='^', color='green', label=self._buy_label)
        ax[1].scatter(self._rsi_indicator.GetData().index, self._data['SellRSI'], marker='v', color='red', label=self._sell_label)
        ax[1].set(ylabel='Index')
        ax[1].legend(loc=self._rsi_indicator.LegendPlace)
        # ax2
        ax[2].plot(self._summary, alpha=an_alpha)
        ax[2].legend(loc=self._rsi_indicator.LegendPlace)
        ax[2].xaxis.set_tick_params(rotation=self._rsi_indicator.LabelXangle)
        ax[2].set(ylabel='Buy & Sell', xlabel=x_title)
        plt.tight_layout()
        return plt

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
        self._data['LongTomorrow'] = np.nan
        self._data['Buy'] = np.nan
        self._data['Sell'] = np.nan
        self._data['BuyRSI'] = np.nan
        self._data['SellRSI'] = np.nan
        self._data['BuyAndSell'] = np.nan
        self._data = self.__setBuyNsell(self._data)
        self._setSummary()
        print(self._data.BuyAndSell)
        print(self._summary.BuyAndSell)

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

    def __setBuyNsell(self, a_df: pd.DataFrame) -> pd.DataFrame:
        for x in range(15, len(a_df)):
            # long tomorrow
            if (a_df['RSI'][x] <= 40) & (a_df['RSI'][x - 1] > 40):
                a_df['LongTomorrow'][x] = True
            elif (a_df['LongTomorrow'][x - 1] == True) & (a_df['RSI'][x] <= 70):
                a_df['LongTomorrow'][x] = True
            else:
                a_df['LongTomorrow'][x] = False
            # buy
            if (a_df['LongTomorrow'][x] == True) & (a_df['LongTomorrow'][x - 1] == False):
                a_df['Buy'][x] = a_df[self._col][x]
                a_df['BuyRSI'][x] = a_df['RSI'][x]
            # sell
            if (a_df['LongTomorrow'][x] == False) & (a_df['LongTomorrow'][x - 1] == True):
                a_df['Sell'][x] = a_df[self._col][x]
                a_df['SellRSI'][x] = a_df['RSI'][x]
        a_df['BuyAndSell'][15] = a_df[self._col][15]
        for x in range(16, len(a_df)):
            if a_df['LongTomorrow'][x - 1] == True:
                a_df['BuyAndSell'][x] = a_df['BuyAndSell'][x - 1] * (a_df[self._col][x] / a_df[self._col][x - 1])
            else:
                a_df['BuyAndSell'][x] = a_df['BuyAndSell'][x - 1]
        return a_df

    def _setSummary(self):
        self._summary = pd.DataFrame(index=self._data.index)
        self._summary['Buy'] = self._data['Buy'].replace(np.nan, 0)
        self._summary['Buy'][self._summary['Buy'] > 0] = 1
        self._summary['Sell'] = self._data['Sell'].replace(np.nan, 0)
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
                self._summary['BuyAndSell'][ind] = last_float
