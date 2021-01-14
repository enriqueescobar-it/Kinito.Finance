from abc import *
from Common.StockType.AbstractStock import AbstractStock


class AbstractStockOption(AbstractStock):

    def __init__(self):
        self.__class = 'Option'

    def __str__(self):
        return self.__class
