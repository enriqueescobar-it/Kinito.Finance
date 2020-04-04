#!/usr/bin/env python
# coding: utf-8
# ## Use Conditional Statements and Loops Together
# *Suggested Answers follow (usually there are multiple ways to solve a problem in Python).*
# Create a For loop that will print all the variables from a given list multiplied by 2. Let the list contain all numbers from 1 to 10. Create it with the help of the range() function.
# In[1]:
for n in range(1,11):
    print (n * 2)
# Create a little program that runs a loop over all values from 1 to 30. Let it print all Odd numbers, and in the place of the even numbers, it should print "Even".
# Help yourself with the range() function to solve this exercise.
# In[2]:
for x in range(1,31):
    if x % 2 == 1:
        print (x, end = " ")
    else:
        print ("Even", end = " ")
# You have the following list of numbers. Iterate over this list, printing out each list value multiplied by 10.
# Find two solutions of this problem.
# In[3]:
n = [1,2,3,4,5,6]
# In[4]:
for item in n:
    print (item * 10, end = " ")
# In[5]:
for item in range(len(n)):
    print (n[item] * 10, end = " ")
