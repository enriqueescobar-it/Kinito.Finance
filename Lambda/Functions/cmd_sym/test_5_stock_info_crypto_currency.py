from Common.InfoType.stock_info import stock_info

print('\n============   ', 'crypto_stock_info', '   ============\n')
crypto_stock_info: stock_info = stock_info('ETH-USD')
print(crypto_stock_info.to_json())
print(crypto_stock_info)

print('\n============   ', 'c_stock_info', '   ============\n')
c_stock_info: stock_info = stock_info('XRP-USD')
print(c_stock_info.to_json())
print(c_stock_info)
