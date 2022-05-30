from Common.InfoType.stock_info import stock_info
from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'equityStock', '   ============\n')
equityStock: AbstractStockEquity = AbstractStockEquity('a cy', 'AAPL', 'A_QUOTE')
print(equityStock.to_json())
print(equityStock)

print('\n============   ', 'equityStock', '   ============\n')
eStock: AbstractStockEquity = AbstractStockEquity('a company', 'CNI', 'UN_QUOTE')
print(eStock.to_json())
print(eStock)
