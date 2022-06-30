from Common.StockType.Funds.Index.IndexFund import IndexFund


class Nasdaq100Index(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^NDX") -> None:
        ticker_name: str = "^NDX" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'NASDAQ 100' if source == 'yahoo' else ticker
        a_to_usd: float = 1.00
        # super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
