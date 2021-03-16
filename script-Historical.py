from Common.Comparators.Index.IndexComparator import IndexComparator
from Common.Plotters.HistoricalPlotter import HistoricalPlotter
from Common.Readers.Engine.YahooFinStockInfo import YahooFinStockInfo
from Common.StockMarketIndex.AbstractStockMarketIndex import AbstractStockMarketIndex
from Common.StockMarketIndex.Yahoo.BitcoinIndex import BitcoinIndex
from Common.StockMarketIndex.Yahoo.CrudeOilIndex import CrudeOilIndex
from Common.StockMarketIndex.Yahoo.DowJonesIndex import DowJonesIndex
from Common.StockMarketIndex.Yahoo.GoldIndex import GoldIndex
from Common.StockMarketIndex.Yahoo.SilverIndex import SilverIndex
from Common.StockMarketIndex.Yahoo.NasdaqIndex import NasdaqIndex
from Common.StockMarketIndex.Yahoo.Nasdaq100Index import Nasdaq100Index
from Common.StockMarketIndex.Yahoo.NyseComposite import NyseIndex
from Common.StockMarketIndex.Yahoo.SnPTSXComposite import SnPTSXComposite
from Common.StockMarketIndex.Yahoo.FvxIndex import FvxIndex
from Common.StockMarketIndex.Yahoo.SoxIndex import SoxIndex
from Common.StockMarketIndex.Yahoo.TnxIndex import TnxIndex
from Common.StockMarketIndex.Yahoo.TreasuryBill13Index import TreasuryBill13Index
from Common.StockMarketIndex.Yahoo.SnP500Index import SnP500Index
from Common.StockMarketIndex.Yahoo.TyxIndex import TyxIndex
from Common.StockMarketIndex.Yahoo.VixIndex import VixIndex
from Common.StockMarketIndex.Yahoo.SkewIndex import SkewIndex
from Common.StockMarketIndex.Yahoo.Wilshire5kIndex import Wilshire5kIndex
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.StockMarketIndex.Yahoo.DaxIndex import DaxIndex
from Common.StockMarketIndex.Yahoo.Estx50Index import Estx50Index
from Common.StockMarketIndex.Yahoo.EuroNext100Index import EuroNext100Index
from Common.StockMarketIndex.Yahoo.OvxIndex import OvxIndex
from Common.StockMarketIndex.Yahoo.HangSengIndex import HangSengIndex
from Common.StockMarketIndex.Yahoo.BovespaIndex import BovespaIndex
from Common.StockMarketIndex.Yahoo.IpcMexicoIndex import IpcMexicoIndex
from Common.StockMarketIndex.Yahoo.IpsaIndex import IpsaIndex
from Common.StockMarketIndex.Yahoo.JkseIndex import JkseIndex
from Common.StockMarketIndex.Yahoo.KospIndex import KospIndex
from Common.StockMarketIndex.Yahoo.MoexRussiaIndex import MoexRussiaIndex
from Common.StockMarketIndex.Yahoo.Nikkei225Index import Nikkei225Index
from Common.StockMarketIndex.Yahoo.ShenzhenComponentIndex import ShenzhenComponentIndex
from Common.StockMarketIndex.Yahoo.NseIndex import NseIndex
#from Common.StockMarketIndex.Yahoo.Vix3mIndex import Vix3mIndex
from Common.Strategies.TechIndicators.AbstractTechStrategy import AbstractTechStrategy
from Common.Strategies.TechIndicators.EmaStrategy import EmaStrategy
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy
from Common.Strategies.TechIndicators.RsiStrategy import RsiStrategy
from Common.Strategies.TechIndicators.SmaStrategy import SmaStrategy
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.TechIndicators.EmaIndicator import EmaIndicator
from Common.TechIndicators.MacdIndicator import MacdIndicator
from Common.TechIndicators.RsiIndicator import RsiIndicator
from Common.TechIndicators.SmaIndicator import SmaIndicator

# DividendYield [2%, 4%] 2.5 - 6
# DividendGrowthRate 6% +
# PEratio [15, 20]
# PBratio [1, 3]
# Return on equity
# Earnings Per Share
# Earnings Per Share Growth
# EBITDA
# Dividend Payout Ratio
# Free Cash flow
# BUFFET AAPLx47.8% BACx10.6% KOx8.6% AXPx6.6% KHCx4.3% CHTRx1.4% DVAx1.4%
#YCBD GRWG FSZ AMZN WELL WCN WMT MWK CP COST KO AMT MA AMD BAC NVDA
#KL WCN OTEX AQN TFII CP CNI LMT RY BRK-B GNW OTEX BPY LMT STOR GME SNE HD
#BCE, ZWB, CM, KEY, VNR, ENB, PPL, SJR.B, NPI, AQN FTS NPI
#ETFs:ARKK TEC.TO, VFV and ACES XEI ARKF QQC-f ZQQ XIT HQU SOXL HZU JNUG FIE BRTXQ
#CCA CGO RCI.B
#DLR VZ ABBV JPM STOR
# Canadian Dividend Aristocrat List from SnP Global
# Canadian Dividend All-Star List
# David Fish's CCC List
# growth portfolio= ETFs & blue chips
# income portfolio= Tx34 IBMx8 ABBVx12 GMx30 Fx126 IRMx30 MPWx60 AGNCx57 PSECx149 MAINx27
# ETSY ESTC VYM - VGT - VTI - VPU / ARKK ARKG ARKQ ARKW
# BND-- <= VXUS- <= BNDX-- <= VNQ- <= VBK <= VYM <= VPU <= VOT ~ VTI <= VIG <= MGK ~ VOO ~ VOOG
# VYM VTSAX/ SWTSX/ FZROX index vs. VTI/ SCHB ETF, VFIAX/ SWPPX/ VXAIX index vs. VOO/ SCHX
# FZROX/ VTSAX FZILX/ VTI FSRNX/ VNQ
# [NFLX, NKE, AMZN] [MRNA, MSFT, CAT] [T, XOM, MO]
# 60% StockMarketFund (FZROX~SWTSX~VTSAX) 20% InternationalFund (FZILX~SWISX~VTIAX) 20% REITFund (FSRNX)
# Sector ETFs: VGT VPU VDC VYM
# Sector Int'l: T (55*30.21$) IBM (14*126.66$) ABBV (21*82.79$) GM (46*35.24$) F (186*8.78$)
# IRM (52*33.48$) MPW (93*17.34$) AGNC (93*17.17$) PSEC (245*6.67$) MAIN (41*37.95$) VYMI (5*59.21$)
# MWK YCBD GRWG FSZ AMZN CGO RCI PPL SJR.B AQN CP CNI TD KL WCN BPY OTEX
# BCE ZWB CM KEY VNR ENB TFII LMT WMT RY BRKB GNW IT
# ETFs: BRTXQ FZILX FSRNX VTSAX FPE HPI DYNF SPGI RSP
# ETFs volat: VCAR VPOP
# ETFs Diversity: XIC.TO+0.8 XIU.TO+0.8 XIT.TO+1.7 XUU.TO+1.0 XAW.TO+0.9
# TFII LSPD T FTS RY SHOP
# ETFs to buy bubble: QQQ HXQ.TO ARKK ARKF HERO.TO CYBR.TO PYPL CRSR TRUL.CN TDOC ZG FB TTCF
# # Top REIT ETFs
# ZRE.TO XRE.TO RIT.TO VNQ MORT
# # High Yield Dividend ETFs Passive income
# HAL.TO ZDV.TO CDZ.TO XEI.TO XDV.TO H.TO EMA.TO ZEB.TO ZWB.TO CIC.TO
# # growth stocks
# BCE.TO BIP-UN.TO BIP BEP
# # Retire early dividends
# PEP JNJ RY
# # passive TSX
# BCE.TO MG.TO SIS.TO IFC.TO AP-UN.TO MFC.TO POW.TO QSR.TO FSV.TO TIH.TO BAM-A.TO TRP.TO
# # speculate
# CSC.TO CPH.TO WME.TO
# # easy portfolio
# 10% -> VAB.TO VGV.TO
# 90% -> 25% VFV XUS 20% HXQ XQQ 5-10% XEC 25% XRE XDV 20% ARKK ARKG
# # covered call ETFs
# ZWB.TO ZWU.TO ZWC.TO
# AAPL+3 ABBV+1.2 AAOI+0.4 ADBE+3.1 ABR+1.8 ABT+1.7 ABX.TO&GOLD+0.8 ACES+2.8 ADC+1.1 ADP+1.1 AGNC+0.8 AKAM+1.3 AMGN+0.9
# AMD+21.7 AM+0.3 AMP+1.5 AMT+1.5 AMAT+3.2 A+1.8 AA+0.5 AY+1.5 API+1.0 AMCX+0.6
# AMZN+3 ANTM+ AQN&TO+1.2 ARKK+3.8 ARKF++ ARKG+ ARKQ ARKW++++ APPS+++ APPN+5 AVGO++ APHA+ ASAN ARKF+1.8 ARKK AVAV
# AVGO++ AVB AYX+3.3 AZN AWK+ ANET+2.5 AEM&TO+ AES+1.5 AT.TO ATZ.TO. ARKG+ ACO-X.TO! ACN++ AIVSX+ AMC. ATVI+1.5 AXP+ AON+
# BA BE+0.9 BCE BCE.TO. BNS BPY BABA+1.7 BIDU- BBBY BNTX BRK-B+ BRTXQ BYND BNS.TO. BIP+1.4 BEP+2.5 BIP-UN.TO+1.5 BZUN+ BILI++ BEP+
# BYND+ BAM-A.TO+ BMO.TO. BTI- BMY- BGS. BAND+6.2 BP+0.5 BX+1.8 BMBL+1.0
# CAG CAT CCA&TO. CAR.UN.TO CGNX CGO CGO.TO. CHD CHWY CL. CLX+ CM CNI CDZ.TO CSU.TO CSX CVD CMCSA COST+1.5 CP CSCO+
# CDNS+3.5 CNQ.TO. CSIQ+1.5 CELH+ CM+ CMI+1.5 CPX.TO+1.5 CVA. CLH+ COLL. COUP+4.6 CRM+1.5 CHTR+2 CDW+2 CCI+1.1 CCIV+1.5 CMS+
# CNR.TO+ CU.TO. CSU.TO++ CTC-A.TO+ CLR.TO. CRWD++ CARR++ CB- CU.TO. CRSP+5.2 CRSR+2.1 C. CLNE. CMCSA+ CIBR+ CVX+0.7 CYBR.TO+1.6
# CSH-UN.TO+0.5 CNQ&TO+0.8 CSIQ+1.0 CRUS+1.1 CWEN+1.4
# DASH+0.7 DCBO.TO DND.TO DHIL+0.6 DLHC DKNG+5.6 DDOG+1.7 DOC+0.7 DOL.TO+ DND.TO+ DIS+ DHR+++ DTE+ DE++ DOCU+3.8 DVN.
# DAL. DLR+ DTE+ DOC.V+2 DYNF+1.0 DLR+1.0
# EMR+ ENB&TO. ESS ESTC+ ESPO EMA.TO EMQQ+2 ED+0.6 EL+1.5 ETSY+10 ENGH.TO+ ENPH+25 EEM EQB.TO+ ELY+ ESS- EPD+ EB. ET.
# EBAY+ ET+0.9
# F+0.6 FD.TO FF.TO FDN+1.5 FFMG FENY FIE FIS+ FIVG+ FSR+2.4 FSLR FSLY+2.0 FSRNX FSZ FTS+ FTS.TO+ FOOD.TO FZILX FZROX FVRR+4.1 FXAIX FEYE.
# FTEC+2 FAST+1.5 FB+1.5 FRC+ FRO. FROG. FRT. FCEL. FCX+3
# GE+0.3 GD+0.7 GM+1.0 GME+2.5 GMF+1.1 GFI+1.1 GIS+0.6 GLD+0.7 GLW+1.2 GNW+0.7 GRWG+6.1 GILD+0.4 GBTC+36.9 GAMR+2.0 GSK+0.6 GSY.TO+3.6
# GOOD+1.0 GXC+1.2 GOOG+1.5 GOOGL+1.4 GGG+1.5
# HD+ HLT HQU HZU HEO.V HII. HLF.TO. HUBS+3 HRL. HTA. HIW. HACK++ HRL. HXQ.TO+1.6 HCLN.TO+0.9 HERO.TO+1.5 HASI+2.3 HTOO+0.7
# IBUY+2.5 IWFH+1.25 INTC+ INE.TO+1.3 INTU+2 IPO+2 IIVI+2.5 IIPR+12 INVH+ IVAC+0.8 IGV+2 IBM+0.8 IRM+ IT+ IPFF. IYW+2
# IWM +1.1 IWY+1.5 ICLN+1.5 IVR+0.3 IEP+0.8 IXN+1.7 INSG+2.9
# JKS+0.9 JD+1.8 JNJ+0.9 JPM+1.5 JNUG+0.0 JNPR+0.6 JBHT+1.0 JKK+1.3
# KEY K KXS.TO KDP KL&TO KO! KR KMI. K.TO++ KXS.TO+ KHC. KWEB+1.5
# LB.TO+0.4 LMT+0.9 LNT+0.8 LOW+1.4 LSPD&TO+2 LOGI+3.9 LAND+1.3 LMND+1.7 LULU+2.7 LUV+0.7 LW+1.25 LLY+1.5
# M+0.5 MA+2 MAIN+0.8 MET+0.8 MELI+10 MFI.TO+0.6 MILN+1.4 MO+0.5 MU+3 MCD+ MGM MRVL MSFT+2.5 MWK+2 MDY+ MRU.TO+ MSCI+ MFC.TO+0.8 MXIM+
# MDLZ. MDB+6 MAA. MTUM+ NWC.TO. MGNI+ MLPX+0.5 MPW+1.5 MRK+ MARA+0.5 MRNA+4 MFC.TO+0.8 MG.TO+ MOGO+1.8 MSTR+3.3 MAC+0.1 MC-
# MPLX+0.7
# NEE+1.5 NEM+1.2 NEP+1.7 NET+3.5 NKE+1.2 NSP+1.9 NEAR+0.5 NFLX+2.9 NIO+6.2 NLY+0.7 NLOK NNDM NPI NOBL+ NVEI.TO NVDA+8.2
# NOW+4.4 NRZ+0.8 NUSI+1.0 NTST+0.9 NXST+1.5 NWC.TO+0.7
# O+0.6 OTEX+1 OHI+0.9 OKTA+6.9 OKE+1.4 OCGN+0.1
# PANW+1.6 PAAS+1.9 PAWZ+1.4 PAYC+8.5 PBI+0.4 PBA+0.8 PBW+3.6 PBH+0.4 PCTY+3.7 PEP+0.8 PFE+0.7 PDD+5.4 PG+0.9 PGX+0.6 PHM+1.6
# PHO+1.2 PINS+2.5 PIODX+0.6 PLAN+2.4 PLTR+2.2 PLTK+0.8 PM+0.6 PNC+1.1 PNR+0.9 POW.TO+0.8 PPL.TO+0.7 PRU+0.7 PSEC+1
# PTON+4.4 PTGX+1.1 PYPL+4.1 PKI.TO+1.2 PLUG+12.9 PNW+0.7
# QCOM+2 QQC-f QQQ+1.5 QQQJ++ QRVO+2.5 QSR.TO+ QTEC+2
# RBA RCI+ RCI.B.TO+ REAL.TO RCL.S REGI+7.5 ROK+1.5 ROKU+9.8 ROP+1.5 RUN+5 RY+ RY.TO+ RYT+1.5 RIOT RHS RNG+9 RF+ RNW.TO++
# RSG+1.0 RTX+0.7 RSP+1.0 RZG+1.0
# SU&TO. SEM+1.6 SFM+0.4 SIS.TO+ SNA SBUX+ SHOP&TO+22.8 SPLK SPYD SJR.B SJR-B.TO SLV+0.8 SNAP+1.6 SNOW+0.8 SPOT SOXL SRU.UN.TO. SPG SAP SPGI+1.9
# SPNS+1.6 SNPS+3.0 STOR+0.8 STAG+1.3 SEDG+6.7 SJR-B.TO+0.6 SOY.TO+1.3 SYK+1.3 STX+1.5 SQ+13.7 SFTBY+2.2 SAVA+2.1 SMOG+1.9 SE+9.5
# SCHA+1.1 SCHW+1.3 STN&TO+0.9 SPGI+2 SLYG+1.1
# T&TO+0.5 TAL+5.1 TD+0.9 TCOM+0.4 TDOC+10.8 TEC.TO+1.3 TEAM+6.5 TENB+1.1 TFII&TO+2.7 TGT+1.5 TJX+1 TMO+2 TOU.TO+0.4 TPB+2.9 TPR+0.6
# TRMB+1.8 TRP&TO+0.7 TRIT+0.5 TRUL.CN+4 TROW+1.3 TSLA+13.8 TSN+0.6 TSM+3.2 TTCF+1.9 TTD+15.8 TVE.TO+0.2 TWLO+7.6
# TWST+7.9 TWTR+1.8 TWOU+0.9 TXN+1.8 TCL-A.TO+0.7 TLRY+0.8
# U+1.5 UNM+0.5 UNP+1.5 UPWK+1.2 UNM+0.5 UDN+0.5 UL+0.7
# V+1.5 VDC+0.7 VEEV+6.9 VEQT.TO+0.8 VFC+0.8 VFF+1.2 VFV.TO+1.0 VG+1.5 VGT+2.0 VGRO.TO+0.9 VHT+1.0 VIOO+1.1 VITAX+2.0 VMW+1.7
# VNRT.L+0.9 VNQ+0.7 VOO+1.1 VOOG+1.3 VPL+0.9 VPU+0.8 VRTX+1.3 VSP.TO+1.0 VTI+1.1 VTV+0.9 VTWG+1.2 VTSAX+1.2 VYM+0.9 VYMI+0.8 VZ+0.7
# W+4.2 WCN&TO+1.2 WELL.TO+225.9 WEED.TO+7.5 WISH+0.9 WM+1.1 WMT+1.1 WORK+0.8 WPC+0.8 WPM+1.5 WBA+0.3 WKHS+1.7
# XEI.TO. XIT.TO+1.7 XBC.TO XOM. XWEB+ XLC+ XLK+2 XBC.V+++ XTC.TO. ZS++ XBUY+1.5
# YCBD+0.5
# ZG+3.5 ZM+4.7 ZIM+1.7 ZQQ.TO+1.5 ZS+4.4 ZWB.TO+0.8 ZUO+0.6 ZTS+1.9 ZEN+3.4
# AYX+4 PLAN+1.5 ASAN+ DDOG+1.5 DT+ FOUR++ FROG. MDLA+ NTNX. PEGA+3 PSTG+ SMAR++ WDAY++
# Yield on Cost MANULIFE ~ 25$ x 100000 = 2500000$ invest
# 1.09$ per share/ year => 109000$/ year ROI
yahooStockOption: YahooStockOption = YahooStockOption('COUP')#'ESTC')XWEB DDOG BEKE GBTC IHI GC=F JPY=X JPY=X ^TNX BTC-USD BTCC-B.TO
#exit(-11)
sAnP500: AbstractStockMarketIndex = SnP500Index('yahoo', "^GSPC", yahooStockOption.TimeSpan)
vixIndex: AbstractStockMarketIndex = VixIndex('yahoo', "^VIX", yahooStockOption.TimeSpan)
skewIndex: AbstractStockMarketIndex = SkewIndex('yahoo', "^SKEW", yahooStockOption.TimeSpan)
#''' #ovxIndex: AbstractStockMarketIndex = OvxIndex('yahoo', "^OVX", yahooStockOption.TimeSpan)
sAndPTsx: AbstractStockMarketIndex = SnPTSXComposite('yahoo', "^GSPTSE", yahooStockOption.TimeSpan)
nasdaqIndex: AbstractStockMarketIndex = NasdaqIndex('yahoo', "^IXIC", yahooStockOption.TimeSpan)
nasdaq100Index: AbstractStockMarketIndex = Nasdaq100Index('yahoo', "^NDX", yahooStockOption.TimeSpan)
nyseIndex: AbstractStockMarketIndex = NyseIndex('yahoo', "^NYA", yahooStockOption.TimeSpan)
dowJonesIndex: AbstractStockMarketIndex = DowJonesIndex('yahoo', "^DJI", yahooStockOption.TimeSpan)
goldIndex: AbstractStockMarketIndex = GoldIndex('yahoo', "GC=F", yahooStockOption.TimeSpan)
silverIndex: AbstractStockMarketIndex = SilverIndex('yahoo', "SI=F", yahooStockOption.TimeSpan)
crudeOilIndex: AbstractStockMarketIndex = CrudeOilIndex('yahoo', "CL=F", yahooStockOption.TimeSpan)
#bitcoinIndex: AbstractStockMarketIndex = BitcoinIndex('yahoo', "BTC-USD", yahooStockOption.TimeSpan)
soxIndex: AbstractStockMarketIndex = SoxIndex('yahoo', "^SOX", yahooStockOption.TimeSpan)
tnxIndex: AbstractStockMarketIndex = TnxIndex('yahoo', "^TNX", yahooStockOption.TimeSpan)
tyxIndex: AbstractStockMarketIndex = TyxIndex('yahoo', "^TYX", yahooStockOption.TimeSpan)
fvxIndex: AbstractStockMarketIndex = FvxIndex('yahoo', "^FVX", yahooStockOption.TimeSpan)
irxIndex: AbstractStockMarketIndex = TreasuryBill13Index('yahoo', "^IRX", yahooStockOption.TimeSpan)
wilshire5kIndex: AbstractStockMarketIndex = Wilshire5kIndex('yahoo', "^W5000", yahooStockOption.TimeSpan)
#vix3mIndex: AbstractStockMarketIndex = Vix3mIndex('yahoo', "^VIX3M", yahooStockOption.TimeSpan)
#euroNext100Index: AbstractStockMarketIndex = EuroNext100Index('yahoo', "^N100", yahooStockOption.TimeSpan)
#estx50Index: AbstractStockMarketIndex = Estx50Index('yahoo', "^N100", yahooStockOption.TimeSpan)
#daxIndex: AbstractStockMarketIndex = DaxIndex('yahoo', "^GDAXI", yahooStockOption.TimeSpan)
#nikkei225Index: AbstractStockMarketIndex = Nikkei225Index('yahoo', "^N225", yahooStockOption.TimeSpan)
#moexRussiaIndex: AbstractStockMarketIndex = MoexRussiaIndex('yahoo', "IMOEX.ME", yahooStockOption.TimeSpan)
#hangSengIndex: AbstractStockMarketIndex = HangSengIndex('yahoo', "^HSI", yahooStockOption.TimeSpan)
#shenzhenComponentIndex: AbstractStockMarketIndex = ShenzhenComponentIndex('yahoo', "399001.SZ", yahooStockOption.TimeSpan)
#nifty50Index: AbstractStockMarketIndex = NseIndex('yahoo', "^NSEI", yahooStockOption.TimeSpan)
#bovespaIndex: AbstractStockMarketIndex = BovespaIndex('yahoo', "^BVSP", yahooStockOption.TimeSpan)
#ipcMexicoIndex: AbstractStockMarketIndex = IpcMexicoIndex('yahoo', "^MXX", yahooStockOption.TimeSpan)
#ipsaIndex: AbstractStockMarketIndex = IpsaIndex('yahoo', "^IPSA", yahooStockOption.TimeSpan)
#jkseIndex: AbstractStockMarketIndex = JkseIndex('yahoo', "^JKSE", yahooStockOption.TimeSpan)
#kospIndex: AbstractStockMarketIndex = KospIndex('yahoo', "^KS11", yahooStockOption.TimeSpan)
marketIndices = list()
marketIndices.append(sAnP500)
marketIndices.append(vixIndex)
marketIndices.append(skewIndex)
#marketIndices.append(ovxIndex)
marketIndices.append(sAndPTsx)
marketIndices.append(nasdaqIndex)
marketIndices.append(nasdaq100Index)
marketIndices.append(nyseIndex)
marketIndices.append(dowJonesIndex)
marketIndices.append(goldIndex)
marketIndices.append(silverIndex)
marketIndices.append(crudeOilIndex)
#marketIndices.append(bitcoinIndex)
marketIndices.append(soxIndex)
marketIndices.append(tnxIndex)
marketIndices.append(tyxIndex)
marketIndices.append(irxIndex)
marketIndices.append(fvxIndex)
marketIndices.append(wilshire5kIndex)
#marketIndices.append(vix3mIndex)
#marketIndices.append(euroNext100Index)
#marketIndices.append(estx50Index)
#marketIndices.append(daxIndex)
#marketIndices.append(nikkei225Index)
#marketIndices.append(moexRussiaIndex)
#marketIndices.append(hangSengIndex)
#marketIndices.append(shenzhenComponentIndex)
#marketIndices.append(nifty50Index)
#marketIndices.append(bovespaIndex)
#marketIndices.append(ipcMexicoIndex)
#marketIndices.append(ipsaIndex)
#marketIndices.append(jkseIndex)
#marketIndices.append(kospIndex)
yahooStockOption.SetSnpRatio(sAnP500.DataNorm, 'S&P500Norm')
print(yahooStockOption.SnpRatio)
#exit(-111)
indexComparator: IndexComparator = IndexComparator(yahooStockOption, marketIndices)
#'''
exit(-1111)#
yahooStockOptionPlotter: HistoricalPlotter = HistoricalPlotter(yahooStockOption, vixIndex, sAnP500)
yahooStockOptionPlotter.RadarPlot().show()
#exit(-11111)#
#yahooStockOptionPlotter.SnP500Plot().show()
yahooStockOptionPlotter.GraphPlot().show()
yahooStockOptionPlotter.Plot().show()#snp_ratio
#yahooStockOptionPlotter.PlotTimely()
#exit(-111111)#
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
#yahooStockOptionPlotter.RsiInd.PlotData().show()
#yahooEmaStrategy: RsiStrategy = yahooStockOptionPlotter.RsiStrat #RsiStrategy(yahooEmaIndicator)
yahooStockOptionPlotter.RsiStrat.PlotAll().show()
#***
yahooStockOptionPlotter.IndicatorPlot().show()
yahooStockOptionPlotter.StrategyPlot().show()
# preprocessing
## Mean removal
print('MEAN=', yahooStockOption.Data.Sparse.mean(axis=0))
print('SD=', yahooStockOption.Data.Sparse.std(axis=0))
# classification by classes
# viz
## uni variate
