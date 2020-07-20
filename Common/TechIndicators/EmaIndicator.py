import pandas as pd
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class EmaIndicator(AbstractTechIndicator):
    _EMA05: pd.core.series.Series
    _EMA21: pd.core.series.Series
    _EMA63: pd.core.series.Series

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._Label = 'EMA'
        self._EMA05 = self.__getEma(y_stock_option, 5)
        self._EMA21 = self.__getEma(y_stock_option, 21)
        self._EMA63 = self.__getEma(y_stock_option, 63)

    def __getEma(self, y_stock_option: YahooStockOption, a_int: int = 21):
        # return last column as .iloc[:,-1] spaning ewm mean
        return y_stock_option.HistoricalData[self._Col].ewm(span=a_int, adjust=False).mean()
