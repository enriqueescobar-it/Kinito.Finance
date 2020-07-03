import pandas as pd
from Common.TechIndicators.AbstractTechIndicator import AbstractIndicatorManager


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
