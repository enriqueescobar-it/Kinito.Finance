from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Options.AbstractStockOption import AbstractStockOption

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

aStockOption: AbstractStockOption = AbstractStockOption('a cy', 'APT')
print(aStockOption)
print(aStockOption.to_json())

a_StockOption: AbstractStockOption = AbstractStockOption('une cie', 'OPT')
print(a_StockOption)
print(a_StockOption.to_json())