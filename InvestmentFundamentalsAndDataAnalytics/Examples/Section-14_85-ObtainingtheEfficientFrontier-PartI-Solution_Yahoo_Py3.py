#!/usr/bin/env python
# coding: utf-8
# ## Obtaining the Efficient Frontier - Part I
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# We are in the middle of a set of 3 Python lectures that will help you reproduce the Markowitz Efficient Frontier. Let’s split this exercise into 3 parts and cover the first part here. 
# Begin by extracting data for Walmart and Facebook from the 1st of January 2014 until today.
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
assets = ['WMT', 'FB']
pf_data = pd.DataFrame()
for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2014-1-1')['Adj Close']
# Do a quick check of the data, normalize it to 100, and see how the 2 stocks were doing during the given timeframe. 
# In[2]:
pf_data.tail()
# In[3]:
(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))
# Calculate their logarithmic returns.
# In[4]:
log_returns = np.log(pf_data / pf_data.shift(1))
# Create a variable that carries the number of assets in your portfolio.
# In[5]:
num_assets = len(assets)
# In[6]:
num_assets
# The portfolio need not be equally weighted. So, create a variable, called “weights”. Let it contain as many randomly generated values as there are assets in your portfolio. Don’t forget these values should be neither smaller than 0 nor equal or greater than 1! <br />
# 
# *Hint: There is a specific NumPy function that allows you to generate such values. It is the one we used in the lecture - NumPy.random.random().*
# In[7]:
weights = np.random.random(num_assets)
weights /= np.sum(weights)
weights
# Sum the obtained values to obtain 1 – summing up the weights to 100%!
# In[8]:
weights[0] + weights[1]
# *****
# Save this document! The next 2 exercises will build on the code you just created!
