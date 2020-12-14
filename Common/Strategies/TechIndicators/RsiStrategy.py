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

    def PlotAx(self, ax: object) -> object:
        return ax

    def Plot(self) -> plt:
        pass
