from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Index.IndexFund import IndexFund

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractStockFund', '   ============\n')
abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund.to_json())
print(abstractStockFund)

print('\n============   ', 'i_0', '   ============\n')
i_0: IndexFund = IndexFund('an index', 'VFX', 'UN_QUOTE')
print(i_0.to_json())
print(i_0)

print('\n============   ', 'i_1', '   ============\n')
i_1: IndexFund = IndexFund('un index', 'TNX', 'UNE_QUOTE')
print(i_1.to_json())
print(i_1)
