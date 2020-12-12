from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.RsiIndicator import RsiIndicator
#from Common.Strategies.TechIndicators.RsiStrategy import RsiStrategy
#from Common.Plotters.Strategies.RsiStrategyPlotter import RsiStrategyPlotter

yahooStockOption: YahooStockOption = YahooStockOption('ESTC')
print(yahooStockOption.DataFrame.describe(include='all'))
yahooStockIndicator: RsiIndicator = RsiIndicator(yahooStockOption)
print('Column=', yahooStockIndicator.Column)
print('Data=', yahooStockIndicator.GetData().columns)
print('FigSize=', yahooStockIndicator.FigSizeTuple)
print('FigStyle=', yahooStockIndicator.FigStyle)
print('Label=', yahooStockIndicator.Label)
print('LabelX=', yahooStockIndicator.LabelX)
print('LabelXangle=', yahooStockIndicator.LabelXangle)
print('LabelY=', yahooStockIndicator.LabelY)
print('LabelMain=', yahooStockIndicator.LabelMain)
print('LegendPlace=', yahooStockIndicator.LegendPlace)
print('LowHigh=', yahooStockIndicator.LowMedHighTuple)
print('Name=', yahooStockIndicator.Name)
print('Source=', yahooStockIndicator.Source)
yahooStockIndicator.PlotData().show()
'''yahooStockIndicatorPlotter: RsiIndicatorPlotter = RsiIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()'''
#yahooStockStrategy: RsiStrategy = RsiStrategy(yahooStockIndicator, yahooStockOption)
#yahooStockStrategyPlotter: RsiStrategyPlotter = RsiStrategyPlotter(yahooStockOption, yahooStockStrategy).Plot()
#yahooStockStrategyPlotter.show()
