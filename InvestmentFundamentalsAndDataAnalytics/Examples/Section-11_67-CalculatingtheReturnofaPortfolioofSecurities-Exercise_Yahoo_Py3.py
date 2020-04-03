#!/usr/bin/env python
# coding: utf-8

# ## Calculating the Return of a Portfolio of Securities

# Download data for a portfolio composed of 5 stocks. Do it for British Petroleum, Ford, Exxon, Lincoln, and Apple for the period ‘2000-1-1’ until today.

# In[ ]:





# ### Normalization to 100:
# 
# $$
# \frac {P_t}{P_0} * 100
# $$

# Normalize to a hundred and plot the data on a graph (you can apply the .loc() or the .iloc() method). 

# In[ ]:





# In[ ]:





# How would you interpret the behavior of the stocks? Just by looking at the chart, would you be able to create a portfolio that provides a solid return on investment?

# *****

# ### Calculating the Return of a Portfolio of Securities

# Obtain the simple return of the securities in the portfolio and store the results in a new table.

# In[ ]:





# First, assume you would like to create an equally-weighted portfolio. Create the array, naming it “weights”.

# In[ ]:





# Obtain the annual returns of each of the stocks and then calculate the dot product of these returns and the weights.

# In[ ]:





# In[ ]:





# Transform the result into a percentage form. 

# In[ ]:





# Is the return of this portfolio satisfactory?
