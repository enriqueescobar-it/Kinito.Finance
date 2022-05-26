from Common.StockType.AbstractStock import AbstractStock

abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

aStock: AbstractStock = AbstractStock()
print(aStock.to_json())
print(aStock)
