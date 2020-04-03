#!/usr/bin/env python
# coding: utf-8

# ## While Loops and Incrementing

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Create a while loop that will print all odd numbers from 0 to 30 on the same row. 
# <br />
# *Hint: There are two ways in which you can create the odd values!*

# In[2]:


x = 1
while x <= 30:
    print (x, end=" ")
    x = x + 2


# or:

# In[3]:


x = 1
while x <= 30:
    print (x, end=" ")
    x += 2

