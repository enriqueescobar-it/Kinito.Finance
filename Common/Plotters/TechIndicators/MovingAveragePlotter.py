import matplotlib.pyplot as plt
from pandas import DatetimeIndex
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Plotters.TechIndicators.AbstractTechIndicatorsPlotter import AbstractTechIndicatorsPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.MovingAverageIndicator import MovingAverageIndicator


class MovingAveragePlotter(AbstractTechIndicatorsPlotter):
    __dateTimeIndex: DatetimeIndex
    _Indicator: MovingAverageIndicator
    __Label: str
    __src: str
    __ticker: str
    __timeSpan: TimeSpan

    def __init__(self, y_stock_option: YahooStockOption, ma_indicator: MovingAverageIndicator):
        self.__dateTimeIndex = y_stock_option.HistoricalData.index
        self._Indicator = ma_indicator
        self.__src = y_stock_option.Source
        self.__legendPlace = 'upper left'
        self.__ticker = y_stock_option.Ticker
        self.__timeSpan = y_stock_option.TimeSpan
        self.__Label = y_stock_option.Source + y_stock_option.Ticker + "_" + self._Indicator._Label
