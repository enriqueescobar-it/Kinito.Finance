from abc import *
from Common.StockType.AbstractStock import AbstractStock


class AbstractStockFund(AbstractStock):

    def __init__(self):
        self.__class = 'Fund'

    def __str__(self):
        return self.__class
