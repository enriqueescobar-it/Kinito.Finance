from pandas import DataFrame

from Common.Markets.AbstractMarket import AbstractMarket


class AbstractMarketIndex(AbstractMarket):
    _column: str = ''
    _name: str = ''
    _source: str = ''
    _ticker: str = ''
    _toUsd: float = -1.1
    _data: DataFrame = DataFrame()
    _data_norm: DataFrame = DataFrame()
    _data_scaled: DataFrame = DataFrame()
