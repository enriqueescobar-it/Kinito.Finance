from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Mutual.MutualFund import MutualFund

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund')
print(abstractStockFund)
print(abstractStockFund.to_json())

mf_0: MutualFund = MutualFund('a mutual', 'QASGX')
print(mf_0)
print(mf_0.to_json())

mf_1: MutualFund = MutualFund('un mutual', 'HISFX')
print(mf_1)
print(mf_1.to_json())
