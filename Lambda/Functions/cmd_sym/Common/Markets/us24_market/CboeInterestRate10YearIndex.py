from Common.StockType.Funds.Index.IndexFund import IndexFund


class CboeInterestRate10YearIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^TNX") -> None:
        ticker_name: str = "^TNX" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'CBOE Interest Rate 10 Year T No' if source == 'yahoo' else ticker
        a_to_usd: float = 1.0
        #super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
