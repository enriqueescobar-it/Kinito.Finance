#!/usr/bin/env python
# coding: utf-8
# ## Importing and Organizing Your Data in Python - Part II
# In[1]:
from pandas_datareader import data as wb
F = wb.DataReader('F', data_source='iex', start='2015-1-1')
F
# Use the “info” method to obtain basic statistics, regarding the data you extracted in the previous exercise (data from Morningstar for Ford starting from the 1st of January 2005 until today). 
# In[ ]:

# Apply the “head” and “tail” methods and observe the output. How would you interpret the adjusted closing prices?
# 
# In[ ]:

# In[ ]:

# Practice extracting closing price data from the same source and for the same timeframe. Do this for Apple, Microsoft, Exxon, and British Petroleum. 
# Use IEX to find the tickers of these companies, if you don’t already know them. 
# In[ ]:

# In[ ]:

# In[ ]:

# ***
# Repeat this exercise for any stock of interest to you. :)
