from abc import *
from Common.StockType.AbstractStock import AbstractStock


class AbstractStockBond(AbstractStock):

    def __init__(self):
        self.__class = 'Bond'

    def __str__(self):
        return self.__class
