from Common.Readers.Engine.YahooFinanceEngine import YahooFinanceEngine
import requests
import yahoo_fin.stock_info as si
from Common.Readers.Engine.YahooFinStockInfo import YahooFinStockInfo

api_key = '41da2fad6cc1f1221dc6b74b0a926139'


def getMarketCap(stock) -> float:
    company_info = requests.get(f"https://financialmodelingprep.com/api/v3/profile/{stock}?apikey={api_key}")
    company_info = company_info.json()
    market_capit = float(company_info[0]['mktCap'])
    print('market_cap0', market_capit)
    #market_capit = float(company_info['profile']['mktCap'])
    #print('market_cap', market_capit)
    return round(market_capit, 5)


def getPriceToBook(stock, cap: float) -> float:
    BS = requests.get(
        f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock}?period=quarter&limit=400&apikey={api_key}")
    BS = BS.json()
    book_value_equity_now = float(BS[0]['totalStockholdersEquity'])
    print('book_value_equity_now', book_value_equity_now)
    #company_info = requests.get(f"https://financialmodelingprep.com/api/v3/profile/{stock}?apikey={api_key}")
    #company_info = company_info.json()
    market_capit = cap # float(company_info[0]['mktCap'])
    #print('market_cap', market_capit)
    price_to_book = market_capit / book_value_equity_now
    print('price_to_book', price_to_book)
    print(BS)
    return round(price_to_book, 5)


def getPricetoEarnings(stock, cap: float) -> float:
    BS = requests.get(f"https://financialmodelingprep.com/api/v3/financials/income-statement/{stock}?apikey={api_key}")
    BS = BS.json()
    print(BS)
    earnings = float(BS['financials'][0]['Net Income'])
    #company_info = requests.get(f"https://financialmodelingprep.com/api/v3/company/profile/{stock}")
    #company_info = company_info.json()
    market_capit = cap #float(company_info['profile']['mktCap'])
    price_to_earn = market_capit / earnings
    # p2e[stock] = price_to_earn
    # return p2e
    print('price_to_earn', price_to_earn)
    return round(price_to_earn, 5)


def getPriceToSales(stock, cap: float) -> float:
    try:
        # annual income statement since we need anual sales
        BS = requests.get(f'https://fmpcloud.io/api/v3/income-statement/{stock}?apikey={api_key}')
        BS = BS.json()
        revenue = BS[0]['revenue']
        gross_prof_rat = BS[0]['grossProfitRatio']
        # most recent market capitliazation
        #market_capit = requests.get(f'https://fmpcloud.io/api/v3/market-capitalization/{stock}?apikey={api_key}')
        #market_capit = market_capit.json()
        market_capit = cap #market_capit[0]['marketCap']
        # Price to sales
        p_to_sales = market_capit / revenue
        pricetosales = {}
        pricetosales['revenue'] = revenue
        pricetosales['Gross_Profit_ratio'] = gross_prof_rat
        pricetosales['price_to_sales'] = p_to_sales
        print('price_to_sales', p_to_sales)
        return round(p_to_sales, 5)
    except:
        pass


us_treasuries = ['^TNX', '^IRX', '^TYX']#! #~
tech_stocks = ['AAPL', 'MSFT', 'INTC', 'ATD-B.TO']#~
bank_stocks = ['WFC', 'BAC', 'C']#~
cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']#! #~
currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']#! #~
commodity_futures = ['GC=F', 'SI=F', 'CL=F']#! #~
etf_stocks = ['VOO', 'VOOG', 'GINN.TO', 'VGRO.TO', 'XIT.TO']#!
mutual_funds = ['PRLAX', 'QASGX', 'HISFX']#!
a_ticker: str = '^TNX'#
abstractEngine: YahooFinanceEngine = YahooFinanceEngine(a_ticker)
print(abstractEngine)
print(abstractEngine.StockType)
#exit(-7)
yfsi: YahooFinStockInfo = YahooFinStockInfo(a_ticker) #PRLAX VOOG SI=F EURUSD=X BTC-USD
print(yfsi.PeRatio)
print(yfsi.FpeRatio)
print(yfsi.PegRatio)
print(yfsi.PriceToBook)
print(yfsi.PriceToEarnings)
print(yfsi.PriceToSales)
exit(-77)

market_cap: float = getMarketCap(a_ticker)
price_earn: float = getPricetoEarnings(a_ticker, market_cap)
price_book: float = getPriceToBook(a_ticker, market_cap)
price_sale: float = getPriceToSales(a_ticker, market_cap)
# quote = si.get_quote_table(a_ticker)
# print(quote["PE Ratio (TTM)"])
# val = si.get_stats_valuation(a_ticker)
# val = val.iloc[:, :2]
# val.columns = ["Attribute", "Recent"]
# print(float(val[val.Attribute.str.contains("Trailing P/E")].iloc[0, 1]))
'''
|       Name      | T.RowePriceLatinAmericaFun |
|  StockPartCount |             98             |
|  BondPartCount  |             2              |
| PriceToEarnings |           22.87            |
|   PriceToBook   |            2.47            |
|   PriceToSales  |            2.02            |
| PriceToCashflow |            8.2             |
'''
