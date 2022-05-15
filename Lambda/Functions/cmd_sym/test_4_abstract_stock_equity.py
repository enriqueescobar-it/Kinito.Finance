from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

equityStock: AbstractStockEquity = AbstractStockEquity('a cy', 'AAPL', 'A_QUOTE')
print(equityStock)
print(equityStock.to_json())


eStock: AbstractStockEquity = AbstractStockEquity('a company', 'CNI', 'UN_QUOTE')
print(eStock)
print(eStock.to_json())
