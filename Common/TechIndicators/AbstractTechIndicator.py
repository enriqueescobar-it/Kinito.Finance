import math
from abc import *
from typing import Tuple
from pandas import DataFrame
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy


class AbstractTechIndicator(ABC):
    _col: str
    _label: str = 'Indicator'
    _name: str
    _src: str == 'yahoo'
    _legend_place: str = 'upper left'
    #['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
    _plot_style: str = 'seaborn'
    _x_ticks_angle: int = 45
    _data: DataFrame = DataFrame()
    _strategy: AbstractTechIndicatorStrategy
    _fig_size: Tuple[float, float]
    _low_high: Tuple[int, int]
    _main_label: str
    _x_label: str
    _y_label: str

    def __init__(self, y_stock_option: YahooStockOption):
        self._src = y_stock_option.Source
        self._col = 'Adj Close' if self._src == 'yahoo' else 'Close'
        self._fig_size = (3 * math.log(y_stock_option.TimeSpan.MonthCount), 4.5)
        self._main_label = "{1} ({0}) {2} History {3} months".format(y_stock_option.Source,
                                                                    y_stock_option.Ticker,
                                                                    self._col,
                                                                    str(y_stock_option.TimeSpan.MonthCount))
        self._x_label = y_stock_option.TimeSpan.StartDateStr + ' - ' + y_stock_option.TimeSpan.EndDateStr
        self._y_label = self._col + ' in USD'

    @abstractmethod
    def _setData(self, y_stock_option: YahooStockOption):
        pass

    def GetCol(self) -> str:
        return self._col

    def GetLowHigh(self) -> Tuple[int, int]:
        return self._low_high

    def GetLabel(self) -> str:
        return self._label

    def GetMainLabel(self) -> str:
        return self._main_label

    def GetName(self) -> str:
        return self._name

    def GetSource(self) -> str:
        return self._src

    def GetData(self) -> DataFrame:
        return self._data
