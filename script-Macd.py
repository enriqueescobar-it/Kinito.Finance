from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.MacdIndicator import MacdIndicator
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy

yahooStockOption: YahooStockOption = YahooStockOption('AAPL')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: MacdIndicator = MacdIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockStrategy: MacdStrategy = MacdStrategy(yahooStockIndicator)
#yahooStockStrategy.Plot().show()
yahooStockStrategy.PlotAll().show()
