from pyarrow.lib import null
from Common.Drawers.AbstractDrawer import AbstractDrawer
import pandas as pd
from Common.Measures.Time.TimeSpan import TimeSpan
import matplotlib.pyplot as plt


class HistoricalDrawer(AbstractDrawer):

    def __init__(self, df: pd.DataFrame, src: str = 'yahoo', tick: str = 'CNI', ts: TimeSpan = null):
        if src == 'yahoo':
            self._draw_col = "Adj Close"
        super().__init__(df, src, tick, ts)
        self.__draw()

    def __draw(self):
        '''
        fig, ax = plt.subplots()
        fig.set_size_inches(3, 1.5)
        plt.savefig(file.jpeg, edgecolor='black', dpi=400, facecolor='black', transparent=True)
        '''
        # visualize data
        plt.style.use('fivethirtyeight')
        # self._monthCount
        plt.figure(figsize=(1920 / 200, 1080 / 200))
        # Plot the grid lines
        plt.plot(self._dataFrame[self._draw_col], label=self._ticker)
        plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
        plt.title(self._ticker + ' ' + self._draw_col + ' History ' + str(self._time_span.MonthCount) + ' mts')
        plt.xlabel(self._time_span.StartDateStr + ' - ' + self._time_span.EndDateStr)
        plt.ylabel(self._draw_col + ' in $USD')
        plt.legend(loc=self._legend_place)
        plt.show()
