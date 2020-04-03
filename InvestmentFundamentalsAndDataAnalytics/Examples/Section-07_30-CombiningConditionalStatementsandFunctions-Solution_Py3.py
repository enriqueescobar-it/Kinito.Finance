#!/usr/bin/env python
# coding: utf-8

# ## Combining Conditional Statements and Functions

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Define a function, called **compare_the_two()**, with two arguments. If the first one is greater than the second one, let it print "Greater". If the second one is greater, it should print "Less". Let it print "Equal" if the two values are the same number.

# In[1]:


def compare_the_two(x,y):
    if x > y:
        print ("Greater")
    elif x < y:
        print ("Less")
    else:
        print ("Equal")


# In[2]:


compare_the_two(10,10)

