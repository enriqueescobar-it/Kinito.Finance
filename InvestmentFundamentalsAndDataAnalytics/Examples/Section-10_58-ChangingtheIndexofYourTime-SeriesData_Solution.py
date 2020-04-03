#!/usr/bin/env python
# coding: utf-8

# ## Importing and Organizing Your Data in Python - Part III

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Import the 'example 01' file you created in the previous lecture and set the 'Date' column as an index of that table. 
# Remember that there are two possible answers to this question.

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('D:/Python/New_Files/example_01.csv', index_col = 'Date')


# In[3]:


data


# In[4]:


data = pd.read_csv('D:/Python/New_Files/example_01.csv')


# In[5]:


data = data.set_index('Date')
data

