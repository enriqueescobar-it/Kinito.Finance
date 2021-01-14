from abc import *
from Common.StockType.AbstractStock import AbstractStock


class AbstractCurrency(AbstractStock):

    def __init__(self):
        self.__class = 'Currency'

    def __str__(self):
        return self.__class
