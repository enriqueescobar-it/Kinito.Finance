import time

from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency
from Common.InfoType.StockInfo import StockInfo

print('\n============   ', 'abstractStock', '   ============\n')
abstractStock: AbstractStock = AbstractStock()
print(abstractStock.to_json())
print(abstractStock)

print('\n============   ', 'abstractCurrency', '   ============\n')
abstractCurrency: AbstractCurrency = AbstractCurrency('a cy', 'A_QUOTE')
print(abstractCurrency.to_json())
print(abstractCurrency)

crypto_currency_list: list = ['ETH-USD', 'XRP-USD', 'BTC-USD', 'USDT-USD']
count: int = 0

for crypto_currency_item in crypto_currency_list:
    start_t = time.time()
    print('\n============   ', crypto_currency_item + '_info', '   ============\n')
    a_stock_info: StockInfo = StockInfo(crypto_currency_item)
    print(a_stock_info.to_json())
    print(a_stock_info)
    count = count + 1
    stop_t = time.time()
    print(stop_t - start_t)
