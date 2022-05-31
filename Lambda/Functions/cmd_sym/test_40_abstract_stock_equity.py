from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Equities.AbstractStockEquity import AbstractStockEquity

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

equity_list: list = ['AAPL', 'AMZN']
count: int = 0

for equity_item in equity_list:
    equity_title: str = "equity_stock_" + equity_item
    equity_compa: str = "company " + str(count)
    equity_quote: str = "quote_" + str(count)
    print('\n============   ', equity_title, '   ============\n')
    equity_stock: AbstractStockEquity = AbstractStockEquity(equity_compa, equity_item, equity_quote)
    print(equity_stock.to_json())
    print(equity_stock)
