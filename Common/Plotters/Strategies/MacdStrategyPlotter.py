from Common.Plotters.Strategies.AbstractStrategyPlotter import AbstractStrategyPlotter
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy


class MacdStrategyPlotter(AbstractStrategyPlotter):
    __macdStrategy: MacdStrategy

    def __init__(self, macd_strategy: MacdStrategy):
        self.__macdStrategy = macd_strategy

