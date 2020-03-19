import pandas as pd
import pandas_datareader.data as pdr
import datetime

# Download historical data for NIFTY constituent stocks
all_tickers = ["ASIANPAINT.NS","ADANIPORTS.NS","AXISBANK.NS","BAJAJ-AUTO.NS",
           "BAJFINANCE.NS","BAJAJFINSV.NS","BPCL.NS","BHARTIARTL.NS",
           "INFRATEL.NS","CIPLA.NS","COALINDIA.NS","DRREDDY.NS","EICHERMOT.NS",
           "GAIL.NS","GRASIM.NS","HCLTECH.NS","HDFCBANK.NS","HEROMOTOCO.NS",
           "HINDALCO.NS","HINDPETRO.NS","HINDUNILVR.NS","HDFC.NS","ITC.NS",
           "ICICIBANK.NS","IBULHSGFIN.NS","IOC.NS","INDUSINDBK.NS","INFY.NS",
           "KOTAKBANK.NS","LT.NS","LUPIN.NS","M&M.NS","MARUTI.NS","NTPC.NS",
           "ONGC.NS","POWERGRID.NS","RELIANCE.NS","SBIN.NS","SUNPHARMA.NS",
           "TCS.NS","TATAMOTORS.NS","TATASTEEL.NS","TECHM.NS","TITAN.NS",
           "UPL.NS","ULTRACEMCO.NS","VEDL.NS","WIPRO.NS","YESBANK.NS","ZEEL.NS"]
ticker_dataframe = pd.DataFrame() # dataframe to store close price of each ticker
attempt = 0 # initializing passthrough variable
drop_list = [] # initializing list to store tickers whose close price was successfully extracted
while len(all_tickers) != 0 and attempt <= 5:
    all_tickers = [j for j in all_tickers if j not in drop_list] # removing stocks whose data has been extracted from the ticker list
    for i in range(len(all_tickers)):
        try:
            data_f = pdr.get_data_yahoo(all_tickers[i],datetime.date.today()-datetime.timedelta(365),datetime.date.today())
            data_f.dropna(inplace = True)
            ticker_dataframe[all_tickers[i]] = data_f["Adj Close"]
            drop_list.append(all_tickers[i])       
        except:
            print(all_tickers[i]," :failed to fetch data...retrying")
            continue
    attempt+=1
print(ticker_dataframe)