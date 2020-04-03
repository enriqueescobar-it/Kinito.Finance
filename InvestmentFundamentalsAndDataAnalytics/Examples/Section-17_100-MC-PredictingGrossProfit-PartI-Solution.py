#!/usr/bin/env python
# coding: utf-8

# ## Monte Carlo - Predicting Gross Profit - Part I

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Imagine you are an experienced manager and you have forecasted revenues of \$200mln, with an expected deviation of $10mln. You are convinced Cogs will be near 40% of the revenues, and their expected deviation is 20% of its own value. 

# Use NumPy’s random.random function to simulate the potential revenue stream for 250 iterations (which is the number of trading days in a year) and then the predicted Cogs value. 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


rev_m = 200
rev_stdev = 10
iterations = 250


# In[3]:


rev = np.random.normal(rev_m, rev_stdev, iterations)
rev


# Plot the obtained data for revenues and Cogs on a graph and observe the behavior of the obtained values.

# In[4]:


plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()


# In[5]:


COGS = - (rev * np.random.normal(0.4,0.2))
 
plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()


# Cogs mean:

# In[6]:


COGS.mean()


# Cogs std:

# In[7]:


COGS.std()

