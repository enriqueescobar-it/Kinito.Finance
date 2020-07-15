import pandas as pd
import numpy as np

from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.SmaIndicator import SmaIndicator


class SmaStrategy(AbstractTechIndicatorStrategy):
    _DataFrame: pd.DataFrame
    _BuyLabel: str
    _SellLabel: str
    __ticker: str

    def __init__(self, sma_indicator: SmaIndicator, y_stockOption: YahooStockOption):
        self._Col = sma_indicator._Col
        self._Label = sma_indicator._Label
        self._DataFrame = pd.DataFrame()
        self._BuyLabel = 'Buy_' + self._Label
        self._SellLabel = 'Sell_' + self._Label
        self.__ticker = y_stockOption.Ticker
        self._DataFrame[y_stockOption.Ticker] = y_stockOption.HistoricalData[self._Col]
        self._DataFrame[sma_indicator._Label + '005'] = sma_indicator._SMA005
        self._DataFrame[sma_indicator._Label + '009'] = sma_indicator._SMA009
        self._DataFrame[sma_indicator._Label + '010'] = sma_indicator._SMA010
        self._DataFrame[sma_indicator._Label + '020'] = sma_indicator._SMA020
        self.__SMA20label = sma_indicator._Label + '020'
        self._DataFrame[sma_indicator._Label + '050'] = sma_indicator._SMA050
        self.__SMA50label = sma_indicator._Label + '050'
        self._DataFrame[sma_indicator._Label + '100'] = sma_indicator._SMA100
        self._DataFrame[sma_indicator._Label + '200'] = sma_indicator._SMA200
        buyNsellTuple = self.__buyNsell()
        self._DataFrame[self._BuyLabel] = buyNsellTuple[0]
        self._DataFrame[self._SellLabel] = buyNsellTuple[1]
        print(self._DataFrame)

    def __buyNsell(self):
        buySignal = []
        sellSignal = []
        flag = -1

        for i in range(len(self._DataFrame)):
            if self._DataFrame[self.__SMA20label][i] > self._DataFrame[self.__SMA50label][i]:#
                if flag != 1:
                    buySignal.append(self._DataFrame[self.__ticker][i])
                    sellSignal.append(np.nan)
                    flag = 1
                else:
                    buySignal.append(np.nan)
                    sellSignal.append(np.nan)
            elif self._DataFrame[self.__SMA20label][i] < self._DataFrame[self.__SMA50label][i]:#
                if flag != 0:
                    buySignal.append(np.nan)
                    sellSignal.append(self._DataFrame[self.__ticker][i])
                    flag = 0
                else:
                    buySignal.append(np.nan)
                    sellSignal.append(np.nan)
            else:
                buySignal.append(np.nan)
                sellSignal.append(np.nan)

        return buySignal, sellSignal
