#!/usr/bin/env python
# coding: utf-8

# ## Another Way to Define a Function

# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*

# Define a function that states the value of the argument accompanied by the phrase "Raised to the power of 2:" and returns a value equal to its argument raised to the power of 2. This time, use a new variable, called "result", in the body of the Function. 
# Call the function with some argument to verify it works properly.
# 
# *Hint: Your knowledge about stating multiple elements on a line can be of great help in solving this exercise!*

# In[1]:


def multiplication_by_2(x):
    result = x ** 2
    print (x, "Raised to the power of 2:")
    return result


# In[2]:


multiplication_by_2(5)

