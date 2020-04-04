#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
# In[2]:
PG = pd.read_csv('D:/Python/PG_1995-03_23_2017.csv', index_col = 'Date')
# or:
# In[3]:
PG = pd.read_csv('D:/Python/PG_1995-03_23_2017.csv')
PG = PG.set_index('Date')
# In[4]:
PG.head()
# In[5]:
PG.tail()
# ## Simple Rate of Return
# $$
# \frac{P_1 - P_0}{P_0} = \frac{P_1}{P_0} - 1
# $$
# In[6]:
PG['simple_return'] = (PG['Close'] / PG['Close'].shift(1)) - 1
print (PG['simple_return'])
