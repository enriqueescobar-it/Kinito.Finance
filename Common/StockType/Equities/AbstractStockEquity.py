from abc import *
from Common.StockType.AbstractStock import AbstractStock


class AbstractStockEquity(AbstractStock):

    def __init__(self):
        self.__class = 'Equity'

    def __str__(self):
        return self.__class
