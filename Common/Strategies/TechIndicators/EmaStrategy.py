import pandas as pd
import numpy as np

from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.EmaIndicator import EmaIndicator


class EmaStrategy(AbstractTechIndicatorStrategy):
    _DataFrame: pd.DataFrame
    _BuyLabel: str
    _SellLabel: str
    __LowerLabel: str
    __MediumLabel: str
    __UpperLabel: str
    __ticker: str

    def __init__(self, ema_indicator: EmaIndicator, y_stockOption: YahooStockOption):
        self._Col = ema_indicator._Col
        self._Label = ema_indicator._Label
        self._DataFrame = pd.DataFrame()
        self._BuyLabel = 'Buy_' + self._Label
        self._SellLabel = 'Sell_' + self._Label
        self.__LowerLabel = ema_indicator._Label + '05'
        self.__MediumLabel = ema_indicator._Label + '21'
        self.__UpperLabel = ema_indicator._Label + '63'
        self.__ticker = y_stockOption.Ticker
        self._DataFrame[y_stockOption.Ticker] = y_stockOption.HistoricalData[self._Col]
        self._DataFrame[self.__LowerLabel] = ema_indicator._EMA005
        self._DataFrame[self.__MediumLabel] = ema_indicator._EMA021
        self._DataFrame[self.__UpperLabel] = ema_indicator._EMA063
        buyNsellTuple = self.__buyNsell()
        self._DataFrame[self._BuyLabel] = buyNsellTuple[0]
        self._DataFrame[self._SellLabel] = buyNsellTuple[1]
        print(self._DataFrame)

    def __buyNsell(self):
        buySignal = []
        sellSignal = []
        flagLong = False
        flagShort = False

        for i in range(len(self._DataFrame)):
            if self._DataFrame[self.__MediumLabel][i] < self._DataFrame[self.__UpperLabel][i] and self._DataFrame[self.__LowerLabel][i] < self._DataFrame[self.__MediumLabel][i] and flagLong == False:
                buySignal.append(self._DataFrame[self.__ticker][i])
                sellSignal.append(np.nan)
                flagShort = True
            elif flagShort == True and self._DataFrame[self.__LowerLabel][i] > self._DataFrame[self.__MediumLabel][i]:
                buySignal.append(np.nan)
                sellSignal.append(self._DataFrame[self.__ticker][i])
                flagShort = False
            elif self._DataFrame[self.__MediumLabel][i] > self._DataFrame[self.__UpperLabel][i] and self._DataFrame[self.__LowerLabel][i] > self._DataFrame[self.__MediumLabel][i] and flagLong == False:
                buySignal.append(self._DataFrame[self.__ticker][i])
                sellSignal.append(np.nan)
                flagLong = True
            elif flagLong == True and self._DataFrame[self.__LowerLabel][i] < self._DataFrame[self.__MediumLabel][i]:
                buySignal.append(np.nan)
                sellSignal.append(self._DataFrame[self.__ticker][i])
                flagLong = False
            else:
                buySignal.append(np.nan)
                sellSignal.append(np.nan)

        return buySignal, sellSignal
