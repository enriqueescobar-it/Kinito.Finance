from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.EmaIndicator import EmaIndicator
from Common.Strategies.TechIndicators.EmaStrategy import EmaStrategy
from Common.Plotters.Strategies.EmaStrategyPlotter import EmaStrategyPlotter

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: EmaIndicator = EmaIndicator(yahooStockOption)
print(yahooStockIndicator.GetLabel())
yahooStockIndicator.PlotData().show()
'''
yahooStockIndicatorPlotter: EmaIndicatorPlotter = EmaIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()
yahooStockStrategy: EmaStrategy = EmaStrategy(yahooStockIndicator, yahooStockOption)
yahooStockStrategyPlotter: EmaStrategyPlotter = EmaStrategyPlotter(yahooStockOption, yahooStockStrategy).Plot()
yahooStockStrategyPlotter.show()'''
