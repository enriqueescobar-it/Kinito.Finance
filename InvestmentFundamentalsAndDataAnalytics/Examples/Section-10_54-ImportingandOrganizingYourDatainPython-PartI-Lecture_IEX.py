#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


ser = pd.Series(np.random.random(5), name = "Column 01")


# In[3]:


ser


# In[4]:


ser[2]


# In[5]:


from pandas_datareader import data as wb


# In[6]:


PG = wb.DataReader('PG', data_source='iex', start='2015-1-1')


# In[7]:


PG

