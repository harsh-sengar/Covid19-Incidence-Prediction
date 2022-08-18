#!/usr/bin/env python
# coding: utf-8

# In[120]:


import pandas as pd
import numpy as np


# In[121]:


df_finished_paths_noback = pd.read_csv("finished-paths-no-back.csv")
df_finished_paths_noback.columns = [0,1,2,3]


# In[122]:


exact_length = 0
larger_by = {1:0, 2:0, 3:0 ,4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}

for i in range(len(df_finished_paths_noback)):
    if(df_finished_paths_noback[1][i] == df_finished_paths_noback[2][i]):
        exact_length = exact_length + 1
    elif((df_finished_paths_noback[1][i] - df_finished_paths_noback[2][i]) <= 10):
        larger_by[(df_finished_paths_noback[1][i] - df_finished_paths_noback[2][i])] = larger_by[(df_finished_paths_noback[1][i] - df_finished_paths_noback[2][i])] + 1
    if((df_finished_paths_noback[1][i] - df_finished_paths_noback[2][i]) >= 11):
        larger_by[11] = larger_by[11] + 1


# In[123]:


len(df_finished_paths_noback)


# In[124]:


exact_length = (exact_length*100)/len(df_finished_paths_noback)


# In[125]:


for large in larger_by:
    larger_by[large] = (larger_by[large]*100)/len(df_finished_paths_noback)


# In[126]:


list(larger_by.values())


# In[127]:


exact_length


# In[128]:


percentage_paths_noback = []
percentage_paths_noback.append(exact_length)
percentage_paths_noback = percentage_paths_noback + list(larger_by.values())


# In[ ]:





# In[129]:


percentage_paths_noback


# In[ ]:





# In[130]:


df_percentage_paths_noback = pd.DataFrame([percentage_paths_noback])
df_percentage_paths_noback.to_csv (r'percentage-paths-no-back.csv', header=["Equal_Length", "Larger_by_1", "Larger_by_2", "Larger_by_3", "Larger_by_4" ,"Larger_by_5", "Larger_by_6", "Larger_by_7", "Larger_by_8", "Larger_by_9", "Larger_by_10", "Larger_by_more_than_10"])


# In[ ]:





# In[ ]:





# In[131]:


df_finished_paths_back = pd.read_csv("finished-paths-back.csv")
df_finished_paths_back.columns = [0,1,2,3]


# In[ ]:





# In[132]:


exact_length = 0
larger_by = {1:0, 2:0, 3:0 ,4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}

for i in range(len(df_finished_paths_back)):
    if(df_finished_paths_back[1][i] == df_finished_paths_back[2][i]):
        exact_length = exact_length + 1
    elif((df_finished_paths_back[1][i] - df_finished_paths_back[2][i]) <= 10):
        larger_by[(df_finished_paths_back[1][i] - df_finished_paths_back[2][i])] = larger_by[(df_finished_paths_back[1][i] - df_finished_paths_back[2][i])] + 1
    if((df_finished_paths_back[1][i] - df_finished_paths_back[2][i]) >= 11):
        larger_by[11] = larger_by[11] + 1


# In[133]:


len(df_finished_paths_back)


# In[ ]:





# In[134]:


exact_length = (exact_length*100)/len(df_finished_paths_back)


# In[135]:


for large in larger_by:
    larger_by[large] = (larger_by[large]*100)/len(df_finished_paths_back)


# In[136]:


exact_length


# In[137]:


percentage_paths_back = []
percentage_paths_back.append(exact_length)
percentage_paths_back = percentage_paths_back + list(larger_by.values())


# In[138]:


np.array(percentage_paths_back).sum()


# In[ ]:





# In[139]:


df_percentage_paths_back = pd.DataFrame([percentage_paths_back])
df_percentage_paths_back.to_csv (r'percentage-paths-back.csv', header=["Equal_Length", "Larger_by_1", "Larger_by_2", "Larger_by_3", "Larger_by_4" ,"Larger_by_5", "Larger_by_6", "Larger_by_7", "Larger_by_8", "Larger_by_9", "Larger_by_10", "Larger_by_more_than_10"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




