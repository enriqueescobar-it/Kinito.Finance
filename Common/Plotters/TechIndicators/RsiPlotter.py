from Common.Measures.Time.TimeSpan import TimeSpan
from Common.TechIndicators.RsiManager import RsiManager


class RsiPlotter(globals()):

    __rsiManager: RsiManager
    __src: str
    __ticker: str
    __timeSpan: TimeSpan

    def __init__(self, rsi_manager: RsiManager, src: str = 'yahoo', tick: str = 'CNI', ts: TimeSpan = null):
        self.__rsiManager = rsi_manager
        self.__src = src
        self.__ticker = tick
        self.__timeSpan = ts
