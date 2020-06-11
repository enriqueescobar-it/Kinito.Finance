from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print("Source_fv: FinViz")
print("Name_fv:", yahooStockOption.FvCompanyName)
print("Sector_fv:", yahooStockOption.FvCompanySector)
print("Industry_fv:", yahooStockOption.FvCompanyIndustry)
print("Country_fv:", yahooStockOption.FvCompanyCountry)
print("ChangePercent_fv:", yahooStockOption.FvChangePercent)
print("Beta_fv:", yahooStockOption.FvBeta)
print("Dividend_fv:", yahooStockOption.FvDividend)
print("Dividend%_fv:", yahooStockOption.FvDividendPercent)
print("EPS_fv:", yahooStockOption.FvEPS)
print("EarningsDate_fv:", yahooStockOption.FvEarnings)
print("High2_fv:", yahooStockOption.FvHigh52)
print("Low52_fv:", yahooStockOption.FvLow52)
print("MarketCap_fv:", yahooStockOption.FvMarketCap)
print("Payout_fv:", yahooStockOption.FvPayout)
print("PeRatio_fv:", yahooStockOption.FvPeRatio)
print("Price_fv:", yahooStockOption.FvPrice)
print("Range52_fv:", yahooStockOption.FvRange52)
print("Rsi14_fv:", yahooStockOption.FvRsi14)
print("Volatility_fv:", yahooStockOption.FvVolatility)
print("Volume_fv:", yahooStockOption.FvVolume)
print("Url_ye:", yahooStockOption.YeUrl)
print("LogoUrl_ye:", yahooStockOption.YeLogoUrl)
print("Address_ye:", yahooStockOption.YeAddress)
print("City_ye:", yahooStockOption.YeCity)
print("State_ye:", yahooStockOption.YeState)
print("PostalCode_ye:", yahooStockOption.YePostalCode)
print("Country_ye:", yahooStockOption.YeCountry)
print("Beta_ye:", yahooStockOption.YeBeta)
print("Market_ye:", yahooStockOption.YeMarket)
print("Exchange_ye:", yahooStockOption.YeExchange)
print("Currency_ye:", yahooStockOption.YeCurrency)
print("QuoteType_ye:", yahooStockOption.YeQuoteType)
print("52WeekHigh_ye:", yahooStockOption.YeHigh52)
print("52WeekLow_ye:", yahooStockOption.YeLow52)
print("50DayAverage_ye:", yahooStockOption.YeAverage50)
print("200DayAverage_ye:", yahooStockOption.YeAverage200)
print("MarketCap_ye:", yahooStockOption.YeMarketCap)
print("PayoutRatio_ye:", yahooStockOption.YePayoutRatio)
print("PeForward_ye:", yahooStockOption.YePeForward)
print("PeTrailing_ye:", yahooStockOption.YePeTrailing)
print("PegRatio_ye:", yahooStockOption.YePegRatio)
print("ShortRatio_ye:", yahooStockOption.YeShortRatio)
print("BookValue_ye:", yahooStockOption.YeBookValue)
print("PriceToBook_ye:", yahooStockOption.YePriceToBook)
print("ExDividendDate_ye:", yahooStockOption.YeExDividendDate)
print("Ticker:", yahooStockOption.Ticker)
print("Link_yss:", yahooStockOption.YssLink)
print("MarketCap_yss:", yahooStockOption.YssMarketCap)
print("Beta_yss:", yahooStockOption.YssBeta)
print("PEratio_yss:", yahooStockOption.YssPeRatio)
print("EPS_yss:", yahooStockOption.YssEPS)
print("EarningsDate_yss:", yahooStockOption.YssEarningsDate)
print(yahooStockOption.HistoricalData.describe(include='all'))
