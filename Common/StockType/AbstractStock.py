from abc import *


class AbstractStock(ABC):
    __class: str = 'NA'

    def __init__(self):
        self.__class = 'Stock'

    def __str__(self):
        return self.__class
