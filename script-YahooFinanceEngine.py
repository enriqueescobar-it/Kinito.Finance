from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine


tech_stocks = ['AAPL', 'MSFT', 'INTC', 'ATD-B.TO']
bank_stocks = ['WFC', 'BAC', 'C']
etf_stocks = ['VOO', 'VOOG', 'GINN.TO', 'VGRO.TO']
commodity_futures = ['GC=F', 'SI=F', 'CL=F']
cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
mutual_funds = ['PRLAX', 'QASGX', 'HISFX']
us_treasuries = ['^TNX', '^IRX', '^TYX']
a_ticker: str = 'GINN'
abstractEngine: YahooFinanceEngine = YahooFinanceEngine(a_ticker)
print(abstractEngine)
print(abstractEngine.StockType)
