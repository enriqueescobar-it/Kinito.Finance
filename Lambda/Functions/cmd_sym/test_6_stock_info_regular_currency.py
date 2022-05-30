from Common.InfoType.stock_info import stock_info

print('\n============   ', 'currency_stock_info', '   ============\n')
currency_stock_info: stock_info = stock_info('CDN=X')
print(currency_stock_info.to_json())
print(currency_stock_info)

print('\n============   ', 'curr_stock_info', '   ============\n')
curr_stock_info: stock_info = stock_info('JPY=X')
print(curr_stock_info.to_json())
print(curr_stock_info)
