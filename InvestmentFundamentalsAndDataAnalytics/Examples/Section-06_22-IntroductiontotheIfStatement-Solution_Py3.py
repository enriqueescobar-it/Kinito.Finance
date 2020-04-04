#!/usr/bin/env python
# coding: utf-8
# ## Introduction to the IF statement
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Create a two-line code that prints "The condition has been satisfied" if 5 is greater than 2.
# In[1]:
if 5 > 2:
    print ("The condition has been satisfied")
# Assign 10 to the variable x and 25 to the variable y. In the same cell, create 2 conditional statements. Let the first one print "Both conditions are correct" if x is greater then 3 and y is greater than 13. Let the second one print "At least one of the conditions is false" if x is less than or equal to 3 or y is less than or equal to 13. 
# Change the values assigned to x and y and re-run the cell to verify your code still works.
# In[1]:
x = 10
y = 25
if x > 3 and y > 13:
    print ('Both conditions are correct')
if x <= 3 or y <= 13:
    print ('At least one of the conditions is false')
