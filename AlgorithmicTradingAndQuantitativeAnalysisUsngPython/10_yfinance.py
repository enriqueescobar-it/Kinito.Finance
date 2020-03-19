import pandas as pd
from yahoofinancials import YahooFinancials
import datetime

all_tickers = ["AAPL","MSFT","CSCO","AMZN","INTC"]
# extracting stock data (historical close price) for the stocks identified
all_dataframe = pd.DataFrame()
beg_date = (datetime.date.today()-datetime.timedelta(365)).strftime('%Y-%m-%d')
print(beg_date)
end_date = (datetime.date.today()).strftime('%Y-%m-%d')
print(end_date)
new_tickers = all_tickers
attempt = 0
drop_list = []
while len(new_tickers) != 0 and attempt <=5:
    print("-----------------")
    print("attempt number ",attempt)
    print("-----------------")
    new_tickers = [j for j in new_tickers if j not in drop_list]
    for i in range(len(new_tickers)):
        try:
            new_financial = YahooFinancials(new_tickers[i])
            print(type(new_financial.get_historical_stock_data(beg_date,end_date,"daily")))
            new_json = new_financial.get_historical_stock_data(beg_date,end_date,"daily")
            new_json_field = new_json[new_tickers[i]]['prices']
            new_dataframe = pd.DataFrame(new_json_field)[["formatted_date","adjclose"]]
            new_dataframe.set_index("formatted_date",inplace=True)
            first_dataframe = new_dataframe[~new_dataframe.index.duplicated(keep='first')]
            all_dataframe[new_tickers[i]] = first_dataframe["adjclose"]
            drop_list.append(new_tickers[i])   
        except:
            print(new_tickers[i]," :failed to fetch data...retrying")
            continue
    attempt+=1