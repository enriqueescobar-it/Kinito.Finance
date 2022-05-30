from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Options.AbstractStockOption import AbstractStockOption

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'aStockOption', '   ============\n')
aStockOption: AbstractStockOption = AbstractStockOption('a cy', 'APT', 'A_QUOTE')
print(aStockOption.to_json())
print(aStockOption)

print('\n============   ', 'a_StockOption', '   ============\n')
a_StockOption: AbstractStockOption = AbstractStockOption('une cie', 'OPT', 'UN_QUOTE')
print(a_StockOption.to_json())
print(a_StockOption)
