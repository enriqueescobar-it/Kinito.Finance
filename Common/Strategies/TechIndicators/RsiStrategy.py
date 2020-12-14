from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.RsiIndicator import RsiIndicator


class RsiStrategy(AbstractTechIndicatorStrategy):
    _rsi_indicator: RsiIndicator

    def __init__(self, rsi_indicator: RsiIndicator):
        pass
        self._setSummary()

    @property
    def Summary(self):
        return self._summary

    def PlotAx(self, ax: object) -> object:
        return ax

    def Plot(self) -> plt:
        pass

    def _setSummary(self):
        self._summary = pd.DataFrame(index=self._data.index)
        self._summary['Buy'] = self._data[self._buy_label].replace(np.nan, 0)
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
                self._summary['BuyAndSell'][ind] = last_float
