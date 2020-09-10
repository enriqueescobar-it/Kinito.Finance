from abc import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from Common.Strategies.AbstractStrategy import AbstractStrategy


class AbstractTechIndicatorStrategy(AbstractStrategy):
    _buy_label: str = 'Buy'
    _sell_label: str = 'Sell'
    _col: str
    _lower_label: str = ''
    _middle_label: str = ''
    _upper_label: str = ''
    _data: DataFrame

    @abstractmethod
    def _buyNsell(self):
        pass

    @abstractmethod
    def Plot(self) -> plt:
        pass

    @abstractmethod
    def PlotAll(self) -> plt:
        pass
