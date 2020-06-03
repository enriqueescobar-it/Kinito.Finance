from Common.Measures.Time.TimeSpan import TimeSpan
from Common.Readers.Engine.PandaEngine import PandaEngine
from Common.StockOptions.AbstractStockOption import AbstractStockOption
import pandas as pd
import matplotlib.pyplot as plt


class YahooStockOption(AbstractStockOption):
    Ticker: str
    HistoricalData: pd.DataFrame

    def __init__(self, a_ticker: str = 'CNI'):
        self._timeSpan = TimeSpan()
        self.Source = 'yahoo'
        self.Ticker = a_ticker
        self._GetData()
        #self._DrawData()

    def _GetData(self):
        self.HistoricalData = PandaEngine(self.Source, self._timeSpan, self.Ticker).DataFrame

    def _DrawData(self):
        '''
        fig, ax = plt.subplots()
        fig.set_size_inches(3, 1.5)
        plt.savefig(file.jpeg, edgecolor='black', dpi=400, facecolor='black', transparent=True)
        '''
        # visualize data
        draw_col: str = "Adj Close"
        legend_place: str = 'upper left'
        plt.style.use('fivethirtyeight')
        # self._monthCount
        plt.figure(figsize=(1920 / 200, 1080 / 200))
        # Plot the grid lines
        plt.plot(self.HistoricalData[draw_col], label=self.Ticker)
        plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
        plt.title(self.Ticker + ' ' + draw_col + ' History ' + str(self._timeSpan.MonthCount) + ' mts')
        plt.xlabel(self._timeSpan.StartDateStr + ' - ' + self._timeSpan.EndDateStr)
        plt.ylabel(draw_col + ' in $USD')
        plt.legend(loc=legend_place)
        plt.show()
