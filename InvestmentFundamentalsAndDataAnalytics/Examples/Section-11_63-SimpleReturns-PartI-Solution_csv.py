#!/usr/bin/env python
# coding: utf-8

# ## Simpler Returns - Part I

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Download the data for Microsoft (‘MSFT’) from Yahoo Finance for the period ‘2000-1-1’ until today.

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb


# In[2]:


MSFT = pd.read_csv('D:/Python/MSFT_2000_2017.csv', index_col = 'Date')


# Apply the .**head()** and **.tail()** methods to check if the data is ok. Always pay attention to the dates. Try to get an idea about how the stock price changed during the period.

# In[3]:


MSFT.head()


# In[4]:


MSFT.tail()


# ### Simple Rate of Return

# Calculate the simple returns of ‘MSFT’ for the given timeframe.

# $$
# \frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
# $$

# In[5]:


MSFT['simple_return'] = (MSFT['Adj Close'] / MSFT['Adj Close'].shift(1)) - 1
print (MSFT['simple_return'])

