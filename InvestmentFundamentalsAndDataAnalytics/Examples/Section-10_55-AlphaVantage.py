#!/usr/bin/env python
# coding: utf-8
# # Alpha Vantage
# ***
# There are multiple ways to import data from the 'Alpha Vantage' API. <br>
# As mentioned in the previous videos, requesting data from the 'Alpha Vantage' API is not the easiest option from a programmatic point of view. However, going through this IPython Notebook file will be a great exercise, especially if you feel confident enough about coding with Python or you are up for a challenge.
# First, you'll need to pip install the alpha-vantage module. Hence, open Anaconda Prompt and run **pip install alpha-vantage**.
# <br> <br>
# Then, you need to go to https://www.alphavantage.co/ and click on "Get Your Free API Key". Save it, as you will need to replace all "INSERT-YOUR-API-KEY-HERE" strings you see within the code presented in this document.
# Then, import the usual modules for retrieving and manipulating financial data in Python:
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
# From the module you just installed, you need to import **TimeSeries**. Hence, the following line of code will do the job.
# In[2]:
from alpha_vantage.timeseries import TimeSeries
# Then, with the following line, designate your API key, as well as the format in which you would like to retrieve the data. In our case, this will be the 'pandas' module.
# In[3]:
ts = TimeSeries(key = 'INSERT-YOUR-API-KEY-HERE', output_format='pandas')
# Finally, give a name to the new variable, containing the name of the stock and a suffix indicating the API we have retrieved the data from. <br>
# Next to this new variable, you need to give the name to "metadata", as it will be storing information about the dataset retrieved.
# Then, apply the **.get_daily_adjusted()** method to obtain the adjusted closing prices for the designated stock.
# In[4]:
PG_av, metadata = ts.get_daily_adjusted('PG', outputsize='full')
PG_av
# You can repeat the same exercise, using the tickers of other stocks, such as Apple, for instance ('AAPL').
# In[5]:
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key = 'BCCBVQOU6OFZMNOK', output_format='pandas')
AAPL_av, metadata = ts.get_daily_adjusted('AAPL', outputsize='full')
AAPL_av
# Apart from US stocks, you can retrieve data about foreign stocks (e.g. Beiersdorf, ticker: 'BEI.DE'), or market indices (e.g. Standard & Poor's, ticker: '^GSPC', or Dow Jones, ticker: '^DJI').
# In[6]:
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key = 'BCCBVQOU6OFZMNOK', output_format='pandas')
GSPC_av, metadata = ts.get_daily_adjusted('^GSPC', outputsize='full')
GSPC_av
# To combine specific columns from various stocks, one would need to *concatenate* the columns of interest by using the **.concat()** function to specify which columns you want to extract.
# In[7]:
pfolio_av = pd.concat([PG_av['5. adjusted close'], GSPC_av['5. adjusted close']], axis = 1)
pfolio_av
# Finally, use **.columns** and assign a list with the names of the columns should you wish to change them.
# In[8]:
pfolio_av.columns = ['PG', 'GSPC']
pfolio_av
