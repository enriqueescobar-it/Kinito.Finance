from Common.Measures.Time.TimeSpan import TimeSpan
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from pyarrow.lib import null


class ShenzhenComponentIndex(AbstractStockMarketIndex):

    def __init__(self, source: str = 'yahoo', ticker: str = "399001.SZ", tm_spn: TimeSpan = null):
        a_ticker: str = "399001.SZ" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        a_name: str = 'Shenzhen500' if source == 'yahoo' else ticker
        a_to_usd: float = 6.65
        super().__init__(source, a_name, a_column, a_ticker, tm_spn, a_to_usd)
