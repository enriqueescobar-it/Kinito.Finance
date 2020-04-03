#!/usr/bin/env python
# coding: utf-8

# ## Computing Alpha, Beta, and R Squared in Python 

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# *Running a Regression in Python - continued:*

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm 
import matplotlib.pyplot as plt

data = pd.read_excel('D:/Python/Data_Files/IQ_data.xlsx')

X = data['Test 1']
Y = data['IQ']

plt.scatter(X,Y)
plt.axis([0, 120, 0, 150])
plt.ylabel('IQ')
plt.xlabel('Test 1')
plt.show()


# ****

# Use the statsmodels’ **.add_constant()** method to reassign the X data on X1. Use OLS with arguments Y and X1 and apply the fit method to obtain univariate regression results. Help yourself with the **.summary()** method. 

# In[2]:


X1 = sm.add_constant(X)

reg = sm.OLS(Y, X1).fit()


# In[3]:


reg.summary()


# By looking at the p-values, would you conclude Test 1 scores are a good predictor?

# *****

# Imagine a kid would score 84 on Test 1. How many points is she expected to get on the IQ test, approximately?

# In[4]:


45 + 84*0.76


# ******

# ### Alpha, Beta, R^2:

# Apply the stats module’s **linregress()** to extract the value for the slope, the intercept, the r squared, the p_value, and the standard deviation.

# In[5]:


slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)


# In[6]:


slope


# In[7]:


intercept


# In[8]:


r_value


# In[9]:


r_value ** 2


# In[10]:


p_value


# In[11]:


std_err


# Use the values of the slope and the intercept to predict the IQ score of a child, who obtained 84 points on Test 1. Is the forecasted value different than the one you obtained above?

# In[12]:


intercept + 84 * slope


# ******

# Follow the steps to draw the best fitting line of the provided regression.

# Define a function that will use the slope and the intercept value to calculate the dots of the best fitting line.

# In[13]:


def fitline(b):
    return intercept + slope * b


# Apply it to the data you have stored in the variable X.

# In[14]:


line = fitline(X)


# Draw a scatter plot with the X and Y data and then plot X and the obtained fit-line.

# In[15]:


plt.scatter(X,Y)
plt.plot(X,line)
plt.show()

