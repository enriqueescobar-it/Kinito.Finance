#!/usr/bin/env python
# coding: utf-8
# ## Using a Function in Another Function
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Define a function that adds 5 to the parameter. Then, define another function that will multiply the newly obtained number by 3.
# Verify your code was correct by calling the second function with an argument of 5. 
# Was your output equal to 30?
# In[1]:
def plus_five(x):
    return x + 5
def m_by_3(x):
    return plus_five(x) * 3
# In[2]:
m_by_3(5)
