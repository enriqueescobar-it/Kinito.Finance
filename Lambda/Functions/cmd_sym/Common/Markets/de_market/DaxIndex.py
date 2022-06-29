from Common.StockType.Funds.Index.IndexFund import IndexFund


class DaxIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^GDAXI") -> None:
        a_ticker: str = "^GDAXI" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        a_name: str = 'DeutscherAktien' if source == 'yahoo' else ticker
        a_to_usd: float = 1.15
        #super().__init__(source, a_name, a_column, a_ticker, a_to_usd)
        super().__init__(a_name, a_ticker, 'IndexFund')
