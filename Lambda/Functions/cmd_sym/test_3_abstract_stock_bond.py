from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Bonds.AbstractStockBond import AbstractStockBond

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractStockBond', '   ============\n')
abstractStockBond: AbstractStockBond = AbstractStockBond('a company', 'BOND', 'A_QUOTE')
print(abstractStockBond.to_json())
print(abstractStockBond)

print('\n============   ', 'aStockBond', '   ============\n')
aStockBond: AbstractStockBond = AbstractStockBond('une compagnie', 'BAND', 'UN_QUOTE')
print(aStockBond.to_json())
print(aStockBond)
