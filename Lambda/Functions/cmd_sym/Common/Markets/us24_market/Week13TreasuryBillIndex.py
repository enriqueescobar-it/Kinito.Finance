from Common.StockType.Funds.Index.IndexFund import IndexFund


class Week13TreasuryBillIndex(IndexFund):

    def __init__(self, source: str = 'yahoo', ticker: str = "^IRX") -> None:
        ticker_name: str = "^IRX" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = '13 WEEK TREASURY BILL' if source == 'yahoo' else ticker
        a_to_usd: float = 1.00
        # super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'IndexFund')
