#!/usr/bin/env python
# coding: utf-8
# ## Importing and Organizing Your Data in Python - Part II
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# In[1]:
from pandas_datareader import data as wb
F = wb.DataReader('F', data_source='iex', start='2015-1-1')
F
# Use the “info” method to obtain basic statistics, regarding the data you extracted in the previous exercise (data from Morningstar for Ford starting from the 1st of January 2005 until today). 
# In[2]:
F.info()
# Apply the “head” and “tail” methods and observe the output. How would you interpret the adjusted closing prices?
# In[3]:
F.head()
# In[4]:
F.tail()
# In[5]:
F.head(20)
# In[6]:
F.tail(20)
# Practice extracting closing price data from the same source and for the same timeframe. Do this for Apple, Microsoft, Exxon, and British Petroleum. 
# Use IEX to find the tickers of these companies, if you don’t already know them. 
# In[7]:
from pandas_datareader import data as wb
# In[8]:
import pandas as pd
# In[9]:
tickers = ['AAPL', 'MSFT', 'XOM', 'BP']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='iex', start='2015-1-1')['close']
# In[10]:
new_data.tail()
# In[11]:
new_data.head()
# *****
# Repeat this exercise for any stock of interest to you. :)
