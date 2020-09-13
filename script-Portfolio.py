from Common.Comparators.Portfolio.PortfolioComparator import PortfolioComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption

yahooTickers: list = ['CNI', 'CP', 'TD', 'OTEX']
yahooStocks: list = list()
for yahooTicker in yahooTickers:
    yahooStocks.append(YahooStockOption(yahooTicker))
    print(yahooTicker)

yahooPc: PortfolioComparator = PortfolioComparator(yahooStocks)
