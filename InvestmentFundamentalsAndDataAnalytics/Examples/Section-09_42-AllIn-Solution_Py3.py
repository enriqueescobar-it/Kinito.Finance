#!/usr/bin/env python
# coding: utf-8
# ## All in - Conditional Statements, Functions, and Loops
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# You are provided with the 'nums' list. Complete the code in the cell that follows. Use a while loop to count the number of values lower than 20. <br/>
# *Hint: This exercise is similar to what we did in the video lecture. You might prefer using the x[item] structure for indicating the value of an element from the list.*
# In[1]:
nums = [1,35,12,24,31,51,70,100]
# In[2]:
def count(numbers):
    numbers = sorted(numbers)
    tot = 0
    
    while numbers[tot] < 20:
        tot += 1
    return tot
# In[3]:
count(nums)
