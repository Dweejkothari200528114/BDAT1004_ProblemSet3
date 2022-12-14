#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import geonamescache


# In[3]:


euro12 = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv')
euro12


# In[5]:


euro12.Goals


# In[6]:


euro12.shape[0]


# In[10]:


#Alternative method

team_participate = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', usecols=['Team'])
team_amount = len(team_participate)
print("Number of teams \n", team_amount)


# In[11]:


total_columns = len(euro12.axes[1])
print("Total number of columns present in the dataset are \n", total_columns)


# In[12]:


fouls = euro12[['Team', 'Yellow Cards', 'Red Cards']]
fouls


# In[16]:


sort_by_yellow_team = fouls.sort_values(by = 'Yellow Cards')
sort_by_red_team = fouls.sort_values(by = 'Red Cards')

print("Sort Teams by Red Team \n",sort_by_red_team)
print("sort Teams By Yellow Cards \n",sort_by_yellow_team)


# In[18]:


print("mean value of yellow cards per team \n",round(euro12["Yellow Cards"].mean()))


# In[19]:


euro12[euro12.Goals > 6]


# In[20]:


array_team = np.array(team_participate)
for item in array_team:
      for g in item:
            if g.startswith("G"):
                  print(' Team names that start with G \n',g)


# In[21]:


euro12.iloc[: , 0:7]


# In[22]:


euro12.iloc[: , :-3]


# In[23]:


euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]


# In[ ]:




