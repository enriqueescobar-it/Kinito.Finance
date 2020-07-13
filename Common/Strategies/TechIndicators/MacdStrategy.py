import pandas as pd
import numpy as np
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.MacdIndicator import MacdIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class MacdStrategy(AbstractTechIndicatorStrategy):
    __ticker: str
    __buyLabel: str
    __sellLabel: str
    __col: str
    __dataFrame: pd.DataFrame
    __label: str
    __macd: pd.core.series.Series

    __signal: pd.core.series.Series
    __signalLabel: str

    def __init__(self, macd_indicator: MacdIndicator, y_stockOption: YahooStockOption):
        self.__col = macd_indicator._Col
        self.__dataFrame = pd.DataFrame()
        self.__label = macd_indicator._Label
        self.__macd = macd_indicator._Macd
        self.__signal = macd_indicator._SignalLine
        self.__signalLabel = macd_indicator._SignalLineLabel
        self.__ticker = y_stockOption.Ticker
        self.__dataFrame[y_stockOption.Ticker] = y_stockOption.HistoricalData[self.__col]
        self.__dataFrame[self.__label] = self.__macd
        self.__dataFrame[self.__signalLabel] = self.__signal
        self.__buyLabel = 'Buy_' + self.__label
        self.__sellLabel = 'Sell_' + self.__label
        buyNsellTuple = self.__buyNsell()
        self.__dataFrame[self.__buyLabel] = buyNsellTuple[0]
        self.__dataFrame[self.__sellLabel] = buyNsellTuple[1]
        print(self.__dataFrame.head())

    def __buyNsell(self):
        buySignal = []
        sellSignal = []
        flag = -1

        for i in range(len(self.__dataFrame)):
            if self.__dataFrame[self.__label][i] > self.__dataFrame[self.__signalLabel][i]:
              sellSignal.append(np.nan)
              if flag != 1:
                buySignal.append(self.__dataFrame[self.__ticker][i])
                flag = 1
              else:
                buySignal.append(np.nan)
            elif self.__dataFrame[self.__label][i] < self.__dataFrame[self.__signalLabel][i]:
              buySignal.append(np.nan)
              if flag != 0:
                sellSignal.append(self.__dataFrame[self.__ticker][i])
                flag = 0
              else:
                sellSignal.append(np.nan)
            else:
              buySignal.append(np.nan)
              sellSignal.append(np.nan)
        return (buySignal, sellSignal)
