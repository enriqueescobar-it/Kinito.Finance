from pandas import DataFrame
from pandas_datareader import data
from Common.Readers.Engine.AbstractPandaEngine import AbstractPandaEngine


class YahooPandaEngine(AbstractPandaEngine):
    _source: str = 'yahoo'
    _df: DataFrame = DataFrame()

    def __init__(self) -> None:
        pass
