from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
import numpy as np
from pandas import DataFrame


class IndexFund(AbstractStockFund):
    __ticker: str = 'NA'
    _sector_df: DataFrame = DataFrame()
    _holding_df: DataFrame = DataFrame()
    _stock_part_count: int = -1
    _bond_part_count: int = -1
    _price_to_earn: float = np.nan
    _price_to_book: float = np.nan
    _price_to_sale: float = np.nan
    _price_to_cash: float = np.nan

    def __init__(self, c_name: str):
        super().__init__(c_name.replace(' ', ''))
        self.__class = 'Index'
