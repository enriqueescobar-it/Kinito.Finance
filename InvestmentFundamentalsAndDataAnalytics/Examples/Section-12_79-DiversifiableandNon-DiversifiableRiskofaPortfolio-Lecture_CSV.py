#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


sec_data = pd.read_csv('D:/Python/PG_BEI.DE_2007_2017.csv', index_col='Date')


# In[3]:


sec_data.tail()


# In[4]:


sec_returns = np.log(sec_data / sec_data.shift(1))


# In[5]:


sec_returns


# ## PG

# In[6]:


sec_returns['PG'].mean()


# In[7]:


sec_returns['PG'].mean() * 250


# In[8]:


sec_returns['PG'].std()


# In[9]:


sec_returns['PG'].std() * 250 ** 0.5


# ## Beiersdorf

# In[10]:


sec_returns['BEI.DE'].mean()


# In[11]:


sec_returns['BEI.DE'].mean() * 250


# In[12]:


sec_returns['BEI.DE'].std()


# In[13]:


sec_returns['BEI.DE'].std() * 250 ** 0.5


# ***

# In[14]:


print (sec_returns['PG'].mean() * 250)
print (sec_returns['BEI.DE'].mean() * 250)


# In[15]:


sec_returns['PG', 'BEI.DE'].mean() * 250


# In[16]:


sec_returns[['PG', 'BEI.DE']].mean() * 250


# In[17]:


sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5


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

# In[18]:


PG_var = sec_returns['PG'].var() 
PG_var


# In[19]:


BEI_var = sec_returns['BEI.DE'].var() 
BEI_var


# In[20]:


PG_var_a = sec_returns['PG'].var() * 250
PG_var_a


# In[21]:


BEI_var_a = sec_returns['BEI.DE'].var() * 250
BEI_var_a


# ***

# In[22]:


cov_matrix = sec_returns.cov()
cov_matrix


# In[23]:


cov_matrix_a = sec_returns.cov() * 250
cov_matrix_a


# ***

# In[24]:


corr_matrix = sec_returns.corr()
corr_matrix


# ## Calculating Portfolio Risk

# Equal weigthing scheme:

# In[25]:


weights = np.array([0.5, 0.5])


# Portfolio Variance:

# In[26]:


pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
pfolio_var


# Portfolio Volatility:

# In[27]:


pfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) ** 0.5
pfolio_vol


# In[28]:


print (str(round(pfolio_vol, 5) * 100) + ' %')


# ## Calculating Diversifiable and Non-Diversifiable Risk of a Portfolio

# In[29]:


weights = np.array([0.5, 0.5])


# In[30]:


weights[0]


# In[31]:


weights[1]


# ***

# Diversifiable Risk:

# In[32]:


PG_var_a = sec_returns[['PG']].var() * 250
PG_var_a


# In[33]:


BEI_var_a = sec_returns[['BEI.DE']].var() * 250
BEI_var_a


# In[34]:


dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)
dr


# In[35]:


float(PG_var_a)


# In[36]:


PG_var_a = sec_returns['PG'].var() * 250
PG_var_a


# In[37]:


BEI_var_a = sec_returns['BEI.DE'].var() * 250
BEI_var_a


# In[38]:


dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)
dr


# In[39]:


print (str(round(dr*100, 3)) + ' %')


# Non-Diversifiable Risk:

# In[40]:


n_dr_1 = pfolio_var - dr
n_dr_1


# In[41]:


n_dr_2 = (weights[0] ** 2 * PG_var_a) + (weights[1] ** 2 * BEI_var_a)
n_dr_2


# In[42]:


n_dr_1 == n_dr_2

