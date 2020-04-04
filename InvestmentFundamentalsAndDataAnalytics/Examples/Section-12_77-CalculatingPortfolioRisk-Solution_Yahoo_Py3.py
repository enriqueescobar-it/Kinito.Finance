#!/usr/bin/env python
# coding: utf-8
# ## Calculating Portfolio Risk
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Calculate the risk of an equally weighted portfolio composed of Microsoft and Apple. The data can be obtained from Yahoo Finance for the period 1st of January 2007 until today. 
# *Hint: The code we went through in the lecture is what you need here. You will need to import the data first. The previous lessons could be a good reference point for that! :) *
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
# In[2]:
tickers = ['MSFT', 'AAPL']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2007-1-1')['Adj Close']
# In[3]:
sec_data.tail()
# In[4]:
sec_returns = np.log(sec_data / sec_data.shift(1))
# In[5]:
sec_returns
# ## MSFT
# In[6]:
sec_returns['MSFT'].mean()
# In[7]:
sec_returns['MSFT'].mean() * 250
# In[8]:
sec_returns['MSFT'].std()
# In[9]:
sec_returns['MSFT'].std() * 250 ** 0.5
# ## Apple
# In[10]:
sec_returns['AAPL'].mean()
# In[11]:
sec_returns['AAPL'].mean() * 250
# In[12]:
sec_returns['AAPL'].std()
# In[13]:
sec_returns['AAPL'].std() * 250 ** 0.5
# ***
# In[14]:
sec_returns[['MSFT', 'AAPL']].mean() * 250
# In[15]:
sec_returns[['MSFT', 'AAPL']].std() * 250 ** 0.5
# ## Covariance and Correlation
# 
# \begin{eqnarray*}
# Covariance Matrix: \  \   
# \Sigma = \begin{bmatrix}
#         \sigma_{1}^2 \ \sigma_{12} \ \dots \ \sigma_{1I} \\
#         \sigma_{21} \ \sigma_{2}^2 \ \dots \ \sigma_{2I} \\
#         \vdots \ \vdots \ \ddots \ \vdots \\
#         \sigma_{I1} \ \sigma_{I2} \ \dots \ \sigma_{I}^2
#     \end{bmatrix}
# \end{eqnarray*}
# *****
# In[16]:
cov_matrix = sec_returns.cov()
cov_matrix
# In[17]:
cov_matrix_a = sec_returns.cov() * 250
cov_matrix_a
# ***
# In[18]:
corr_matrix = sec_returns.corr()
corr_matrix
# ## Calculating Portfolio Risk
# Equal weigthing scheme:
# In[19]:
weights = np.array([0.5, 0.5])
# Portfolio Variance:
# In[20]:
pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
pfolio_var
# Portfolio Volatility:
# In[21]:
pfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) ** 0.5
pfolio_vol
# In[22]:
print (str(round(pfolio_vol, 5) * 100) + ' %')
