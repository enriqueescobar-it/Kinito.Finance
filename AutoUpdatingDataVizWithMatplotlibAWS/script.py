import boto3
import pandas as pd
import matplotlib.pyplot as plt


def getIexKey():
    return 'pk_5cd7b4d3ee8e45eca04095fda2cddbda'


def getTickerList():
    return [
        'JPM',
        'BAC',
        'C',
        'WFC',
        'GS',
    ]


def getTickerListFlatten(tickerList: []):
    # Create an empty string called `ticker_string` that we'll add tickerList and commas to
    s = ''
    # Loop through every element of `tickerList` and add them and a comma to ticker_string
    for tickerElement in tickerList:
        s += tickerElement
        s += ','
    # Drop the last comma from `ticker_string`
    s = s[:-1]
    return s


def getHttpRequestString(ticker_string, endpoints, years, IEX_API_Key):
    # Interpolate the endpoint strings into the HTTP_request string
    return f'https://cloud.iexapis.com/stable/stock/market/batch?symbols={ticker_string}&types={endpoints}&range={years}y&cache=true&token={IEX_API_Key}'


def getSeriesList(bank_data, tickers: []):
    # Create an empty list that we will append pandas Series of stock price data into
    seriesList = []
    # Loop through each of our tickerList and parse a pandas Series of their closing prices over the last 5 years
    for tickerElement in tickers:
        seriesList.append(pd.DataFrame(bank_data[tickerElement]['chart'])['close'])
    # Add in a column of dates
    seriesList.append(pd.DataFrame(bank_data['JPM']['chart'])['date'])
    return seriesList


IEX_API_Key = getIexKey()
tickers = getTickerList()
ticker_string = getTickerListFlatten(tickers)
portfolioName = 'bank_data'
portfolioFile = portfolioName + '.png'
# Create the endpoint and years strings
endpoints = 'chart'
years = '5'
HTTP_request = getHttpRequestString(ticker_string), endpoints, years, IEX_API_Key
# Send the HTTP request to the IEX Cloud API and store the response in a pandas DataFrame
bank_data = pd.read_json(HTTP_request)
# Create an empty list that we will append pandas Series of stock price data into
series_list = getSeriesList(bank_data, tickers)
# Copy the 'tickerList' list from earlier in the script, and add a new element called 'Date'.
# These elements will be the column names of our pandas DataFrame later on.
column_names = tickers.copy()
column_names.append('Date')
# Concatenate the pandas Series together into a single DataFrame
bank_data = pd.concat(series_list, axis=1)
# Name the columns of the DataFrame and set the 'Date' column as the index
bank_data.columns = column_names
bank_data.set_index('Date', inplace=True)

########################
# Create a Python box plot
########################

# Set the size of the matplotlib canvas
plt.figure(figsize=(18, 12))

# Generate the box plot
plt.boxplot(bank_data.transpose())

# Add titles to the chart and axes
plt.title('Boxplot of Bank Stock Prices (5Y Lookback)', fontsize=20)
plt.xlabel('Bank', fontsize=20)
plt.ylabel('Stock Prices', fontsize=20)

# Add labels to each individual box plot on the canvas
ticks = range(1, len(bank_data.columns) + 1)
labels = list(bank_data.columns)
plt.xticks(ticks, labels, fontsize=20)

########################
# Create a Python scatter plot
########################

# Set the size of the matplotlib canvas
plt.figure(figsize=(18, 12))

# Create the x-axis data
dates = bank_data.index.to_series()
dates = [pd.to_datetime(d) for d in dates]

# Create the y-axis data
WFC_stock_prices = bank_data['WFC']

# Generate the scatter plot
plt.scatter(dates, WFC_stock_prices)

# Add titles to the chart and axes
plt.title("Wells Fargo Stock Price (5Y Lookback)", fontsize=20)
plt.ylabel("Stock Price", fontsize=20)
plt.xlabel("Date", fontsize=20)

########################
# Create a Python histogram
########################

# Set the size of the matplotlib canvas
plt.figure(figsize=(18, 12))

# Generate the histogram
plt.hist(bank_data.transpose(), bins=50)

# Add a legend to the histogram
plt.legend(bank_data.columns, fontsize=20)

# Add titles to the chart and axes
plt.title("A Histogram of Daily Closing Stock Prices for the 5 Largest Banks in the US (5Y Lookback)", fontsize=20)
plt.ylabel("Observations", fontsize=20)
plt.xlabel("Stock Prices", fontsize=20)

################################################
################################################
# Create subplots in Python
################################################
################################################

########################
# Subplot 1
########################
plt.subplot(2, 2, 1)

# Generate the box plot
plt.boxplot(bank_data.transpose())

# Add titles to the chart and axes
plt.title('Boxplot of Bank Stock Prices (5Y Lookback)')
plt.xlabel('Bank', fontsize=20)
plt.ylabel('Stock Prices')

# Add labels to each individual box plot on the canvas
ticks = range(1, len(bank_data.columns) + 1)
labels = list(bank_data.columns)
plt.xticks(ticks, labels)

########################
# Subplot 2
########################
plt.subplot(2, 2, 2)

# Create the x-axis data
dates = bank_data.index.to_series()
dates = [pd.to_datetime(d) for d in dates]

# Create the y-axis data
WFC_stock_prices = bank_data['WFC']

# Generate the scatter plot
plt.scatter(dates, WFC_stock_prices)

# Add titles to the chart and axes
plt.title("Wells Fargo Stock Price (5Y Lookback)")
plt.ylabel("Stock Price")
plt.xlabel("Date")

########################
# Subplot 3
########################
plt.subplot(2, 2, 3)

# Create the x-axis data
dates = bank_data.index.to_series()
dates = [pd.to_datetime(d) for d in dates]

# Create the y-axis data
BAC_stock_prices = bank_data['BAC']

# Generate the scatter plot
plt.scatter(dates, BAC_stock_prices)

# Add titles to the chart and axes
plt.title("Bank of America Stock Price (5Y Lookback)")
plt.ylabel("Stock Price")
plt.xlabel("Date")

########################
# Subplot 4
########################
plt.subplot(2, 2, 4)

# Generate the histogram
plt.hist(bank_data.transpose(), bins=50)

# Add a legend to the histogram
plt.legend(bank_data.columns, fontsize=20)

# Add titles to the chart and axes
plt.title("A Histogram of Daily Closing Stock Prices for the 5 Largest Banks in the US (5Y Lookback)")
plt.ylabel("Observations")
plt.xlabel("Stock Prices")

plt.tight_layout()

################################################
# Save the figure to our local machine
################################################

plt.savefig('bank_data.png')

################################################
# Push the file to the AWS S3 bucket
################################################

s3 = boto3.resource('s3')
s3.meta.client.upload_file('bank_data.png', 'kike-first-bucket', 'bank_data.png', ExtraArgs={'ACL': 'public-read'})
