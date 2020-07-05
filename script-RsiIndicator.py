from Common.Plotters.TechIndicators.RsiPlotter import RsiPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.RsiIndicator import RsiIndicator

yahooStockOption: YahooStockOption = YahooStockOption('TD')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockHistory = yahooStockOption.HistoricalData
yahooStockSource = yahooStockOption.Source
yahooStockTicker = yahooStockOption.Ticker
yahooStockTs = yahooStockOption.TimeSpan
yahooStockRsi = RsiIndicator(yahooStockHistory, yahooStockSource)
print(yahooStockRsi._RsiLabel)
yahooStockRsiPlot = RsiPlotter(yahooStockHistory.index, yahooStockRsi, yahooStockSource, yahooStockTicker, yahooStockTs)
yahooStockRsiPlot.Plot()
