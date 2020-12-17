from Common.Comparators.Index.IndexComparator import IndexComparator
from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.CrudeOilIndex import CrudeOilIndex
from Common.StockMarketIndex.Yahoo.DaxIndex import DaxIndex
from Common.StockMarketIndex.Yahoo.DowJonesIndex import DowJonesIndex
from Common.StockMarketIndex.Yahoo.Estx50Index import Estx50Index
from Common.StockMarketIndex.Yahoo.EuroNext100Index import EuroNext100Index
from Common.StockMarketIndex.Yahoo.GoldIndex import GoldIndex
from Common.StockMarketIndex.Yahoo.OvxIndex import OvxIndex
from Common.StockMarketIndex.Yahoo.SilverIndex import SilverIndex
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
from Common.StockMarketIndex.Yahoo.NseIndex import NseIndex
from Common.StockMarketIndex.Yahoo.FvxIndex import FvxIndex
from Common.StockMarketIndex.Yahoo.SoxIndex import SoxIndex
from Common.StockMarketIndex.Yahoo.TnxIndex import TnxIndex
from Common.StockMarketIndex.Yahoo.TreasuryBill13Index import TreasuryBill13Index
#from Common.StockMarketIndex.Yahoo.Vix3mIndex import Vix3mIndex
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.TyxIndex import TyxIndex
from Common.StockMarketIndex.Yahoo.VixIndex import VixIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.AbstractTechIndicatorStrategy import AbstractTechIndicatorStrategy
from Common.Strategies.TechIndicators.EmaStrategy import EmaStrategy
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy
from Common.Strategies.TechIndicators.RsiStrategy import RsiStrategy
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.TechIndicators.EmaIndicator import EmaIndicator
from Common.TechIndicators.MacdIndicator import MacdIndicator
from Common.TechIndicators.RsiIndicator import RsiIndicator
from Common.TechIndicators.SmaIndicator import SmaIndicator

yahooStockOption: YahooStockOption = YahooStockOption('XWEB')#'ESTC')XWEB DDOG BEKE GBTC GNDP.V
# DividendYield [2%, 4%]
# DividendGrowthRate 6% +
# PEratio [15, 20]
# PBratio [1, 3]
# Return on equity
# Earnings Per Share
# Earnings Per Share Growth
# EBITDA
# Dividend Payout Ratio
# Free Cash flow
#YCBD GRWG FSZ AMZN WELL WCN WMT MWK CP COST KO AMT MA AMD BAC NVDA
#KL WCN OTEX AQN TFII CP CNI LMT RY BRK-B GNW OTEX BPY LMT STOR GME SNE HD
#BCE, ZWB, CM, KEY, VNR, ENB, PPL, SJR.B, NPI, AQN FTS NPI
#ETFs:ARKK TEC.TO, VFV and ACES XEI ARKF QQC-f ZQQ XIT HQU SOXL HZU JNUG FIE BRTXQ
#CCA CGO RCI.B
# Canadian Dividend Aristocrat List from SnP Global
# Canadian Dividend All-Star List
# David Fish's CCC List
# growth portfolio= ETFs & blue chips
# income portfolio= Tx34 IBMx8 ABBVx12 GMx30 Fx126 IRMx30 MPWx60 AGNCx57 PSECx149 MAINx27
# ETSY ESTC VYM - VGT - VTI - VPU / ARKK ARKG ARKQ ARKW
# BND-- <= VXUS- <= BNDX-- <= VNQ- <= VBK <= VYM <= VPU <= VOT ~ VTI <= VIG <= MGK ~ VOO ~ VOOG
# VYM VTSAX/ SWTSX/ FZROX index vs. VTI/ SCHB ETF, VFIAX/ SWPPX/ VXAIX index vs. VOO/ SCHX
# FZROX FZILX FSRNX
# VTSAX
# [NFLX, NKE, AMZN] [MRNA, MSFT, CAT] [T, XOM, MO]
# 60% StockMarketFund (FZROX~SWTSX~VTSAX) 20% InternationalFund (FZILX~SWISX~VTIAX) 20% REITFund (FSRNX)
# Sector ETFs: VGT VPU VDC VYM
# Sector Int'l: T (55*30.21$) IBM (14*126.66$) ABBV (21*82.79$) GM (46*35.24$) F (186*8.78$)
# IRM (52*33.48$) MPW (93*17.34$) AGNC (93*17.17$) PSEC (245*6.67$) MAIN (41*37.95$) VYMI (5*59.21$)
# MWK YCBD GRWG FSZ AMZN CGO RCI PPL SJR.B AQN CP CNI TD KL WCN BPY OTEX
# BCE ZWB CM KEY VNR ENB TFII LMT WMT RY BRKB GNW IT
# ETFs: BRTXQ FZILX FSRNX VTSAX FPE HPI
# TFII LSPD T FTS RY SHOP
# AAPL ABBV+ AAOI ADBE+ ABR+ ABT ABX.TO&GOLD ACES ADC+ ADP AGNC AKAM AMGN AMD AMP AMT AMZN ANTM AQN AQN.TO ARKK ARKG ARKQ ARKW APPS+++
# APHA+ ASAN ARKF ARKK AVAV AVGO AVB AYX++ AZN AIVSX+ AEM+ AEM.TO+ AWK+ ANET+ AT.TO ATZ.TO. ACO-X.TO+ ARKG+
# BA BCE BCE.TO. BNS BPY BABA BIDU- BBBY BNTX BRK-B BRKA BRKB BRTXQ BYND BNS.TO. BIP+ BZUN+ BILI++ BEP+ BYND+ BAM-A.TO+ BMO.TO.
# CAG CAT CCA CCA.TO. CAR.UN.TO CGNX CGO CGO.TO. CHD CHWY CL- CLX CM CNI CSU.TO CSX CVD CMCSA COST+ CP CRM CSCO CDNS CNQ.TO CSIQ CELH+
# CNR.TO+ CU.TO. CSU.TO++ CTC-A.TO+ CLR.TO. CRWD++
# DCBO.TO DND.TO CU.TO DLHC DDOG DKNG+ DDOG+ DOL.TO+ DND.TO+ DIS-
# EMR+ ENB ENB.TO ESS ESTC+ ESPO EMA.TO ET ETSY+ ENGH.TO+ ENPH+ EEM EQB.TO+ ELY+
# F FD.TO FF.TO FFMG FENY FIE FIVG FROG FSLR FSLY+ FSRNX FSZ FTS+ FTS.TO+ FOOD.TO FZILX FZROX FVRR FXAIX FEYE-
# GM GIS GLD GLW GMF GNW GRWG GILD GBTC GAMR GSY.TO+ GOOD GXC+ GOOG+
# HD+ HLT HQU HZU HEO.V HII HLF.TO. IBM IBUY IWFH INTC IPO IIVI IVAC IGV+ IBM- IRM+ IT IPFF JKS JD+ JNJ+ JPM+ JNUG JNPR
# KEY K KXS.TO KDP KL KL.TO KO- KR KMI K.TO KXS.TO+
# LB.TO LMT LMND LOW+ LSPD++ LSPD.TO++ LVGO LOGI+ LAND+ LMND+
# M MA MAIN MELI+ MFI.TO MO MU MCD- MGM MPW MRK+ MARA MRNA MRVL MSFT+ MWK MDY MRU.TO MSCI+ NXST MFC.TO. MXIM+ NWC.TO.
# NEE+ NEM+ NET NKE NSP NEAR NFLX NIO++ NLY NLOK NNDM NPI NOBL+ NVEI.TO NVDA+++++ NOW+ O+ OTEX OHI O- NWC.TO. OKTA+++++
# PM PANW PFE PINS PGX PEP PLAN PLTR PPL PRU PVD PTON PAWZ PSEC PYPL PKI.TO PIODX+ PKI.TO+ PINS+ PHO POW.TO. PAAS+++
# QCOM QQC-f QQQ QRVO QSR.TO+ RBA RCI+ RCI.B.TO+ REAL.TO REGI ROK+ RUN RY+ RY.TO+ RCI.B.TO. RIOT RHS QRS.TO REAL.TO ROKU+
# SU SU.TO. SIS.TO+ SNA SBUX SHOP+ SHOP.TO+ SPLK SPYD SJR.B SJR-B.TO SLV SNAP SNOW+ SPOT SOXL SRU.UN.TO. SPG SAP SPNS STOR+ STAG SEDG+ SJR-B.TO SOY.TO. ZS++
# T- T.TO+ TD TDOC+ TEC.TO TAL+ TEAM TFII+ TFII.TO+ TGT- TRMB TSLA+++ TRP TRP.TO TTD+++++ TOU.TO TROW TWLO++++ TXN TWST+ TVE.TO. TPB+++
# U UNM UNP UPWK
# VDC VFC VFF VFV.TO VGT VMW VNR VPL VPU VTSAX VYM VYMI VZ+ V VOO+ VOOG+ VNQ+ VIOO VHT VSP.TO
# WCN WCN.TO+ WELL.TO WEED.TO++ WFG WMT- WORK. WPC- XEI XIT XBC.TO XOM. XWEB+ XLK+ XBC.V+++ YCBD ZG ZM+++ ZQQ ZS ZWB
print(yahooStockOption.DataFrame.describe(include='all'))
#exit(1000)
sAnP500: AbstractStockMarketIndex = SnP500Index('yahoo', "^GSPC", yahooStockOption.TimeSpan)
vixIndex: AbstractStockMarketIndex = VixIndex('yahoo', "^VIX", yahooStockOption.TimeSpan)
''' #ovxIndex: AbstractStockMarketIndex = OvxIndex('yahoo', "^OVX", yahooStockOption.TimeSpan)
sAndPTsx: AbstractStockMarketIndex = SnPTSXComposite('yahoo', "^GSPTSE", yahooStockOption.TimeSpan)
nasdaqIndex: AbstractStockMarketIndex = NasdaqIndex('yahoo', "^IXIC", yahooStockOption.TimeSpan)
nyseIndex: AbstractStockMarketIndex = NyseIndex('yahoo', "^NYA", yahooStockOption.TimeSpan)
dowJonesIndex: AbstractStockMarketIndex = DowJonesIndex('yahoo', "^DJI", yahooStockOption.TimeSpan)
goldIndex: AbstractStockMarketIndex = GoldIndex('yahoo', "GC=F", yahooStockOption.TimeSpan)
silverIndex: AbstractStockMarketIndex = SilverIndex('yahoo', "SI=F", yahooStockOption.TimeSpan)
crudeOilIndex: AbstractStockMarketIndex = CrudeOilIndex('yahoo', "CL=F", yahooStockOption.TimeSpan)
soxIndex: AbstractStockMarketIndex = SoxIndex('yahoo', "^SOX", yahooStockOption.TimeSpan)
tnxIndex: AbstractStockMarketIndex = TnxIndex('yahoo', "^TNX", yahooStockOption.TimeSpan)
tyxIndex: AbstractStockMarketIndex = TyxIndex('yahoo', "^TYX", yahooStockOption.TimeSpan)
#vix3mIndex: AbstractStockMarketIndex = Vix3mIndex('yahoo', "^VIX3M", yahooStockOption.TimeSpan)
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
irxIndex: AbstractStockMarketIndex = TreasuryBill13Index('yahoo', "^IRX", yahooStockOption.TimeSpan)
jkseIndex: AbstractStockMarketIndex = JkseIndex('yahoo', "^JKSE", yahooStockOption.TimeSpan)
kospIndex: AbstractStockMarketIndex = KospIndex('yahoo', "^KS11", yahooStockOption.TimeSpan)
marketIndices = list()
marketIndices.append(sAnP500)
marketIndices.append(vixIndex)
#marketIndices.append(ovxIndex)
marketIndices.append(sAndPTsx)
marketIndices.append(nasdaqIndex)
marketIndices.append(nyseIndex)
marketIndices.append(dowJonesIndex)
marketIndices.append(goldIndex)
marketIndices.append(silverIndex)
marketIndices.append(crudeOilIndex)
marketIndices.append(soxIndex)
marketIndices.append(tnxIndex)
marketIndices.append(tyxIndex)
#marketIndices.append(vix3mIndex)
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
marketIndices.append(irxIndex)
marketIndices.append(jkseIndex)
marketIndices.append(kospIndex)
indexComparator: IndexComparator = IndexComparator(yahooStockOption, marketIndices)
'''
yahooStockOptionPlotter: HistoricalPlotter = HistoricalPlotter(yahooStockOption, vixIndex, sAnP500)
yahooStockOptionPlotter.GraphPlot().show()
yahooStockOptionPlotter.Plot().show()
#exit(31415)
#yahooStockOptionPlotter.PlotTimely()
#exit(31415)
#yahooMacdIndicator: MacdIndicator = yahooStockOptionPlotter.MacdInd #MacdIndicator(yahooStockOption)
print(yahooStockOptionPlotter.MacdInd.GetData().columns)
#yahooMacdIndicator.PlotData().show()
#yahooMacdStrategy: MacdStrategy = yahooStockOptionPlotter.MacdStrat #MacdStrategy(yahooMacdIndicator)
#yahooStockOptionPlotter.MacdStrat.Plot().show()
yahooStockOptionPlotter.MacdStrat.PlotAll().show()
#yahooSmaIndicator: SmaIndicator = yahooStockOptionPlotter.SmaInd #SmaIndicator(yahooStockOption)
print(yahooStockOptionPlotter.SmaInd.GetData().columns)
#yahooSmaIndicator.PlotData().show()
#yahooSmaStrategy: SmaStrategy = yahooStockOptionPlotter.SmaStrat #SmaStrategy(yahooSmaIndicator)
#yahooStockOptionPlotter.SmaStrat.Plot().show()
yahooStockOptionPlotter.SmaStrat.PlotAll().show()
#yahooEmaIndicator: EmaIndicator = yahooStockOptionPlotter.EmaInd #EmaIndicator(yahooStockOption)
print(yahooStockOptionPlotter.EmaInd.GetData().columns)
#yahooEmaIndicator.PlotData().show()
#yahooEmaStrategy: EmaStrategy = yahooStockOptionPlotter.EmaStrat #EmaStrategy(yahooEmaIndicator)
#yahooStockOptionPlotter.EmaStrat.Plot().show()
yahooStockOptionPlotter.EmaStrat.PlotAll().show()
#yahooRsiIndicator: RsiIndicator = yahooStockOptionPlotter.RsiInd #RsiIndicator(yahooStockOption)
print(yahooStockOptionPlotter.RsiInd.GetData().columns)
yahooStockOptionPlotter.RsiInd.PlotData().show()
yahooEmaStrategy: RsiStrategy = yahooStockOptionPlotter.RsiStrat #RsiStrategy(yahooEmaIndicator)
yahooStockOptionPlotter.RsiStrat.PlotAll().show()
#***
exit(111)
yahooStockOptionPlotter.IndicatorPlot().show()
yahooStockOptionPlotter.StrategyPlot().show()

# preprocessing
## Mean removal
print('MEAN=', yahooStockOption.Data.Sparse.mean(axis=0))
print('SD=', yahooStockOption.Data.Sparse.std(axis=0))
# classification by classes
# viz
## uni variate
