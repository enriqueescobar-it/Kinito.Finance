from Common.Plotters.Strategies.EmaStrategyPlotter import EmaStrategyPlotter
from Common.Plotters.TechIndicators.EmaIndicatorPlotter import EmaIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.EmaStrategy import EmaStrategy
from Common.TechIndicators.EmaIndicator import EmaIndicator

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: EmaIndicator = EmaIndicator(yahooStockOption)
print(yahooStockIndicator._Label)
yahooStockIndicatorPlotter: EmaIndicatorPlotter = EmaIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()
yahooStockStrategy: EmaStrategy = EmaStrategy(yahooStockIndicator, yahooStockOption)
yahooStockStrategyPlotter: EmaStrategyPlotter = EmaStrategyPlotter(yahooStockOption, yahooStockStrategy).Plot()
yahooStockStrategyPlotter.show()
