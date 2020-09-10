from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.EmaIndicator import EmaIndicator
from Common.Strategies.TechIndicators.EmaStrategy import EmaStrategy

yahooStockOption: YahooStockOption = YahooStockOption('WCN')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: EmaIndicator = EmaIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockStrategy: EmaStrategy = EmaStrategy(yahooStockIndicator)
yahooStockStrategy.Plot().show()
