from pyarrow.lib import null
from Common.Plotters.AbstractPlotter import AbstractPlotter
import pandas as pd
from Common.Measures.Time.TimeSpan import TimeSpan
import matplotlib.pyplot as plt


class HistoricalPlotter(AbstractPlotter):

    def __init__(self, df: pd.DataFrame, src: str = 'yahoo', tick: str = 'CNI', ts: TimeSpan = null):
        if src == 'yahoo':
            self._draw_col = "Adj Close"
        super().__init__(df, src, tick, ts)
        print('yyyy:', ts.YearCount)
        print('MM:', ts.MonthCount)
        print('ww:', ts.WeekCount)
        print('dd:', ts.DayCount)
        print('hh:', ts.HourCount)
        # self.__draw()

    def Plot(self):
        '''
        fig, ax = plt.subplots()
        -ax.plot(x, y)
        -ax.hlines(y=0.2, xmin=4, xmax=20, linewidth=2, color='r')
        -plt.hlines(y=40, xmin=0, xmax=len(self._dataFrame[self._draw_col]), colors='r', linestyles='--', lw=2)
        fig.set_size_inches(3, 1.5)
        plt.savefig(file.jpeg, edgecolor='black', dpi=400, facecolor='black', transparent=True)
        '''
        # visualize data
        plt.style.use('fivethirtyeight')
        # self._monthCount
        plt.figure(figsize=(1920 / 200, 1080 / 200))
        # Plot the grid lines
        plt.plot(self._dataFrame[self._draw_col], label=self._ticker)
        #plt.hlines(y=self.__low52, xmin=self._dataFrame[self._draw_col].index, xmax=?, colors='r', linestyles='--', lw=2)
        plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
        plt.title(self._ticker + ' ' + self._draw_col + ' History ' + str(self._timeSpan.MonthCount) + ' mts')
        plt.xlabel(self._timeSpan.StartDateStr + ' - ' + self._timeSpan.EndDateStr)
        plt.ylabel(self._draw_col + ' in $USD')
        plt.legend(loc=self._legend_place)
        return plt
