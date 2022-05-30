from Common.InfoType.stock_info import stock_info

print('\n============   ', 'equity_stock_info', '   ============\n')
equity_stock_info: stock_info = stock_info('CNI')
print(equity_stock_info.to_json())
print(equity_stock_info)

print('\n============   ', 'eq_stock_info', '   ============\n')
eq_stock_info: stock_info = stock_info('AAPL')
print(eq_stock_info.to_json())
print(eq_stock_info)
