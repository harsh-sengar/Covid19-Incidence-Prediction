#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
from functools import reduce  
import operator
import collections
import networkx as nx
from collections import Mapping


# In[15]:


df = pd.read_csv("categories.tsv", delimiter = "\t", names = ["0","1"] )
df = df[12:]
df = df["1"]


# In[16]:


def getTree(dataDict, keyList):
    return reduce(operator.getitem, keyList, dataDict)

def setCategory(dataDict, keyList, category):
        if category not in getTree(dataDict, keyList[:-1])[keyList[-1]]:
            getTree(dataDict, keyList[:-1])[keyList[-1]].update({category:{}})


# In[17]:


Hierarchy = {}
Hierarchy['subject'] = {}
def buildTree(categoriesData):
    for categories in categoriesData:
        categories = categories.replace("."," ")
        categories = categories.split()
        categories_merged = []
        for category in categories:
            if len(categories_merged):
                categories_merged.append(categories_merged[-1] + "." + category)
            else:
                categories_merged.append(category)
                
        keys = []
        for category in categories_merged:
            if(keys):
                setCategory(Hierarchy, keys, category)
            keys.append(category)


# In[18]:


buildTree(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Iterate Dictionary

# In[19]:


def categoriesAlphabetical(d):
    for k, v in d.items():
        if isinstance(v, dict):  
            v = dict(collections.OrderedDict(sorted(v.items())))
            categoriesAlphabetical(v)
            d[k] = v
            


# In[20]:


categoriesAlphabetical(Hierarchy)


# In[ ]:





# In[ ]:





# In[ ]:





# In[21]:


def assignCategoryId(Hierarchy, G):
    c = 1
    categories_id = []
    q = list(Hierarchy.items())
    categories_id.append(('subject',"C"+"%04d"%c))
    while q:
        v, d = q.pop()
        for nv, nd in d.items():
            G.add_edge(v, nv)
            c = c + 1
            categories_id.append((nv,"C"+"%04d"%c))     
            if isinstance(nd, Mapping):
                q.append((nv,nd))
    return categories_id


# In[22]:


G = nx.DiGraph()
categories_id = assignCategoryId(Hierarchy, G)


# In[23]:


#nx.draw(G, with_labels = True)


# In[24]:


len(G.nodes())


# In[26]:


df_categories = pd.DataFrame(categories_id)
df_categories.to_csv (r'category-ids.csv', header = ["Category_Name", "Category_ID"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




