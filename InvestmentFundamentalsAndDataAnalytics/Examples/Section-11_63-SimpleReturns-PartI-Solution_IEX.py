#!/usr/bin/env python
# coding: utf-8
# ## Simpler Returns - Part I
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Download the data for Microsoft (‘MSFT’) from IEX for the period ‘2015-1-1’ until today.
# In[1]:
import numpy as np
from pandas_datareader import data as wb
# In[2]:
MSFT = wb.DataReader('MSFT', data_source='iex', start='2015-1-1')
MSFT
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
MSFT['simple_return'] = (MSFT['close'] / MSFT['close'].shift(1)) - 1
print (MSFT['simple_return'])
