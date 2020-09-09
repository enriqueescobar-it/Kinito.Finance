from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.SmaIndicator import SmaIndicator
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy
#from Common.Plotters.Strategies.SmaStrategyPlotter import SmaStrategyPlotter

yahooStockOption: YahooStockOption = YahooStockOption('AAPL')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: SmaIndicator = SmaIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockIndicator.PlotData().show()
yahooStockStrategy: SmaStrategy = SmaStrategy(yahooStockIndicator)
