import pandas as pd
import numpy as np
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.MacdIndicator import MacdIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class MacdStrategy(AbstractTechIndicatorStrategy):
    __ticker: str
    _BuyLabel: str
    _SellLabel: str
    _DataFrame: pd.DataFrame
    __macd: pd.core.series.Series

    __signal: pd.core.series.Series
    __signalLabel: str

    def __init__(self, macd_indicator: MacdIndicator, y_stockOption: YahooStockOption):
        self._Col = macd_indicator._Col
        self._DataFrame = pd.DataFrame()
        self._Label = macd_indicator._Label
        self.__macd = macd_indicator._Macd
        self.__signal = macd_indicator._SignalLine
        self.__signalLabel = macd_indicator._SignalLineLabel
        self.__ticker = y_stockOption.Ticker
        self._DataFrame[y_stockOption.Ticker] = y_stockOption.HistoricalData[self._Col]
        self._DataFrame[self._Label] = self.__macd
        self._DataFrame[self.__signalLabel] = self.__signal
        self._BuyLabel = 'Buy_' + self._Label
        self._SellLabel = 'Sell_' + self._Label
        buyNsellTuple = self.__buyNsell()
        self._DataFrame[self._BuyLabel] = buyNsellTuple[0]
        self._DataFrame[self._SellLabel] = buyNsellTuple[1]
        print(self._DataFrame.head())

    def __buyNsell(self):
        buySignal = []
        sellSignal = []
        flag = -1

        for i in range(len(self._DataFrame)):
            if self._DataFrame[self._Label][i] > self._DataFrame[self.__signalLabel][i]:
              sellSignal.append(np.nan)
              if flag != 1:
                buySignal.append(self._DataFrame[self.__ticker][i])
                flag = 1
              else:
                buySignal.append(np.nan)
            elif self._DataFrame[self._Label][i] < self._DataFrame[self.__signalLabel][i]:
              buySignal.append(np.nan)
              if flag != 0:
                sellSignal.append(self._DataFrame[self.__ticker][i])
                flag = 0
              else:
                sellSignal.append(np.nan)
            else:
              buySignal.append(np.nan)
              sellSignal.append(np.nan)
        return (buySignal, sellSignal)
