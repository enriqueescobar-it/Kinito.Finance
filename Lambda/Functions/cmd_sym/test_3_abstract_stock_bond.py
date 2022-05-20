from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

print('\n============   ', 'abstractStockBond', '   ============\n')
abstractStockBond: AbstractStockBond = AbstractStockBond('a company', 'BOND', 'A_QUOTE')
print(abstractStockBond)
print(abstractStockBond.to_json())

print('\n============   ', 'aStockBond', '   ============\n')
aStockBond: AbstractStockBond = AbstractStockBond('une compagnie', 'BAND', 'UN_QUOTE')
print(aStockBond)
print(aStockBond.to_json())
