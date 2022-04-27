from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractStockBond: AbstractStockBond = AbstractStockBond('a company', 'BOND')
print(abstractStockBond)
print(abstractStockBond.to_json())

aStockBond: AbstractStockBond = AbstractStockBond('une compagnie', 'BAND')
print(aStockBond)
print(aStockBond.to_json())
