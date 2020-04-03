#!/usr/bin/env python
# coding: utf-8

# ## Lists

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Create a list, called "Numbers". Let it contain the numbers 10, 25, 40, and 50.

# In[1]:


Numbers = [10, 25, 40, 50]


# Print the element at index 2 from the list.

# In[2]:


Numbers[2]


# Print the 0th element.

# In[3]:


Numbers[0]


# Print the third-to-last element using a minus sign in the brackets.

# In[4]:


Numbers[-3]


# Substitute the number 10 with the number 15.

# In[5]:


Numbers[0] = 15
Numbers


# Delete the number 25 from the Numbers list.

# In[6]:


del Numbers[1]
Numbers

