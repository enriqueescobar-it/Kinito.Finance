import argparse
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity
from Common.StockType.Futures.AbstractStockFuture import AbstractStockFuture
from Common.StockType.Options.AbstractStockOption import AbstractStockOption


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required=True, help="symbol name case sensitive")
args = vars(ap.parse_args())
a_sym: str = args["symbol"]
# display a friendly message to the user
print("Hi there, you are looking for the <{}> symbol?".format(a_sym))

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractStockBond: AbstractStockBond = AbstractStockBond('a company', a_sym)
print(abstractStockBond)
print(abstractStockBond.to_json())

aStockBond: AbstractStockOption = AbstractStockOption('a cy', a_sym)
print(aStockBond)
print(aStockBond.to_json())

'''equityStock: AbstractStockEquity = AbstractStockEquity('a cy', a_sym)
print(equityStock)
print(equityStock.to_json())'''

futureStock: AbstractStockFuture = AbstractStockFuture('una cia', a_sym)
print(futureStock)
print(futureStock.to_json())

aCurrency: AbstractCurrency = AbstractCurrency('una cia')#, a_sym)
print(aCurrency)
print(aCurrency.to_json())
