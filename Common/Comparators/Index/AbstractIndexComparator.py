from abc import abstractmethod

from Common.Comparators.AbstractComparator import AbstractComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
import pandas as pd


class AbstractIndexComparator(AbstractComparator):
    __stockOption: YahooStockOption
    __indexList: list
    DataComparator: pd.DataFrame
    DataNormalized: pd.DataFrame
    DataScaled: pd.DataFrame
