import matplotlib.pyplot as plt
from Common.Plotters.AbstractPlotter import AbstractPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class HistoricalPlotter(AbstractPlotter):

    def __init__(self, y_stockOption: YahooStockOption):
        if y_stockOption.Source == 'yahoo':
            self.__Col = "Adj Close"
        self.__dataFrame = y_stockOption.HistoricalData
        self.__src = y_stockOption.Source
        self.__legendPlace = 'upper left'
        self.__ticker = y_stockOption.Ticker
        self.__timeSpan = y_stockOption.TimeSpan
        print('yyyy:', y_stockOption.TimeSpan.YearCount)
        print('MM:', y_stockOption.TimeSpan.MonthCount)
        print('ww:', y_stockOption.TimeSpan.WeekCount)
        print('dd:', y_stockOption.TimeSpan.DayCount)

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
        plt.figure(figsize=(self.__timeSpan.MonthCount / 2, 4.5))
        # Plot the grid lines
        plt.plot(self.__dataFrame[self.__Col], label=self.__ticker)
        #plt.hlines(y=self.__low52, xmin=self._dataFrame[self._draw_col].index, xmax=?, colors='r', linestyles='--', lw=2)
        plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
        plt.title(self.__ticker + ' ' + self.__Col + ' History ' + str(self.__timeSpan.MonthCount) + ' mts')
        plt.xlabel(self.__timeSpan.StartDateStr + ' - ' + self.__timeSpan.EndDateStr)
        plt.ylabel(self.__Col + ' in $USD')
        plt.legend(loc=self.__legendPlace)
        return plt
