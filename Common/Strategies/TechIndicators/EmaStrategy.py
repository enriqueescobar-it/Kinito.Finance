import pandas as pd
import numpy as np

from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.EmaIndicator import EmaIndicator


class EmaStrategy(AbstractTechIndicatorStrategy):
    _DataFrame: pd.DataFrame
    _BuyLabel: str
    _SellLabel: str
    __LowerLabel: str
    __UpperLabel: str
    __ticker: str

    def __init__(self, ema_indicator: EmaIndicator, y_stockOption: YahooStockOption):
        self._Col = ema_indicator._Col
        self._Label = ema_indicator._Label
        self._DataFrame = pd.DataFrame()
        self._BuyLabel = 'Buy_' + self._Label
        self._SellLabel = 'Sell_' + self._Label
        self.__LowerLabel = ema_indicator._Label + '030'
        self.__UpperLabel = ema_indicator._Label + '100'
        self.__ticker = y_stockOption.Ticker
