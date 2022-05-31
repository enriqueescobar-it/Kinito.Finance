from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Funds.AbstractStockFund import AbstractStockFund
from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractStockFund', '   ============\n')
abstractStockFund: AbstractStockFund = AbstractStockFund('stock fund', 'A_QUOTE')
print(abstractStockFund.to_json())
print(abstractStockFund)

print('\n============   ', 'etf_0', '   ============\n')
etf_0: ExchangeTradedFund = ExchangeTradedFund('un etf', 'VOO', 'UN_QUOTE')
print(etf_0.to_json())
print(etf_0)

print('\n============   ', 'etf_1', '   ============\n')
etf_1: ExchangeTradedFund = ExchangeTradedFund('un etf', 'VOOG', 'UNE_QUOTE')
print(etf_1.to_json())
print(etf_1)
