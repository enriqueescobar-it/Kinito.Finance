from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.MacdIndicator import MacdIndicator
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: MacdIndicator = MacdIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockIndicator.PlotData().show()
yahooStockStrategy: MacdStrategy = MacdStrategy(yahooStockIndicator)
yahooStockStrategy.Plot().show()
yahooStockStrategy.PlotAll().show()
