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

index_list: list = ['^SOX', '^GSPC', '^VIX', '^VVIX', '^SKEW', '^GSPTSE', '^IXIC', '^NDX', '^NYA', '^DJI', '^TNX', '^TYX', '^W5000']
count: int = 0

for index_item in index_list:
    index_title: str = "index_stock_" + index_item
    index_compa: str = "company " + str(count)
    index_quote: str = "quote_" + str(count)
    print('\n============   ', index_title, '   ============\n')
    index_stock: IndexFund = IndexFund(index_compa, index_item, index_quote)
    print(index_stock.to_json())
    print(index_stock)
