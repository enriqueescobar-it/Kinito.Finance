from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund

abstractStock: AbstractStock = AbstractStock()
print(abstractStock)
print(abstractStock.to_json())

abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund')
print(abstractStockFund)
print(abstractStockFund.to_json())
print(abstractStockFund.SectorDataFrame)
print(abstractStockFund.HoldingDataFrame)

etf_0: ExchangeTradedFund = ExchangeTradedFund('un etf', 'VOO')
print(etf_0)
print(etf_0.to_json())
print(etf_0.SectorDataFrame)
print(etf_0.HoldingDataFrame)

etf_1: ExchangeTradedFund = ExchangeTradedFund('un etf', 'VOOG')
print(etf_1)
print(etf_1.to_json())
print(etf_1.SectorDataFrame)
print(etf_1.HoldingDataFrame)
