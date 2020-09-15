from Common.Comparators.Portfolio.PortfolioComparator import PortfolioComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
#from typing import List
yahooTickers: list = ['CNI', 'CP', 'TD', 'OTEX']
yahooStocks: list = list()
for yahooTicker in yahooTickers:
    yahooStocks.append(YahooStockOption(yahooTicker))
    print(yahooTicker)

yahooPc: PortfolioComparator = PortfolioComparator(yahooStocks)
yahooPc.PlotAllData().show()
yahooPc.PlotAll().show()
