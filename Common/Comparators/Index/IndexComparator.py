from sklearn.preprocessing import MinMaxScaler
from Common.Comparators.Index.AbstractIndexComparator import AbstractIndexComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import math


class IndexComparator(AbstractIndexComparator):
    __corr_series: pd.Series = pd.Series()
    __corr_idx_df: pd.DataFrame = pd.DataFrame()
    __corr_idx_list: list = list()

    def __init__(self, stock_option: YahooStockOption, indices: list()):
        self._stock_option = stock_option
        self._index_list = indices
        self._legend_place = 'upper left'
        self.Data = self._setData()
        self.DataNormalized = self._setNormalizer(self.Data)
        self.DataNormalizedL1 = self._setNormalizerL1(self.Data)
        self.DataSparsed = self._setSparser(self.Data)
        self.DataScaled = self._setScaler(self.Data)
        self.DataSimpleReturns = self._setSimpleReturns(self.Data)
        self.DataSimpleReturnsCorr = self._setSimpleReturnsCorr(self.Data)
        self.__corr_series = self.__getBestCorrelations()
        self.__corr_idx_df = self.__getBestMultiIndex()
        self.__corr_idx_list = self.__getBestMultiList()
        self.DataLogReturns = self._setLogReturns(self.Data)
        self._plotHeatMap(self.DataSimpleReturnsCorr)
        self._plotComparison(2, 3)
        # self._plotCompared(self.Data, 'Flat', 'Price in USD')
        # self._plotCompared(self.DataNormalized, 'Normalized', 'Base 1 variation since' + stock_option.TimeSpan.StartDateStr)
        # self._plotCompared(self.DataNormalizedL1, 'NormalizedL1', 'Base 1 variation since' + stock_option.TimeSpan.StartDateStr)
        # self._plotCompared(self.DataSparsed, 'Sparsed', 'Sparse variation since' + stock_option.TimeSpan.StartDateStr)
        # self._plotCompared(self.DataScaled, 'Scaled', 'Range [0-100] scaled since' + stock_option.TimeSpan.StartDateStr)

    def _setData(self) -> pd.DataFrame:
        df: pd.DataFrame = self._stock_option.DataFrame[self._stock_option.Column].to_frame()
        df.columns = self._stock_option.Ticker + df.columns
        a_df: pd.DataFrame = self._index_list[0].Data
        for a_index in self._index_list[1:]:
            a_df = a_df.merge(a_index.Data, left_index=True, right_index=True)
        return df.merge(a_df, left_index=True, right_index=True)

    def _setNormalizer(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return a_df / a_df.iloc[0]

    def _setNormalizerL1(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return pd.DataFrame(preprocessing.normalize(a_df, norm='l1'), columns=a_df.columns, index=a_df.index)

    def _setBinarizer(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return pd.DataFrame(preprocessing.Binarizer(threshold=1.4).transform(a_df), columns=a_df.columns,
                            index=a_df.index)

    def _setSparser(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        return pd.DataFrame(preprocessing.scale(a_df), columns=a_df.columns, index=a_df.index)

    def _setScaler(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        # scale to compare array from 0.0 to 100.0
        minMaxScaler: MinMaxScaler = preprocessing.MinMaxScaler(feature_range=(0.0, 100.0))
        # scale to compare data frame
        stockArrayScaled: np.ndarray = minMaxScaler.fit_transform(a_df)
        return pd.DataFrame(stockArrayScaled, columns=a_df.columns, index=a_df.index)

    def _setSimpleReturns(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        # return a_df.pct_change().to_frame()
        return a_df.pct_change(1)

    def _setLogReturns(self, a_df: pd.DataFrame = pd.DataFrame()) -> pd.DataFrame:
        a_var = np.log(a_df / a_df.shift(1))
        return a_var  # .to_frame()

    def _setSimpleReturnsCorr(self, df: pd.DataFrame):
        return self._setSimpleReturns(df).corr()

    def _plotHeatMap(self, df: pd.DataFrame):
        # plt.figure(figsize=(1.75 * math.log(self.__stockOption.TimeSpan.MonthCount), 1.75 * math.log(self.__stockOption.TimeSpan.MonthCount)))
        sns.clustermap(df, cmap="coolwarm", col_cluster=False)  # annot=False, row_cluster=True,
        plt.rcParams['date.epoch'] = '0000-12-31'
        plt.style.use('fivethirtyeight')
        plt.show()

    def _plotComparison(self, nb_col=1, nb_row=1):
        a_int: int = len(self.__corr_idx_list)
        a_float: float = 3 * math.log(self._stock_option.TimeSpan.MonthCount)
        fig, ax = plt.subplots(nb_row, nb_col, figsize=(a_float, a_float / 2.5), sharex=False, sharey=False)
        plt.rcParams['date.epoch'] = '0000-12-31'
        # plt.style.use('fivethirtyeight')
        plt.style.use('seaborn')
        # plt.style.use('classic')
        # ax00
        self.Data[self.__corr_idx_list].plot(ax=ax[0, 0], legend=None, color=sns.color_palette(n_colors=a_int))
        plt.setp(ax[0, 0].get_xticklabels(), visible=False)
        ax[0, 0].set(ylabel='Price ($)', xlabel='')
        ax[0, 0].legend(loc=self._legend_place, fontsize=7)
        # ax01
        sns.boxplot(data=self.Data[self.__corr_idx_list], width=.5, ax=ax[0, 1]).set(xlabel='')
        ax[0, 1].set(xticklabels=[])
        # ax10
        self.DataNormalized[self.__corr_idx_list].plot(ax=ax[1, 0], legend=None, color=sns.color_palette(n_colors=a_int))
        plt.setp(ax[1, 0].get_xticklabels(), visible=False)
        ax[1, 0].set(ylabel='Normalized', xlabel='')
        ax[1, 0].legend(loc=self._legend_place, fontsize=7)
        # ax11
        sns.boxplot(data=self.DataNormalized[self.__corr_idx_list], width=.5, ax=ax[1, 1])
        ax[1, 1].set(xticklabels=[])
        ## ax20 -> dev null
        # self.DataNormalizedL1.plot(ax=ax[2, 0], legend=None)
        # plt.setp(ax[2, 0].get_xticklabels(), visible=False)
        # ax[2, 0].set(ylabel='L1 variation', xlabel='')
        ## ax21 -> dev null
        # sns.boxplot(data=self.DataNormalizedL1, width=.5, ax=ax[2, 1])
        ## ax30 -> dev null
        # self.DataSparsed.plot(ax=ax[3, 0], legend=None)
        # plt.setp(ax[3, 0].get_xticklabels(), visible=False)
        # ax[3, 0].set(ylabel='Sparse variation', xlabel='')
        ## ax31 -> dev null
        # sns.boxplot(data=self.DataSparsed, width=.5, ax=ax[3, 1])
        # ax40 -> 30 -> 20
        self.DataScaled[self.__corr_idx_list].plot(ax=ax[2, 0], legend=None, color=sns.color_palette(n_colors=a_int))
        ax[2, 0].set(ylabel='100 Sparse', xlabel='') #ax[2, 0].set_xticklabels([]) #ax[2, 0].set_xlabel(None)
        ax[2, 0].legend(loc=self._legend_place, fontsize=7)
        # ax41 -> 31 -> 21
        sns.boxplot(data=self.DataScaled[self.__corr_idx_list], width=.5, ax=ax[2, 1])
        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.show()

    def _plotCompared(self, df: pd.DataFrame, a_title: str = '', y_title: str = ''):
        fig_plot = plt.figure(figsize=(3 * math.log(self._stock_option.TimeSpan.MonthCount), 7))
        grid_spec = gridspec.GridSpec(2, 1)
        ax1 = fig_plot.add_subplot(grid_spec[0, 0])
        for c in df.columns.values:
            plt.plot(df.index, df[c], lw=2, label=c)
        # ax1.set_xlabel('Since ' + self.__stockOption.TimeSpan.StartDateStr)
        ax1.set_ylabel(y_title)
        ax1.set_title(self._stock_option.Column + ' ' + a_title + ':Since ' + self._stock_option.TimeSpan.StartDateStr)
        ax1.legend(loc='upper left', fontsize=(len(self._index_list) * 0.26))
        ax2 = fig_plot.add_subplot(grid_spec[1, 0])
        ax2 = sns.boxplot(data=df, width=.5)  # fliersize=20, whis=.2, , linewidth=2.5
        ax2.set_title('Stock ' + self._stock_option.Column + ' ' + a_title)
        # ax2.set_xlabel('Stock tickers')
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=30)
        # plt.xticks(rotation=45)
        ax2.set_ylabel(y_title)
        plt.tight_layout()
        plt.show()
        # plt.figure(figsize=(3 * math.log(self.__stockOption.TimeSpan.MonthCount), 3.5))
        # self.__summaryPlot(df, a_title, y_title)
        # plt.show()
        # plt.figure(figsize=(3 * math.log(self.__stockOption.TimeSpan.MonthCount), 3.5))
        # self.__snsBoxPlot(df, a_title, y_title)
        # plt.show()

    def _snsBoxPlot(self, df: pd.DataFrame, a_title: str = '', y_title: str = ''):
        sns.boxplot(data=df, width=.5)  # fliersize=20, whis=.2, , linewidth=2.5
        plt.title('Stock ' + self._stock_option.Column + ' ' + a_title)
        plt.xlabel('Stock tickers')
        plt.xticks(rotation=45)
        plt.ylabel(y_title)

    def _summaryPlot(self, df: pd.DataFrame, a_title: str = '', y_title: str = ''):
        for c in df.columns.values:
            plt.plot(df.index, df[c], lw=2, label=c)
        plt.title(
            self._stock_option.Column + ' ' + a_title + ' ' + str(self._stock_option.TimeSpan.MonthCount) + ' months')
        plt.xlabel(self._stock_option.TimeSpan.StartDateStr + ' - ' + self._stock_option.TimeSpan.EndDateStr)
        plt.ylabel(y_title)
        plt.legend(loc='upper left', fontsize=10)

    def __getBestCorrelations(self) -> pd.Series:
        #self.DataSimpleReturnsCorr.abs().where
        #self.DataSimpleReturnsCorr.abs().shape
        return (self.DataSimpleReturnsCorr.where(
                np.triu(np.ones(self.DataSimpleReturnsCorr.shape), k=1).astype(np.bool))
               .stack()
               .sort_values(ascending=False).drop_duplicates())

    def __getBestMultiIndex(self) -> pd.DataFrame:
        a_df: pd.DataFrame = self.__corr_series.index.to_frame().reset_index(drop=True, inplace=False)
        return a_df[a_df[0].str.contains(self._stock_option.Ticker)].head(6)

    def __getBestMultiList(self) -> list:
        a_list: list = pd.DataFrame.drop_duplicates(self.__corr_idx_df[0].to_frame())[0].tolist()
        a_list.extend(self.__corr_idx_df[1].tolist())
        return a_list
