from Common.Comparators.Index.IndexComparator import IndexComparator
from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.SnPTSXComposite import SnPTSXComposite
from Common.StockMarketIndex.Yahoo.SnP500 import SnP500
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
#from Common.Measures.Time.TimeSpan import TimeSpan

yahooStockOption: YahooStockOption = YahooStockOption('SUN')
print(yahooStockOption.HistoricalData.describe(include='all'))
sAndPTsx: AbstractStockMarketIndex = SnPTSXComposite('yahoo', "^GSPTSE", yahooStockOption.TimeSpan)
sAnP500: AbstractStockMarketIndex = SnP500('yahoo', "^GSPC", yahooStockOption.TimeSpan)
print(sAndPTsx.HistoricalData.head())
marketIndices = list()
marketIndices.append(sAndPTsx)
marketIndices.append(sAnP500)
indexComparator: IndexComparator = IndexComparator(yahooStockOption, marketIndices)
exit(666)
yahooStockOptionPlotter: HistoricalPlotter = \
    HistoricalPlotter(yahooStockOption)
yahooStockOptionPlotter.Plot().show()
yahooStockOptionPlotter.Distro().show()
yahooStockOptionPlotter.Daily().show()
yahooStockOptionPlotter.DailyHist().show()
yahooStockOptionPlotter.DailyCum().show()
yahooStockOptionPlotter.Monthly().show()
yahooStockOptionPlotter.MonthlyHist().show()
yahooStockOptionPlotter.MonthlyCum().show()
# preprocessing
## Mean removal
print('MEAN=', yahooStockOption.HistoricalStandardized.mean(axis=0))
print('SD=', yahooStockOption.HistoricalStandardized.std(axis=0))
## scaling
print('MinMaxScaled=', yahooStockOption.HistoricalScaled)
## normalization
print('L1 NORM=', yahooStockOption.HistoricalL1Normalized)
## binarization
print('BIN=', yahooStockOption.HistoricalBinary)
# classification by classes
# viz
## uni variate
'''import matplotlib.pyplot as plt
print(yahooStockOption.HistoricalData.head())
yahooStockOption.HistoricalData.plot(kind='box', subplots=True, layout=(2, 3), sharex=False, sharey=False)
plt.show()
### box and whiskers
yahooStockOption.HistoricalData.hist()
plt.show()
## multi variate
from pandas.plotting import scatter_matrix
scatter_matrix(yahooStockOption.HistoricalData)
plt.show()'''
