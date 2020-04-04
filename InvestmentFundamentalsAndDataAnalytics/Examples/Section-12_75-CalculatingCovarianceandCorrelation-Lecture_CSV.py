#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
# In[ ]:
sec_data = pd.read_csv('D:/Python/PG_BEI.DE_2007_2017.csv', index_col='Date')
# In[ ]:
sec_data.tail()
# In[ ]:
sec_returns = np.log(sec_data / sec_data.shift(1))
# In[ ]:
sec_returns
# ## PG
# In[ ]:
sec_returns['PG'].mean()
# In[ ]:
sec_returns['PG'].mean() * 250
# In[ ]:
sec_returns['PG'].std()
# In[ ]:
sec_returns['PG'].std() * 250 ** 0.5
# ## Beiersdorf
# In[ ]:
sec_returns['BEI.DE'].mean()
# In[ ]:
sec_returns['BEI.DE'].mean() * 250
# In[ ]:
sec_returns['BEI.DE'].std()
# In[ ]:
sec_returns['BEI.DE'].std() * 250 ** 0.5
# ***
# In[ ]:
print sec_returns['PG'].mean() * 250
print sec_returns['BEI.DE'].mean() * 250
# In[ ]:
sec_returns['PG', 'BEI.DE'].mean() * 250
# In[ ]:
sec_returns[['PG', 'BEI.DE']].mean() * 250
# In[ ]:
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
# In[ ]:
PG_var = sec_returns['PG'].var() 
PG_var
# In[ ]:
BEI_var = sec_returns['BEI.DE'].var() 
BEI_var
# In[ ]:
PG_var_a = sec_returns['PG'].var() * 250
PG_var_a
# In[ ]:
BEI_var_a = sec_returns['BEI.DE'].var() * 250
BEI_var_a
# ***
# In[ ]:
cov_matrix = sec_returns.cov()
cov_matrix
# In[ ]:
cov_matrix_a = sec_returns.cov() * 250
cov_matrix_a
# ***
# In[ ]:
corr_matrix = sec_returns.corr()
corr_matrix
