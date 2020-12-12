import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pandas import DataFrame
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class SmaIndicator(AbstractTechIndicator):
    _data: DataFrame = DataFrame()

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._name = 'SMA'
        self._label += self._name
        self._main_label += ' ' + self._label
        self._setData(y_stock_option.DataFrame)

    def GetData(self) -> DataFrame:
        return self._data

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

    def _setData(self, a_df: DataFrame):
        d_f: DataFrame = a_df.copy()
        self._data[self._col] = d_f[self._col]
        self._data[self._name + '005'] = self.__getSma(d_f, 5)
        self._data[self._name + '009'] = self.__getSma(d_f, 9)
        self._data[self._name + '010'] = self.__getSma(d_f, 10)
        self._data[self._name + '020'] = self.__getSma(d_f, 20)
        self._data[self._name + '030'] = self.__getSma(d_f, 30)
        self._data[self._name + '050'] = self.__getSma(d_f, 50)
        self._data[self._name + '100'] = self.__getSma(d_f, 100)
        self._data[self._name + '200'] = self.__getSma(d_f, 200)
        self._low_high = (5, 7)

    def __getSma(self, a_df: DataFrame, a_int: int = 12):
        d_f: DataFrame = a_df.copy()
        # return last column as .iloc[:,-1] spaning rollng mean
        return a_df[self._col].rolling(window=a_int, min_periods=0).mean()
