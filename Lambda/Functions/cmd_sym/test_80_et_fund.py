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

et_list: list = ['VOO', 'VOOG', 'FDTS']
count: int = 0

for et_item in et_list:
    et_title: str = "et_stock_" + et_item
    et_compa: str = "company " + str(count)
    et_quote: str = "quote_" + str(count)
    print('\n============   ', et_title, '   ============\n')
    et_stock: ExchangeTradedFund = ExchangeTradedFund(et_compa, et_item, et_quote)
    print(et_stock.to_json())
    print(et_stock)
