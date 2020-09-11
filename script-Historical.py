from Common.Comparators.Index.IndexComparator import IndexComparator
from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.CrudeOilIndex import CrudeOilIndex
from Common.StockMarketIndex.Yahoo.DaxIndex import DaxIndex
from Common.StockMarketIndex.Yahoo.DowJonesIndex import DowJonesIndex
from Common.StockMarketIndex.Yahoo.Estx50Index import Estx50Index
from Common.StockMarketIndex.Yahoo.EuroNext100Index import EuroNext100Index
from Common.StockMarketIndex.Yahoo.GoldIndex import GoldIndex
from Common.StockMarketIndex.Yahoo.HangSengIndex import HangSengIndex
from Common.StockMarketIndex.Yahoo.BovespaIndex import BovespaIndex
from Common.StockMarketIndex.Yahoo.IpcMexicoIndex import IpcMexicoIndex
from Common.StockMarketIndex.Yahoo.IpsaIndex import IpsaIndex
from Common.StockMarketIndex.Yahoo.JkseIndex import JkseIndex
from Common.StockMarketIndex.Yahoo.KospIndex import KospIndex
from Common.StockMarketIndex.Yahoo.MoexRussiaIndex import MoexRussiaIndex
from Common.StockMarketIndex.Yahoo.NasdaqIndex import NasdaqIndex
from Common.StockMarketIndex.Yahoo.Nikkei225Index import Nikkei225Index
from Common.StockMarketIndex.Yahoo.NyseComposite import NyseIndex
from Common.StockMarketIndex.Yahoo.ShenzhenComponentIndex import ShenzhenComponentIndex
from Common.StockMarketIndex.Yahoo.SnPTSXComposite import SnPTSXComposite
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.NseIndex import NseIndex
from Common.StockMarketIndex.Yahoo.FvxIndex import FvxIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
#from Common.Measures.Time.TimeSpan import TimeSpan

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
#MWK YCBD GRWG FSZ AMZN
#KL WCN OTEX AQN TFII CP CNI LMT WMT RY BRK-B GNW OTEX BPY
#BCE, ZWB, CM, KEY, VNR, ENB, PPL, SJR.B, NPI, AQN
#ETFs:ARKK TEC.TO, VFV and ACES XEI ARKF QQC-f ZQQ XIT HQU SOXL QQQ HZU JNUG FIE
#BRTXQ
#CCA CGO RCI.B
# FZROX FZILX FSRNX VTSAX
# 60% StockMarketFund (FZROX~SWTSX~VTSAX) 20% InternationalFund (FZILX~SWISX~VTIAX) 20% REITFund (FSRNX)
# Sector ETFs: VGT VPU VDC VYM
print(yahooStockOption.HistoricalData.describe(include='all'))
'''
sAndPTsx: AbstractStockMarketIndex = SnPTSXComposite('yahoo', "^GSPTSE", yahooStockOption.TimeSpan)
sAnP500: AbstractStockMarketIndex = SnP500Index('yahoo', "^GSPC", yahooStockOption.TimeSpan)
nasdaqIndex: AbstractStockMarketIndex = NasdaqIndex('yahoo', "^IXIC", yahooStockOption.TimeSpan)
nyseIndex: AbstractStockMarketIndex = NyseIndex('yahoo', "^NYA", yahooStockOption.TimeSpan)
dowJonesIndex: AbstractStockMarketIndex = DowJonesIndex('yahoo', "^DJI", yahooStockOption.TimeSpan)
goldIndex: AbstractStockMarketIndex = GoldIndex('yahoo', "GC=F", yahooStockOption.TimeSpan)
crudeOilIndex: AbstractStockMarketIndex = CrudeOilIndex('yahoo', "CL=F", yahooStockOption.TimeSpan)
daxIndex: AbstractStockMarketIndex = DaxIndex('yahoo', "^GDAXI", yahooStockOption.TimeSpan)
euroNext100Index: AbstractStockMarketIndex = EuroNext100Index('yahoo', "^N100", yahooStockOption.TimeSpan)
estx50Index: AbstractStockMarketIndex = Estx50Index('yahoo', "^N100", yahooStockOption.TimeSpan)
nikkei225Index: AbstractStockMarketIndex = Nikkei225Index('yahoo', "^N225", yahooStockOption.TimeSpan)
moexRussiaIndex: AbstractStockMarketIndex = MoexRussiaIndex('yahoo', "IMOEX.ME", yahooStockOption.TimeSpan)
hangSengIndex: AbstractStockMarketIndex = HangSengIndex('yahoo', "^HSI", yahooStockOption.TimeSpan)
shenzhenComponentIndex: AbstractStockMarketIndex = ShenzhenComponentIndex('yahoo', "399001.SZ", yahooStockOption.TimeSpan)
bovespaIndex: AbstractStockMarketIndex = BovespaIndex('yahoo', "^BVSP", yahooStockOption.TimeSpan)
ipcMexicoIndex: AbstractStockMarketIndex = IpcMexicoIndex('yahoo', "^MXX", yahooStockOption.TimeSpan)
nifty50Index: AbstractStockMarketIndex = NseIndex('yahoo', "^NSEI", yahooStockOption.TimeSpan)
ipsaIndex: AbstractStockMarketIndex = IpsaIndex('yahoo', "^IPSA", yahooStockOption.TimeSpan)
fvxIndex: AbstractStockMarketIndex = FvxIndex('yahoo', "^FVX", yahooStockOption.TimeSpan)
jkseIndex: AbstractStockMarketIndex = JkseIndex('yahoo', "^JKSE", yahooStockOption.TimeSpan)
kospIndex: AbstractStockMarketIndex = KospIndex('yahoo', "^KS11", yahooStockOption.TimeSpan)
marketIndices = list()
marketIndices.append(sAndPTsx)
marketIndices.append(sAnP500)
marketIndices.append(nasdaqIndex)
marketIndices.append(nyseIndex)
marketIndices.append(dowJonesIndex)
marketIndices.append(goldIndex)
marketIndices.append(crudeOilIndex)
marketIndices.append(daxIndex)
marketIndices.append(euroNext100Index)
marketIndices.append(estx50Index)
marketIndices.append(nikkei225Index)
marketIndices.append(moexRussiaIndex)
marketIndices.append(hangSengIndex)
marketIndices.append(shenzhenComponentIndex)
marketIndices.append(bovespaIndex)
marketIndices.append(ipcMexicoIndex)
marketIndices.append(nifty50Index)
marketIndices.append(ipsaIndex)
marketIndices.append(fvxIndex)
marketIndices.append(jkseIndex)
marketIndices.append(kospIndex)
indexComparator: IndexComparator = IndexComparator(yahooStockOption, marketIndices)
'''
yahooStockOptionPlotter: HistoricalPlotter = \
    HistoricalPlotter(yahooStockOption)
yahooStockOptionPlotter.Plot().show()
#yahooStockOptionPlotter.PlotForecast().show()
yahooStockOptionPlotter.GraphPlot().show()
yahooStockOptionPlotter.Daily().show()
yahooStockOptionPlotter.DailyCum().show()
yahooStockOptionPlotter.DailyHist().show()
yahooStockOptionPlotter.Monthly().show()
yahooStockOptionPlotter.MonthlyCum().show()
yahooStockOptionPlotter.MonthlyHist().show()
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
