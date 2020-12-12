from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.SmaIndicator import SmaIndicator
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy

yahooStockOption: YahooStockOption = YahooStockOption('ESTC')
print(yahooStockOption.DataFrame.describe(include='all'))
yahooStockIndicator: SmaIndicator = SmaIndicator(yahooStockOption)
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
yahooStockStrategy: SmaStrategy = SmaStrategy(yahooStockIndicator)
yahooStockStrategy.Plot().show()
yahooStockStrategy.PlotAll().show()
