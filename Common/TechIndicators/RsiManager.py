import pandas as pd
import matplotlib.pyplot as plt

from Common.TechIndicators.AbstractIndicatorManager import AbstractIndicatorManager


class RsiManager(AbstractIndicatorManager):
    _RsiLabel: str
    __col: str
    __period: int
    __src: str

    def __init__(self, a_df: pd.DataFrame, src: str = 'yahoo'):
        self.__src = src
        self.__col = 'Adj Close' if src == 'yahoo' else 'Close'
        self.__delta = a_df[self.__col].diff(1)
        self.__setPeriod(14)
        self._RsiLabel = 'RSI'
        self.__setUp()
        self.__setDown()
        self.__setRsi()

    def __setUp(self):
        up = self.__delta.copy()
        up[up < 0] = 0
        self.__up = up
        self.__setAvgGain()

    def __setDown(self):
        down = self.__delta.copy()
        down[down > 0] = 0
        self.__down = down
        self.__setAvgLoss()

    def __setPeriod(self, a_int: int):
        self.__period = a_int

    def __setAvgGain(self):
        self.__avgGain = self.__up.rolling(window=self.__period).mean()

    def __setAvgLoss(self):
        self.__avgLoss = abs(self.__down.rolling(window=self.__period).mean())

    def __setRsi(self):
        self.__rs = self.__avgGain / self.__avgLoss
        self.__rsi = 100.0 - (100.0 / (1.0 + self.__rs))

    def getVizualization(self):
        pass
        '''plt.figure(figsize=(num_months/2, 4.5))
        plt.plot(AAPL.index, RSI, label = RSIlabel, alpha = 0.7)
        plt.axhline(10, linestyle='--', label = '10%', alpha = 0.50, color='gray')
        plt.axhline(20, linestyle='--', label = '20%', alpha = 0.50, color='orange')
        plt.axhline(30, linestyle='--', label = '30%', alpha = 0.50, color='green')
        plt.axhline(40, linestyle='--', label = '40%', alpha = 0.50, color='red')
        plt.axhline(60, linestyle='--', label = '60%', alpha = 0.50, color='red')
        plt.axhline(70, linestyle='--', label = '70%', alpha = 0.50, color='green')
        plt.axhline(80, linestyle='--', label = '80%', alpha = 0.50, color='orange')
        plt.axhline(90, linestyle='--', label = '90%', alpha = 0.50, color='gray')
        plt.title(RSIlabel + ' ' + dfCol + ' History ' + str(num_months) + ' mts')
        plt.xlabel(start_date_s + ' - ' + end_date_s)
        plt.xticks(rotation=45)
        plt.ylabel(dfCol + ' in $USD')
        plt.legend(loc = legend_place)
        plt.show()'''
