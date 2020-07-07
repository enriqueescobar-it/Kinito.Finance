from Common.Plotters.TechIndicators.RsiPlotter import RsiPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.RsiIndicator import RsiIndicator

yahooStockOption: YahooStockOption = YahooStockOption('TD')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockRsi = RsiIndicator(yahooStockOption)
print(yahooStockRsi._RsiLabel)
yahooStockRsiPlot = RsiPlotter(yahooStockOption, yahooStockRsi).Plot()
yahooStockRsiPlot.show()
