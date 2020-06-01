from Common.WebScrappers.Yahoo.YahooSummaryScrapper import YahooSummaryScrapper

stockOptionTicker: str = "AMZN"
s: YahooSummaryScrapper = YahooSummaryScrapper(stockOptionTicker)
print(s.Link)
s.ParseBody()
print(s.MarketCap)
print(s.Beta)
print(s.PEratio)
print(s.EPS)
print(s.EarningsDate)
