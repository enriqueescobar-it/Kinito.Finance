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

mutual_list: list = ['HISFX', 'QASGX', 'RYVYX', 'SCATX', 'SAGAX']
count: int = 0

for mutual_item in mutual_list:
    mutual_title: str = "mutual_stock_" + mutual_item
    mutual_compa: str = "company " + str(count)
    mutual_quote: str = "quote_" + str(count)
    print('\n============   ', mutual_title, '   ============\n')
    mutual_stock: MutualFund = MutualFund(mutual_compa, mutual_item, mutual_quote)
    print(mutual_stock.to_json())
    print(mutual_stock)
