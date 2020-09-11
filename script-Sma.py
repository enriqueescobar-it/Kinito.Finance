from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.SmaIndicator import SmaIndicator
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy
#MWK YCBD GRWG FSZ AMZN
yahooStockOption: YahooStockOption = YahooStockOption('FSZ')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: SmaIndicator = SmaIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockStrategy: SmaStrategy = SmaStrategy(yahooStockIndicator)
yahooStockStrategy.Plot().show()
