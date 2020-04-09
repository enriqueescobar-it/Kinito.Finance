#!/usr/bin/env python
# coding: utf-8
# # Pandas Exercise - Solutions
# Time to test your new pandas skills! Use the two csv files in this folder to complete the tasks in bold below!
# ** NOTE: ALL TASKS MUST BE DONE IN ONE LINE OF PANDAS CODE. GOT STUCK? NO PROBLEM! CHECK OUT THE SOLUTIONS LECTURE! **
# ** Import pandas and read in the banklist.csv file into a dataframe called banks. **
import pandas as pd
# In[25]:
banks = pd.read_csv('banklist.csv')
# ** Show the head of the dataframe **
banks.head()
# ** What are the column names? **
banks.columns
# ** How many States (ST) are represented in this data set? **
banks['ST'].nunique()
# ** Get a list or array of all the states in the data set. **
banks['ST'].unique()
# ** What are the top 5 states with the most failed banks? **
banks.groupby("ST").count().sort_values('Bank Name',ascending=False).iloc[:5]['Bank Name']
# ** What are the top 5 acquiring institutions? **
banks['Acquiring Institution'].value_counts().iloc[:5]
# ** How many banks has the State Bank of Texas acquired? How many of them were actually in Texas?**
banks[banks['Acquiring Institution']=='State Bank of Texas']
# ** What is the most common city in California for a bank to fail in?**
banks[banks['ST']=='CA'].groupby('City').count().sort_values('Bank Name',ascending=False).head(1)
# ** How many failed banks don't have the word "Bank" in their name? **
# banks['Bank Name'].apply(lambda name: 'Bank' not in name).value_counts()
sum(banks['Bank Name'].apply(lambda name: 'Bank' not in name))
# ** How many bank names start with the letter 's' ? **
sum(banks['Bank Name'].apply(lambda name:name[0].upper() =='S'))
# ** How many CERT values are above 20000 ? **
sum(banks['CERT']>20000)
# ** How many bank names consist of just two words? (e.g. "First Bank" , "Bank Georgia" )**
sum(banks['Bank Name'].apply(lambda name: len(name.split())==2))
# **Bonus: How many banks closed in the year 2008? (this is hard because we technically haven't learned about time series with pandas yet! Feel free to skip this one!**
# WE WILL LEARN A MUCH BETTER WAY TO DO THIS SOON!
sum(banks['Closing Date'].apply(lambda date: date[-2:]) == '08')
# Better way
# sum(pd.to_datetime(banks['Closing Date']).apply(lambda date: date.year) == 2008)
# # GREAT JOB!
