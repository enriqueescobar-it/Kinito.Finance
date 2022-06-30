from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture


class GoldAug22Future(AbstractStockFuture):

    def __init__(self, source: str = 'yahoo', ticker: str = "GC=F") -> None:
        ticker_name: str = "GC=F" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'Gold Aug 22' if source == 'yahoo' else ticker
        a_to_usd: float = 1.0
        #super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'Future')
