#!/usr/bin/env python
# coding: utf-8
## Running a Multivariate Regression in Python
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Let’s continue working on the file we used when we worked on univariate regressions.
# *****
# Run a multivariate regression with 5 independent variables – from Test 1 to Test 5.
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm 
import matplotlib.pyplot as plt
data = pd.read_excel('Section-13_Housing.xlsx')
data.head()
# ### Multivariate Regression:
# Independent Variables: *"House Size (sq.ft.)", "Number of Rooms", "Year of Construction"*
X = data[['House Size (sq.ft.)', 'Number of Rooms', 'Year of Construction']]
X = data.iloc[:,[1,3,4]]
Y = data.iloc[:,0]
# In[ ]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# Independent Variables: *"House Size (sq.ft.)", "Number of Rooms"*
X = data[['House Size (sq.ft.)', 'Number of Rooms']]
X = data.iloc[:,[1,3]]
Y = data.iloc[:,0]
# In[ ]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# Independent Variables: *"House Size (sq.ft.)", "Year of Construction"*
X = data[['House Size (sq.ft.)', 'Year of Construction']]
X = data.iloc[:,[1,4]]
Y = data.iloc[:,0]
# In[ ]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# Independent Variables: *"Number of Rooms", "Year of Construction"*
X = data[['Number of Rooms', 'Year of Construction']]
X = data.iloc[:,[3,4]]
Y = data.iloc[:,0]
# In[ ]:
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
reg.summary()
# ***Suggested Answer:***
# *Test 1 and Test 4 are correlated, and they contribute to the preparation of the IQ test in a similar way.*
