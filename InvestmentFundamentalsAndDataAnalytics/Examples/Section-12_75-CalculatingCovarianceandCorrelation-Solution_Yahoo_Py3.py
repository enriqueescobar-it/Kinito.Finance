#!/usr/bin/env python
# coding: utf-8
# ## Calculating Covariance and Correlation
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Consider a portfolio composed of *Walmart* and *Facebook*. Do you expect the returns of these companies to show high or low covariance? Or, could you guess what the correlation would be? Will it be closer to 0 or closer to 1? 
# Begin by extracting data for Walmart and Facebook from the 1st of January 2014 until today.
# In[1]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
# In[2]:
tickers = ['WMT', 'FB']
sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2014-1-1')['Adj Close']
# In[3]:
sec_data.head()
# In[4]:
returns = np.log(sec_data / sec_data.shift(1))
returns
# Repeat the process we went through in the lecture for these two stocks. How would you explain the difference between their means and their standard deviations?
# In[5]:
returns[['WMT', 'FB']].mean() * 250
# In[6]:
returns[['WMT', 'FB']].std() * 250 ** 0.5
# ***
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
# ***
# In[7]:
cov_matrix = returns.cov()
cov_matrix
# In[8]:
cov_matrix_a = returns.cov() * 250
cov_matrix_a
# ***
# In[9]:
corr_matrix = returns.corr()
corr_matrix
# Would you consider investing in such a portfolio?
