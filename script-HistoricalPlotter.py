from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockOptionPlotter: HistoricalPlotter = \
    HistoricalPlotter(yahooStockOption).__plot()
yahooStockOptionPlotter.show()
