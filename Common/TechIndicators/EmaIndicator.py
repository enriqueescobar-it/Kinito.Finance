import pandas as pd
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class EmaIndicator(AbstractTechIndicator):
    _EMA005: pd.core.series.Series
    _EMA010: pd.core.series.Series
    _EMA020: pd.core.series.Series
    _EMA021: pd.core.series.Series
    _EMA050: pd.core.series.Series
    _EMA063: pd.core.series.Series
    _EMA100: pd.core.series.Series
    _EMA200: pd.core.series.Series
    _Df: pd.DataFrame

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._label += 'EMA'
        self._EMA005 = self.__getEma(y_stock_option, 5)
        self._EMA010 = self.__getEma(y_stock_option, 10)
        self._EMA020 = self.__getEma(y_stock_option, 20)
        self._EMA021 = self.__getEma(y_stock_option, 21)
        self._EMA050 = self.__getEma(y_stock_option, 50)
        self._EMA063 = self.__getEma(y_stock_option, 63)
        self._EMA100 = self.__getEma(y_stock_option, 100)
        self._EMA200 = self.__getEma(y_stock_option, 200)

    def __getEma(self, y_stock_option: YahooStockOption, a_int: int = 21):
        # return last column as .iloc[:,-1] spaning ewm mean
        return y_stock_option.HistoricalData[self._col].ewm(span=a_int, adjust=False).mean()
