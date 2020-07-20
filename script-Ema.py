from Common.Plotters.TechIndicators.EmaIndicatorPlotter import EmaIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.EmaIndicator import EmaIndicator

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: EmaIndicator = EmaIndicator(yahooStockOption)
print(yahooStockIndicator._Label)
yahooStockIndicatorPlotter: EmaIndicatorPlotter =\
    EmaIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()
