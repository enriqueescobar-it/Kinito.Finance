from abc import *
from pandas import DataFrame


class AbstractStockOption(ABC):
    Source: str = ''
    Data: DataFrame
