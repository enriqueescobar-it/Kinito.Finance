import pandas as pd
import numpy as np

from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.SmaIndicator import SmaIndicator


class SmaStrategy(AbstractTechIndicatorStrategy):
    _DataFrame: pd.DataFrame
    _BuyLabel: str
    _SellLabel: str
    __ticker: str

    def __init__(self, sma_indicator: SmaIndicator, y_stockOption: YahooStockOption):
        self._Col = sma_indicator._Col
        self._Label = sma_indicator._Label
        self._DataFrame = pd.DataFrame()
        self._BuyLabel = 'Buy_' + self._Label
        self._SellLabel = 'Sell_' + self._Label
        self.__ticker = y_stockOption.Ticker
        self._DataFrame[y_stockOption.Ticker] = y_stockOption.HistoricalData[self._Col]
        buyNsellTuple = self.__buyNsell()
        self._DataFrame[self._BuyLabel] = buyNsellTuple[0]
        self._DataFrame[self._SellLabel] = buyNsellTuple[1]
        print(self._DataFrame.head())

    def __buyNsell(self):
        pass
