from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine
import requests

api_key = '41da2fad6cc1f1221dc6b74b0a926139'


def getpricetobook(stock):
    BS = requests.get(
        f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock}?period=quarter&limit=400&apikey={api_key}")
    BS = BS.json()
    book_value_equity_now = float(BS[0]['totalStockholdersEquity'])
    print('book_value_equity_now', book_value_equity_now)
    company_info = requests.get(f"https://financialmodelingprep.com/api/v3/profile/{stock}?apikey={api_key}")
    company_info = company_info.json()
    market_cap = float(company_info[0]['mktCap'])
    print('market_cap', market_cap)
    price_to_book = market_cap/book_value_equity_now
    print('price_to_book', price_to_book)
    print(BS)

tech_stocks = ['AAPL', 'MSFT', 'INTC', 'ATD-B.TO']
bank_stocks = ['WFC', 'BAC', 'C']
cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
commodity_futures = ['GC=F', 'SI=F', 'CL=F']
etf_stocks = ['VOO', 'VOOG', 'GINN.TO', 'VGRO.TO', 'XIT.TO']
mutual_funds = ['PRLAX', 'QASGX', 'HISFX']
us_treasuries = ['^TNX', '^IRX', '^TYX']
a_ticker: str = 'WFC'
getpricetobook(a_ticker)
abstractEngine: YahooFinanceEngine = YahooFinanceEngine(a_ticker)
print(abstractEngine)
print(abstractEngine.StockType)
