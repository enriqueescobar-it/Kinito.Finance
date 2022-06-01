from Common.StockType.AbstractStock import AbstractStock
from Common.StockType.Currencies.AbstractCurrency import AbstractCurrency
from Common.StockType.Currencies.Crypto.CryptoCurrency import CryptoCurrency

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
    crypto_currency_title: str = "crypto_currency_stock_" + crypto_currency_item
    crypto_currency_compa: str = "company " + str(count)
    crypto_currency_quote: str = "quote_" + str(count)
    print('\n============   ', crypto_currency_title, '   ============\n')
    crypto_currency_stock: CryptoCurrency = CryptoCurrency(crypto_currency_compa, crypto_currency_item, crypto_currency_quote)
    print(crypto_currency_stock.to_json())
    print(crypto_currency_stock)
