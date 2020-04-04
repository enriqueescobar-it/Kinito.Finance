#!/usr/bin/env python
# coding: utf-8
# ## Calculating the Return of a Portfolio of Securities
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Download data for a portfolio composed of 5 stocks. Do it for British Petroleum, Ford, Exxon, Lincoln, and Apple for the period ‘2000-1-1’ until today.
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
# In[2]:
tickers = ['BP', 'F', 'XOM', 'LNC', 'AAPL']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='2000-1-1')['Adj Close']
# In[3]:
mydata.info()
# In[4]:
mydata.head()
# In[5]:
mydata.tail()
# ### Normalization to 100:
# 
# $$
# \frac {P_t}{P_0} * 100
# $$
# Normalize to a hundred and plot the data on a graph (you can apply the .loc() or the .iloc() method). 
# In[6]:
mydata.iloc[0]
# In[7]:
(mydata / mydata.iloc[0] * 100).plot(figsize = (15, 6));
plt.show()
# How would you interpret the behavior of the stocks? Just by looking at the chart, would you be able to create a portfolio that provides a solid return on investment?
# *****
# ### Calculating the Return of a Portfolio of Securities
# Obtain the simple return of the securities in the portfolio and store the results in a new table.
# In[8]:
returns = (mydata / mydata.shift(1)) - 1
returns.head()
# First, assume you would like to create an equally-weighted portfolio. Create the array, naming it “weights”.
# In[9]:
weights = np.array([0.20, 0.20, 0.20, 0.20, 0.20])
# Obtain the annual returns of each of the stocks and then calculate the dot product of these returns and the weights.
# In[10]:
annual_returns = returns.mean() * 250
annual_returns
# In[11]:
np.dot(annual_returns, weights)
# Transform the result into a percentage form. 
# In[12]:
pfolio_1 = str(round(np.dot(annual_returns, weights), 5) * 100) + ' %'
print (pfolio_1)
# Is the return of this portfolio satisfactory?
