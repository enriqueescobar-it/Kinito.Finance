import argparse
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--symbol", required=True, help="symbol name case sensitive")
args = vars(ap.parse_args())
# display a friendly message to the user
print("Hi there, you are looking for the <{}> symbol?".format(args["symbol"]))

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractStockBond: AbstractStockBond = AbstractStockBond('a company', 'a ticker')
print(abstractStockBond)
print(abstractStockBond.to_json())
