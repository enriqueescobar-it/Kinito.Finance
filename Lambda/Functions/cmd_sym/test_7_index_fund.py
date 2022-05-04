from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Index.IndexFund import IndexFund

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund')
print(abstractStockFund)
print(abstractStockFund.to_json())

i_0: IndexFund = IndexFund('an index', 'VFX')
print(i_0)
print(i_0.to_json())

i_1: IndexFund = IndexFund('an index', 'TNX')
print(i_1)
print(i_1.to_json())
