from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Mutual.MutualFund import MutualFund

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractStockFund', '   ============\n')
abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund.to_json())
print(abstractStockFund)

print('\n============   ', 'mf_0', '   ============\n')
mf_0: MutualFund = MutualFund('a mutual', 'QASGX', 'UN_QUOTE')
print(mf_0.to_json())
print(mf_0)

print('\n============   ', 'mf_1', '   ============\n')
mf_1: MutualFund = MutualFund('un mutual', 'HISFX', 'UNE_QUOTE')
print(mf_1.to_json())
print(mf_1)
