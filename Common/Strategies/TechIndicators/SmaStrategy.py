import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Common.Plotters.Strategies.AbstractStrategyPlotter import AbstractStrategyPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.TechIndicators.SmaIndicator import SmaIndicator


class SmaStrategy(AbstractTechIndicatorStrategy, AbstractStrategyPlotter):
    __sma_indicator: SmaIndicator

    def __init__(self, sma_indicator: SmaIndicator, y_stock_option: YahooStockOption):
        self.__sma_indicator = sma_indicator
        a_df: pd.DataFrame = self.__sma_indicator.GetData()
        self._col = self.__sma_indicator.GetCol()
        self._lower_label = a_df.columns[self.__sma_indicator.GetLowHigh()[0]]
        self._upper_label = a_df.columns[self.__sma_indicator.GetLowHigh()[1]]
        self._data = a_df[self.__sma_indicator.GetCol()].to_frame()
        self._data[self._lower_label] = a_df[self._lower_label]
        self._data[self._upper_label] = a_df[self._upper_label]
        self._buy_label += self.__sma_indicator.GetLabel()
        self._sell_label += self.__sma_indicator.GetLabel()
        buyNsellTuple = self._buyNsell()
        self._data[self._buy_label] = buyNsellTuple[0]
        self._data[self._sell_label] = buyNsellTuple[1]
        print('DATA', self._data.describe())
        self.__SOURCE = y_stock_option.Source
        self.__TICKER_LABEL = y_stock_option.Source + y_stock_option.Ticker + "_" + self._col
        self.__DATE_TIME_INDEX = y_stock_option.HistoricalData.index
        self.__STRATEGY_LABEL = self.__sma_indicator.GetLabel()
        self.__STRATEGY_LABEL_BUY = self._buy_label
        self.__STRATEGY_DATA_BUY = self._data[self._buy_label]
        self.__STRATEGY_LABEL_SELL = self._sell_label
        self.__STRATEGY_DATA_SELL = self._data[self._sell_label]

    def _buyNsell(self):
        buySignal = []
        sellSignal = []
        flag = -1

        for i in range(len(self._data)):
            if self._data[self._lower_label][i] > self._data[self._upper_label][i]:#
                if flag != 1:
                    buySignal.append(self._data[self._col][i])
                    sellSignal.append(np.nan)
                    flag = 1
                else:
                    buySignal.append(np.nan)
                    sellSignal.append(np.nan)
            elif self._data[self._lower_label][i] < self._data[self._upper_label][i]:#
                if flag != 0:
                    buySignal.append(np.nan)
                    sellSignal.append(self._data[self._col][i])
                    flag = 0
                else:
                    buySignal.append(np.nan)
                    sellSignal.append(np.nan)
            else:
                buySignal.append(np.nan)
                sellSignal.append(np.nan)

        return buySignal, sellSignal

    def Plot(self):
        plt.figure(figsize=self.__sma_indicator.GetFigSize())
        plt.style.use(self.__sma_indicator.GetPlotStyle())
        plt.plot(self._data[self._col], label=self.__TICKER_LABEL, alpha=0.7)
        '''
        plt.plot(self._data[self.__STRATEGY_LABEL + '005'], label=self.__STRATEGY_LABEL + '005', alpha=0.50, color='lightblue')
        plt.plot(self._data[self.__STRATEGY_LABEL + '009'], label=self.__STRATEGY_LABEL + '009', alpha=0.50, color='lightgray')
        plt.plot(self._data[self.__STRATEGY_LABEL + '010'], label=self.__STRATEGY_LABEL + '010', alpha=0.50, color='green')
        plt.plot(self._data[self.__STRATEGY_LABEL + '020'], label=self.__STRATEGY_LABEL + '020', alpha=0.50, color='orange')
        plt.plot(self._data[self.__STRATEGY_LABEL + '030'], label=self.__STRATEGY_LABEL + '030', alpha=0.50, color='violet')
        plt.plot(self._data[self.__STRATEGY_LABEL + '050'], label=self.__STRATEGY_LABEL + '050', alpha=0.50, color='pink')
        plt.plot(self._data[self.__STRATEGY_LABEL + '100'], label=self.__STRATEGY_LABEL + '100', alpha=0.50, color='red')
        plt.plot(self._data[self.__STRATEGY_LABEL + '200'], label=self.__STRATEGY_LABEL + '200', alpha=0.50, color='yellow')
        '''
        plt.scatter(self.__DATE_TIME_INDEX, self.__STRATEGY_DATA_BUY, label=self.__STRATEGY_LABEL_BUY, marker='^', color='green')
        plt.scatter(self.__DATE_TIME_INDEX, self.__STRATEGY_DATA_SELL, label=self.__STRATEGY_LABEL_SELL, marker='v', color='red')
        plt.title(self.__sma_indicator.GetMainLabel())
        plt.xlabel(self.__sma_indicator.GetXLabel())
        plt.xticks(rotation=self.__sma_indicator.GetXticksAngle())
        plt.ylabel(self.__sma_indicator.GetYLabel())
        plt.legend(loc=self.__sma_indicator.GetLegendPlace())
        return plt
