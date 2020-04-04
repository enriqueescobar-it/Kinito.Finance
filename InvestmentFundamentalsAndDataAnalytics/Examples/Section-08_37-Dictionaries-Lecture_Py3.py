#!/usr/bin/env python
# coding: utf-8
# In[1]:
dict = {'k1': "cat", 'k2': "dog", 'k3': "mouse", 'k4': "fish"}
dict
# In[2]:
dict['k1']
# In[3]:
dict["k3"]
# In[4]:
dict['k5'] = 'parrot'
dict
# In[5]:
dict['k2'] = 'squirrel'
dict
# ******
# In[6]:
dep_workers = {'dep_1': 'Peter', 'dep_2': ['Jennifer', 'Michael', 'Tommy']}
# In[7]:
dep_workers['dep_2']
# ******
# In[8]:
Team = {}
Team['Point Guard'] = 'Dirk'
Team['Shooting Guard'] = 'Al'
Team['Small Forward'] = 'Sean'
Team['Power Forward'] = 'Alexander'
Team['Center'] = 'Hector'
# In[9]:
print (Team)
# In[10]:
print (Team['Center'])
# In[11]:
print (Team.get('Small Forward'))
# In[12]:
print (Team.get('Coach'))
