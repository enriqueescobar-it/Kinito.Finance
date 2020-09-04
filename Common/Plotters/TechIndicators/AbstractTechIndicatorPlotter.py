from abc import *
from pandas import DatetimeIndex
import pandas as pd
import matplotlib.pyplot as plt
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator


class AbstractTechIndicatorPlotter(ABC):
    _legend_place: str = 'upper left'
    #['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
    _plot_style: str = 'seaborn'
    _x_ticks_angle: int = 45
    __ABSTRACT_INDICATOR: AbstractTechIndicator
    __DATE_TIME_INDEX: DatetimeIndex
    __INDICATOR_DATA_FRAME: pd.DataFrame
    __SOURCE: str
    __TICKER: str
    __TICKER_LABEL: str
    __TITLE: str
    __XLABEL: str
    __YLABEL: str

    @abstractmethod
    def PlotData(self) -> plt:
        pass

