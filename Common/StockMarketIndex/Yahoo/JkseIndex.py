from pyarrow.lib import null
from Common.Measures.Time.TimeSpan import TimeSpan
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex


class JkseIndex(AbstractStockMarketIndex):

    def __init__(self, source: str = 'yahoo', ticker: str = "^JKSE", tm_spn: TimeSpan = null):
        a_ticker: str = "^JKSE" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        a_name: str = 'JakartaCompo' if source == 'yahoo' else ticker
        a_to_usd: float = 14680.00
        super().__init__(source, a_name, a_column, a_ticker, tm_spn, a_to_usd)
