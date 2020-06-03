from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.WebScrappers.Yahoo.YahooSummaryScrapper import YahooSummaryScrapper

stockOptionTicker: str = "AMZN"
summaryScrapper: YahooSummaryScrapper = YahooSummaryScrapper(stockOptionTicker)
print(summaryScrapper.Link)
summaryScrapper.ParseBody()
print(summaryScrapper.MarketCap)
print(summaryScrapper.Beta)
print(summaryScrapper.PEratio)
print(summaryScrapper.EPS)
print(summaryScrapper.EarningsDate)
yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.Source)
print(yahooStockOption.Ticker)
print(yahooStockOption.HistoricalData.describe(include='all'))
