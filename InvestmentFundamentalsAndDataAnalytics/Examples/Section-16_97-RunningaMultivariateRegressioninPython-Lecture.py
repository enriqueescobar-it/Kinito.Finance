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
# ### Multivariate Regression:
# Independent Variables: *"House Size (sq.ft.)", "Number of Rooms", "Year of Construction"*
# In[ ]:
X = data[['House Size (sq.ft.)', 'Number of Rooms', 'Year of Construction']]
Y = data['House Price']
# In[ ]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# Independent Variables: *"House Size (sq.ft.)", "Number of Rooms"*
# In[ ]:
X = data[['House Size (sq.ft.)', 'Number of Rooms']]
Y = data['House Price']
# In[ ]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# Independent Variables: *"House Size (sq.ft.)", "Year of Construction"*
# In[ ]:
X = data[['House Size (sq.ft.)', 'Year of Construction']]
Y = data['House Price']
# In[ ]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# Independent Variables: *"Number of Rooms", "Year of Construction"*
# In[ ]:
X = data[['Number of Rooms', 'Year of Construction']]
Y = data['House Price']
# In[ ]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
