from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency


class BitcoinUSDCrypto(CryptoCurrency):

    def __init__(self, source: str = 'yahoo', ticker: str = "BTC-USD") -> None:
        ticker_name: str = "BTC-USD" if source == 'yahoo' else ticker
        a_column: str = 'Adj Close' if source == 'yahoo' else ticker
        company_name: str = 'Bitcoin USD' if source == 'yahoo' else ticker
        a_to_usd: float = 1.0
        #super().__init__(source, company_name, a_column, ticker_name, a_to_usd)
        super().__init__(company_name, ticker_name, 'CryptoCurrency')
