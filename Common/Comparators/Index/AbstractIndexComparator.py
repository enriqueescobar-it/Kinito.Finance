from abc import abstractmethod

from Common.Comparators.AbstractComparator import AbstractComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
import pandas as pd


class AbstractIndexComparator(AbstractComparator):
    __stockOption: YahooStockOption
    __indexList: list
    Data: pd.DataFrame
    DataNormalized: pd.DataFrame
    DataNormalizedL1: pd.DataFrame
    DataSparsed: pd.DataFrame
    DataScaled: pd.DataFrame
    DataSimpleReturns: pd.DataFrame
    DataSimpleReturnsCorr: pd.DataFrame
    DataLogReturns: pd.DataFrame
