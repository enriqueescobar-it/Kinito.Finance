import matplotlib.pyplot as plt
import matplotlib.cm as cm

from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class MacdIndicator(AbstractTechIndicator):

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._name = 'MACD'
        self._label += self._name
        self._main_label += ' ' + self._label
        self._setData(y_stock_option)

    def __getEMA(self, y_stock_option: YahooStockOption, a_int: int = 12):
        return y_stock_option.HistoricalData[self._col].ewm(span=a_int, adjust=False).mean()

    def _setData(self, y_stock_option: YahooStockOption):
        self._data[self._col] = y_stock_option.HistoricalData[self._col]
        shortEma = self.__getEMA(y_stock_option, 12)
        self._data['EMA12'] = shortEma
        longEma = self.__getEMA(y_stock_option, 26)
        self._data['EMA26'] = longEma
        macd = shortEma - longEma
        self._data[self._name] = macd
        self._data['SignalLine'] = macd.ewm(span=9, adjust=False).mean()
        self._low_high = (3, 4)

    def PlotData(self) -> plt:
        plt.figure(figsize=self._fig_size)
        plt.style.use(self._plot_style)
        colors = cm.coolwarm
        for a_ind, col in enumerate(self._data.columns[-2:self._data.columns.size]):
            an_alpha: float = 0.5 if a_ind != 0 else 1.0
            self._data[col].plot(alpha=an_alpha)
            print('i', a_ind)
        plt.title(self._main_label)
        plt.xlabel(self._x_label)
        plt.xticks(rotation=self._x_ticks_angle)
        plt.ylabel(self._y_label)
        plt.legend(loc=self._legend_place)
        plt.grid(True)
        return plt
