from Common.Plotters.TechIndicators.RsiIndicatorPlotter import RsiIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.RsiIndicator import RsiIndicator

yahooStockOption: YahooStockOption = YahooStockOption('TD')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator = RsiIndicator(yahooStockOption)
print(yahooStockIndicator._Label)
yahooStockPlotter = RsiIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockPlotter.show()
