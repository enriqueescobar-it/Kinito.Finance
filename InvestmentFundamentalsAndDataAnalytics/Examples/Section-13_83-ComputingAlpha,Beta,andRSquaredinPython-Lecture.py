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
# In[11]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
# In[12]:
reg.summary()
# Expected value of Y:
# In[13]:
260800 + 402 * 1000
# ### Alpha, Beta, R^2:
# In[14]:
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
# In[15]:
slope
# In[16]:
intercept
# In[17]:
r_value
# In[18]:
r_value ** 2
# In[19]:
p_value
# In[20]:
std_err
