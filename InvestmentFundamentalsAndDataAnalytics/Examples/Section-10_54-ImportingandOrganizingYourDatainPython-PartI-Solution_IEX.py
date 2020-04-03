#!/usr/bin/env python
# coding: utf-8

# ## Importing and Organizing Your Data in Python - Part I

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# a. (*Challenge!*) Create a series object of 10 randomly generated integer values.

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


ser = pd.Series(np.random.randint(10, size = 10, dtype = 'int'), name = "Column 01")


# In[3]:


ser


# b. Extract data from IEX for Ford from the 1st of January 2015. The ticker you need is ‘F’. 

# In[4]:


from pandas_datareader import data as wb


# In[5]:


F = wb.DataReader('F', data_source='iex', start='2015-1-1')


# In[6]:


F

