from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Options.AbstractStockOption import AbstractStockOption

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

option_list: list = ['APT', 'OPT']
count: int = 0

for option_item in option_list:
    option_title: str = "option_stock_" + option_item
    option_compa: str = "company " + str(count)
    option_quote: str = "quote_" + str(count)
    print('\n============   ', option_title, '   ============\n')
    option_stock: AbstractStockOption = AbstractStockOption(option_compa, option_item, option_quote)
    print(option_stock.to_json())
    print(option_stock)
    count = count + 1
