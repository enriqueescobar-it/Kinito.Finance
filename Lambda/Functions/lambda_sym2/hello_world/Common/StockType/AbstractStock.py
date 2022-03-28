from abc import *
from prettytable import PrettyTable


class AbstractStock(ABC):
    __class: str = 'NA'
    _pretty_table: PrettyTable = PrettyTable()

    def __init__(self):
        self.__class = 'Stock'

    def __str__(self):
        return self.__class
