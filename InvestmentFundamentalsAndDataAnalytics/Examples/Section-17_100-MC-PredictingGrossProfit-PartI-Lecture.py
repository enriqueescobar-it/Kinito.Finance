#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np
import matplotlib.pyplot as plt
# In[2]:
rev_m = 170
rev_stdev = 20
iterations = 1000
# In[3]:
rev = np.random.normal(rev_m, rev_stdev, iterations)
rev
# In[4]:
plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()
# In[5]:
COGS = - (rev * np.random.normal(0.6,0.1))
 
plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()
# In[6]:
COGS.mean()
# In[7]:
COGS.std()
