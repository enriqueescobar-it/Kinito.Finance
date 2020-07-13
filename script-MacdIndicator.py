from Common.Plotters.Strategies.MacdStrategyPlotter import MacdStrategyPlotter
from Common.Plotters.TechIndicators.MacdIndicatorPlotter import MacdIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy
from Common.TechIndicators.MacdIndicator import MacdIndicator

yahooStockOption: YahooStockOption = YahooStockOption('TD')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: MacdIndicator = MacdIndicator(yahooStockOption)
print(yahooStockIndicator._Label)
yahooStockIndicatorPlotter: MacdIndicatorPlotter =\
    MacdIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()
yahooStockStrategy: MacdStrategy =\
    MacdStrategy(yahooStockIndicator, yahooStockOption)
yahooStockStrategyPlotter: MacdStrategyPlotter =\
    MacdStrategyPlotter(yahooStockOption, yahooStockStrategy).Plot()
yahooStockStrategyPlotter.show()
