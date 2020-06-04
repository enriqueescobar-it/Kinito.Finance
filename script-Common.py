from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print("Source:", yahooStockOption.Source)
print("Ticker:", yahooStockOption.Ticker)
print("Link:", yahooStockOption.YahooSummaryScrapper.Link)
print("MarketCap:", yahooStockOption.YahooSummaryScrapper.MarketCap)
print("Beta:", yahooStockOption.YahooSummaryScrapper.Beta)
print("PEratio:", yahooStockOption.YahooSummaryScrapper.PEratio)
print("EPS:", yahooStockOption.YahooSummaryScrapper.EPS)
print("EarningsDate:", yahooStockOption.YahooSummaryScrapper.EarningsDate)
print(yahooStockOption.HistoricalData.describe(include='all'))
