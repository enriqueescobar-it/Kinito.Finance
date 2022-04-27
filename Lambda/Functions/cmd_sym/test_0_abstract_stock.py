from Common.StockType.AbstractStock import AbstractStock

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

aStock: AbstractStock = AbstractStock()
print(aStock)
print(aStock.to_json())
