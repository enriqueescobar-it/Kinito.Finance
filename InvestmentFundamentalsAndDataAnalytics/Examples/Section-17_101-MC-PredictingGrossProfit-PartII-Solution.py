#!/usr/bin/env python
# coding: utf-8

# ## Monte Carlo - Predicting Gross Profit - Part II

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Proceed from where we left off on the previous exercise.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

rev_m = 200
rev_stdev = 10
iterations = 256

rev = np.random.normal(rev_m, rev_stdev, iterations)
COGS = - (rev * np.random.normal(0.4,0.2))

COGS.mean(), COGS.std()


# ****

# Based on the predicted revenue and Cogs values, estimate the expected Gross Profit of your company. 

# *Reminder: Be careful about estimating the gross profit. If you have stored the Cogs value as a negative number, the gross profit will equal revenues plus Cogs. If you have created Cogs as a positive value, then gross profit would be equal to revenues minus Cogs. Either way, you will obtain the same result for gross profit.* 

# In[2]:


Gross_Profit = rev + COGS
Gross_Profit


# In[3]:


plt.figure(figsize=(15, 6))
plt.plot(Gross_Profit)
plt.show()


# What is the maximum and what is the minimum gross profit value you obtained?

# In[4]:


max(Gross_Profit)


# In[5]:


min(Gross_Profit)


# What is its mean and standard deviation?

# In[6]:


Gross_Profit.mean()


# In[7]:


Gross_Profit.std()


# Do you remember what a histogram is? Plot the gross profit data on a histogram. Use 20 bins directly to check the distribution of the data.

# In[8]:


plt.figure(figsize=(10, 6));
plt.hist(Gross_Profit, bins = 20);
plt.show()


# ************
