from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture


class SilverJul22Future(AbstractStockFuture):

    def __init__(self, source: str = 'yahoo', ticker: str = "SI=F") -> None:
        ticker_name: str = "SI=F" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'Silver Jul 22' if source == 'yahoo' else ticker
        a_to_usd: float = 1.0
        #super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'Future')
