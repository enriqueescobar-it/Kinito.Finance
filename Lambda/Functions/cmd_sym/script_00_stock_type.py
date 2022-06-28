import argparse

from Common.InfoType.QuarterInfo import QuarterInfo
from Common.InfoType.YahooFinanceStockInfo import YahooFinanceStockInfo
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund
from Common.StockType.Funds.Index.IndexFund import IndexFund
from Common.StockType.Funds.Mutual.MutualFund import MutualFund
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture
from Common.StockType.Options.AbstractStockOption import AbstractStockOption


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required=True, help="symbol name case sensitive")
ap.add_argument("-q", "--quote", required=True, help="quote type name case sensitive")
args = vars(ap.parse_args())
a_sym: str = args["symbol"]
a_quote: str = args["quote"]
# display a friendly message to the user
print("Hi there, you are looking for the <{}> symbol with <{}> quote?".format(a_sym, a_quote))
qi: QuarterInfo = QuarterInfo()
print(qi)
exit(69)
abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())
'''
aStockBond: AbstractStockOption = AbstractStockOption('a cy', a_sym)
print(aStockBond)
print(aStockBond.to_json())

equityStock: AbstractStockEquity = AbstractStockEquity('a cy', a_sym)
print(equityStock)
print(equityStock.to_json())

futureStock: AbstractStockFuture = AbstractStockFuture('una cia', a_sym)
print(futureStock)
print(futureStock.to_json())

aCurrency: AbstractCurrency = AbstractCurrency('una cia')#, a_sym)
print(aCurrency)
print(aCurrency.to_json())
'''
abstractStockFund: AbstractStockFund = AbstractStockFund('una cia', a_quote)
print(abstractStockFund)
print(abstractStockFund.to_json())
'''
mutualFund: MutualFund = MutualFund('una cia', a_sym)
print(mutualFund)
print(mutualFund.to_json())

etFund: ExchangeTradedFund = ExchangeTradedFund('una cia', a_sym)
print(etFund)
print(etFund.to_json())
'''
indexFund: IndexFund = IndexFund('una cia', a_sym, a_quote)
print(indexFund)
print(indexFund.to_json())
