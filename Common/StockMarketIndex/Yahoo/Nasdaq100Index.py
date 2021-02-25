from Common.Measures.Time.TimeSpan import TimeSpan
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from pyarrow.lib import null


class Nasdaq100Index(AbstractStockMarketIndex):

    def __init__(self, source: str = 'yahoo', ticker: str = "^NDX", tm_spn: TimeSpan = null):
        a_ticker: str = "^NDX" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        a_name: str = 'Nasdaq100' if source == 'yahoo' else ticker
        a_to_usd: float = 1.00
        super().__init__(source, a_name, a_column, a_ticker, tm_spn, a_to_usd)
