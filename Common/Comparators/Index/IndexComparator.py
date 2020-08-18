from Common.Comparators.Index.AbstractIndexComparator import AbstractIndexComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
import pandas as pd
import matplotlib.pyplot as plt


class IndexComparator(AbstractIndexComparator):
    __stockOption: YahooStockOption
    __indexList: list
    DataComparator: pd.DataFrame
    DataNorma: pd.DataFrame

    def __init__(self, stock_option: YahooStockOption, indices: list()):
        self.__stockOption = stock_option
        self.__indexList = indices
        self.DataComparator = stock_option.HistoricalData[stock_option.SourceColumn].to_frame()
        self.DataComparator.columns = stock_option.Ticker + self.DataComparator.columns
        df: pd.DataFrame = indices[0].HistoricalData
        for a_index in indices[1:]:
            df = df.merge(a_index.HistoricalData, left_index=True, right_index=True)
        self.DataComparator = self.DataComparator.merge(df, left_index=True, right_index=True)
        self.DataNorma = (self.DataComparator - self.DataComparator.min()) / (
                    self.DataComparator.max() - self.DataComparator.min())
        print(self.DataNorma.head())
        plt.figure(figsize=(stock_option.TimeSpan.MonthCount/2, 4.5))
        for c in self.DataNorma.columns.values:
          plt.plot(self.DataNorma.index, self.DataNorma[c], lw= 2, label = c)

        #plt.title('_'.join(stockSymbols) + ' Cumulative Returns ' + str(num_months) + ' mts')
        #plt.xlabel(start_date_s + ' - ' + end_date_s)
        plt.ylabel('Growth per dollar invested')
        #plt.legend(loc = legend_place, fontsize = 10)
        plt.show()
