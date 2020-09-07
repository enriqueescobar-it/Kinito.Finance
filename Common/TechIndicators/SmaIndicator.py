import matplotlib.pyplot as plt
import matplotlib.cm as cm

from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class SmaIndicator(AbstractTechIndicator):

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._name = 'SMA'
        self._label += self._name
        self._main_label += ' ' + self._label
        self._setData(y_stock_option)

    def __getSma(self, y_stock_option: YahooStockOption, a_int: int = 12):
        # return last column as .iloc[:,-1] spaning rollng mean
        return y_stock_option.HistoricalData[self._col].rolling(window=a_int, min_periods=0).mean()

    def _setData(self, y_stock_option: YahooStockOption):
        self._data[self._col] = y_stock_option.HistoricalData[self._col]
        self._data[self._name + '005'] = self.__getSma(y_stock_option, 5)
        self._data[self._name + '009'] = self.__getSma(y_stock_option, 9)
        self._data[self._name + '010'] = self.__getSma(y_stock_option, 10)
        self._data[self._name + '020'] = self.__getSma(y_stock_option, 20)
        self._data[self._name + '030'] = self.__getSma(y_stock_option, 30)
        self._data[self._name + '050'] = self.__getSma(y_stock_option, 50)
        self._data[self._name + '100'] = self.__getSma(y_stock_option, 100)
        self._data[self._name + '200'] = self.__getSma(y_stock_option, 200)
        print(self._data.tail())

    def PlotData(self) -> plt:
        plt.figure(figsize=self._fig_size)
        plt.style.use(self._plot_style)
        colors = cm.coolwarm
        for a_ind, col in enumerate(self._data.columns):
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
