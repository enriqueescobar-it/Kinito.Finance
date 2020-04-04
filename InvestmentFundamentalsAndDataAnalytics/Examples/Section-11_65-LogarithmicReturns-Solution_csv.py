#!/usr/bin/env python
# coding: utf-8
# ## Logarithmic Returns
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
MSFT = pd.read_csv('D:/Python/MSFT_2000_2017.csv', index_col = 'Date')
MSFT
# ### Log Returns
# $$
# ln(\frac{P_t}{P_{t-1}})
# $$
# In[2]:
MSFT.head()
# Calculate the Log returns for Microsoft.
# In[3]:
MSFT['log_return'] = np.log(MSFT['Adj Close'] / MSFT['Adj Close'].shift(1))
print (MSFT['log_return'])
# Plot the results on a graph.
# In[4]:
MSFT['log_return'].plot(figsize=(8, 5))
plt.show()
# Estimate the daily and the annual mean of the obtained log returns.
# In[5]:
log_return_d = MSFT['log_return'].mean()
log_return_d
# In[6]:
log_return_a = MSFT['log_return'].mean() * 250
log_return_a
# Print the result in a presentable form.
# In[7]:
print (str(round(log_return_a, 5) * 100) + ' %')
# ****
# Repeat this exercise for any stock of interest to you. :)
