from Common.Plotters.TechIndicators.MacdPlotter import MacdPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.MacdIndicator import MacdIndicator

yahooStockOption: YahooStockOption = YahooStockOption('TD')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator = MacdIndicator(yahooStockOption)
print(yahooStockIndicator._Label)
yahooStockPlotter = MacdPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockPlotter.show()
