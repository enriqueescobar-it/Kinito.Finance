from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine
import requests
import yahoo_fin.stock_info as si

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
    price_to_book = market_cap / book_value_equity_now
    print('price_to_book', price_to_book)
    print(BS)


def getPricetoEarnings(stock):
    IS = requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{stock}")
    IS = IS.json()
    print(IS)
    earnings = float(IS['financials'][0]['Net Income'])
    company_info = requests.get(f"https://financialmodelingprep.com/api/v3/company/profile/{stock}")
    company_info = company_info.json()
    market_cap = float(company_info['profile']['mktCap'])
    PtoEarnings = market_cap / earnings
    # p2e[stock] = PtoEarnings
    # return p2e
    return PtoEarnings


def getPricetoSaless(stock):
    try:
        # annual income statement since we need anual sales
        IS = requests.get(f'https://fmpcloud.io/api/v3/income-statement/{stock}?apikey={api_key}')
        IS = IS.json()
        Revenue = IS[0]['revenue']
        grossprofitratip = IS[0]['grossProfitRatio']
        # most recent market capitliazation
        MarketCapit = requests.get(f'https://fmpcloud.io/api/v3/market-capitalization/{stock}?apikey={api_key}')
        MarketCapit = MarketCapit.json()
        MarketCapit = MarketCapit[0]['marketCap']
        # Price to sales
        p_to_sales = MarketCapit / Revenue
        pricetosales = {}
        pricetosales['revenue'] = Revenue
        pricetosales['Gross_Profit_ratio'] = grossprofitratip
        pricetosales['price_to_sales'] = p_to_sales
        pricetosales['Market_Capit'] = MarketCapit
    except:
        pass


tech_stocks = ['AAPL', 'MSFT', 'INTC', 'ATD-B.TO']
bank_stocks = ['WFC', 'BAC', 'C']
cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
commodity_futures = ['GC=F', 'SI=F', 'CL=F']
etf_stocks = ['VOO', 'VOOG', 'GINN.TO', 'VGRO.TO', 'XIT.TO']
mutual_funds = ['PRLAX', 'QASGX', 'HISFX']
us_treasuries = ['^TNX', '^IRX', '^TYX']
a_ticker: str = 'MSFT'
# getpricetobook(a_ticker)
# getPricetoEarnings(a_ticker)
quote = si.get_quote_table(a_ticker)
print(quote["PE Ratio (TTM)"])
val = si.get_stats_valuation(a_ticker)
val = val.iloc[:, :2]
val.columns = ["Attribute", "Recent"]
print(float(val[val.Attribute.str.contains("Trailing P/E")].iloc[0, 1]))
abstractEngine: YahooFinanceEngine = YahooFinanceEngine(a_ticker)
print(abstractEngine)
print(abstractEngine.StockType)
