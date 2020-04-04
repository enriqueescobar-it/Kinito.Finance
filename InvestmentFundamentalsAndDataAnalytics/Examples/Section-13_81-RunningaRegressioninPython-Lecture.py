#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm 
import matplotlib.pyplot as plt
# In[2]:
data = pd.read_excel('D:/Python/Data_Files/Housing.xlsx')
# In[3]:
data
# In[4]:
data[['House Price', 'House Size (sq.ft.)']]
# ### Univariate Regression
# In[5]:
X = data['House Size (sq.ft.)']
Y = data['House Price']
# In[6]:
X
# In[7]:
Y
# In[8]:
plt.scatter(X,Y)
plt.show()
# In[9]:
plt.scatter(X,Y)
plt.axis([0, 2500, 0, 1500000])
plt.show()
# In[10]:
plt.scatter(X,Y)
plt.axis([0, 2500, 0, 1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft)')
plt.show()
