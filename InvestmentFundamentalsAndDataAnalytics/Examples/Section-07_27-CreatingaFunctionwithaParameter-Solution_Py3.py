#!/usr/bin/env python
# coding: utf-8

# ## Creating a Function with a Parameter

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Define a function that returns a value equal to its argument multiplied by 2.

# In[1]:


def multiplication_by_2(x):
    print (x * 2)


# Define a funciton that returns a float value equal to its argument divided by 2.

# In[2]:


def division_by_2(x):
    return float(x) / 2


# or:

# In[3]:


def divisin_by_2(x):
    return x / 2.0

# This is new to you - yes, the divisor could be set to be a float, and that would make your output a floating point, too!

