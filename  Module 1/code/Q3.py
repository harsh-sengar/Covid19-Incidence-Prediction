#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests 
import json
import numpy as np
import pandas as pd

with open('neighbor-districts-modified.json') as f:
      data = json.load(f)


# In[11]:


def dictToList(data):
    edgeList = []
    for city in data:
        for neighbour in data[city]:
            pair = [city,neighbour]
            edgeList.append(pair)
    return edgeList


# In[12]:


edgeList = dictToList(data)
edgeList
edgeListFrame = pd.DataFrame(np.array(edgeList),
                   columns=['district1', 'district2'])


# In[13]:


edgeListFrame.to_csv (r'edge-graph.csv', index = False, header=True)


# In[ ]:





# In[ ]:





# In[ ]:




