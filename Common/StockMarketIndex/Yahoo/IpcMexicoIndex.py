from Common.Measures.Time.TimeSpan import TimeSpan
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from pyarrow.lib import null


class IpcMexicoIndex(AbstractStockMarketIndex):

    def __init__(self, source: str = 'yahoo', ticker: str = "^MXX", tm_spn: TimeSpan = null):
        a_ticker: str = "^MXX" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        a_name: str = 'IpcMexico' if source == 'yahoo' else ticker
        a_to_usd: float = 0.05
        super().__init__(source, a_name, a_column, a_ticker, tm_spn, a_to_usd)
