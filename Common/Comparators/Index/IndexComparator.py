from Common.Comparators.Index.AbstractIndexComparator import AbstractIndexComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math


class IndexComparator(AbstractIndexComparator):
    __stockOption: YahooStockOption
    __indexList: list
    DataComparator: pd.DataFrame
    DataNorma: pd.DataFrame
    DataScaled: pd.DataFrame

    def __init__(self, stock_option: YahooStockOption, indices: list()):
        self.__stockOption = stock_option
        self.__indexList = indices
        self.DataComparator = stock_option.HistoricalData[stock_option.SourceColumn].to_frame()
        self.DataComparator.columns = stock_option.Ticker + self.DataComparator.columns
        df: pd.DataFrame = indices[0].HistoricalData
        for a_index in indices[1:]:
            df = df.merge(a_index.HistoricalData, left_index=True, right_index=True)
        self.DataComparator = self.DataComparator.merge(df, left_index=True, right_index=True)
        self.DataNorma = self.DataComparator / self.DataComparator.iloc[0]
        print(self.DataNorma.head())
        plt.figure(figsize=(3 * math.log(stock_option.TimeSpan.MonthCount), 4.5))
        for c in self.DataNorma.columns.values:
            plt.plot(self.DataNorma.index, self.DataNorma[c], lw=2, label=c)

        plt.title(stock_option.SourceColumn + ' Normalized ' + str(stock_option.TimeSpan.MonthCount) + ' months')
        plt.xlabel(stock_option.TimeSpan.StartDateStr + ' - ' + stock_option.TimeSpan.EndDateStr)
        plt.ylabel('Base 1 variation since ' + stock_option.TimeSpan.StartDateStr)
        plt.legend(loc='upper left', fontsize=10)
        plt.show()
        # scale to compare array
        minMaxScaler = preprocessing.MinMaxScaler(feature_range=(0.0, 100.0))
        stockArrayScaled = minMaxScaler.fit_transform(self.DataComparator)
        # scale to compare data frame
        self.DataScaled = pd.DataFrame(stockArrayScaled, columns=self.DataComparator.columns)
        print(self.DataScaled.tail())
        plt.figure(figsize=(3 * math.log(stock_option.TimeSpan.MonthCount), 4.5))
        for c in self.DataNorma.columns.values:
            plt.plot(self.DataScaled[c], label=c)

        plt.title(stock_option.SourceColumn + ' Scaled ' + str(stock_option.TimeSpan.MonthCount) + ' months')
        plt.xlabel(stock_option.TimeSpan.StartDateStr + ' - ' + stock_option.TimeSpan.EndDateStr)
        plt.ylabel('Base 100 scaled span since ' + stock_option.TimeSpan.StartDateStr)
        plt.legend(loc='upper left', fontsize=10)
        plt.show()
        self.DataSimpleReturnsCorr = self.DataComparator.pct_change(1).corr()
        # graph correlation
        plt.subplots(figsize=(math.log(stock_option.TimeSpan.MonthCount), math.log(stock_option.TimeSpan.MonthCount)))
        s_h_m = sns.heatmap(self.DataSimpleReturnsCorr, cmap="RdYlGn", annot= True, fmt= '.2%') #YlOrRd
        s_h_m.set_xticklabels(s_h_m.get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()
