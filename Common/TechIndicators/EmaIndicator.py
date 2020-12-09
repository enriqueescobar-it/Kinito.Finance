import matplotlib.pyplot as plt
import matplotlib.cm as cm

from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class EmaIndicator(AbstractTechIndicator):

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._name = 'EMA'
        self._label += self._name
        self._main_label += ' ' + self._label
        self._setData(y_stock_option)

    def __getEma(self, y_stock_option: YahooStockOption, a_int: int = 21):
        # return last column as .iloc[:,-1] spaning ewm mean
        return y_stock_option.DataFrame[self._col].ewm(span=a_int, adjust=False).mean()

    def _setData(self, y_stock_option: YahooStockOption):
        self._data[self._col] = y_stock_option.DataFrame[self._col]
        self._data[self._name + '005'] = self.__getEma(y_stock_option, 5)
        self._data[self._name + '010'] = self.__getEma(y_stock_option, 10)
        self._data[self._name + '020'] = self.__getEma(y_stock_option, 20)
        self._data[self._name + '021'] = self.__getEma(y_stock_option, 21)
        self._data[self._name + '050'] = self.__getEma(y_stock_option, 50)
        self._data[self._name + '063'] = self.__getEma(y_stock_option, 63)
        self._data[self._name + '100'] = self.__getEma(y_stock_option, 100)
        self._data[self._name + '200'] = self.__getEma(y_stock_option, 200)
        self._low_high = (1, 4, 6)
        print(self._data.tail())

    def PlotData(self) -> plt:
        plt.figure(figsize=self._fig_size)
        plt.style.use(self._plot_style)
        colors = cm.coolwarm
        for a_ind, col in enumerate(self._data.columns):
            an_alpha: float = 1.0 if (a_ind == 0 or a_ind in self._low_high) else 0.3
            self._data[col].plot(alpha=an_alpha)
            print('i', an_alpha)
        plt.title(self._main_label)
        plt.xlabel(self._x_label)
        plt.xticks(rotation=self._x_ticks_angle)
        plt.ylabel(self._y_label)
        plt.legend(loc=self._legend_place)
        plt.grid(True)
        return plt
