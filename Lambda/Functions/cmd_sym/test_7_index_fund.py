from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.Index.IndexFund import IndexFund

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund)
print(abstractStockFund.to_json())
print(abstractStockFund.SectorDataFrame)
print(abstractStockFund.HoldingDataFrame)
print('yoyo')
i_0: IndexFund = IndexFund('an index', 'VFX', 'UN_QUOTE')
print(i_0)
print(i_0.to_json())
print(i_0.SectorDataFrame)
print(i_0.HoldingDataFrame)
print('yaya')
i_1: IndexFund = IndexFund('un index', 'TNX', 'UNE_QUOTE')
print(i_1)
print(i_1.to_json())
print(i_1.SectorDataFrame)
print(i_1.HoldingDataFrame)
print('yeye')
