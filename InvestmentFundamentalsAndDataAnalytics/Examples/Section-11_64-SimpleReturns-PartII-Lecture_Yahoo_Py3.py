#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
# In[2]:
PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')
# In[3]:
PG.head()
# In[4]:
PG.tail()
# ## Simple Rate of Return
# $$
# \frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
# $$
# In[5]:
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print (PG['simple_return'])
# In[6]:
PG['simple_return'].plot(figsize=(8, 5))
plt.show()
# In[7]:
avg_returns_d = PG['simple_return'].mean()
avg_returns_d
# In[8]:
avg_returns_a = PG['simple_return'].mean() * 250
avg_returns_a
# In[9]:
print (str(round(avg_returns_a, 5) * 100) + ' %')