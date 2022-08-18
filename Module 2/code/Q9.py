#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[9]:


df_category_path = pd.read_csv("category-paths.csv")
df_category_path.columns = [0,1,2,3,4,5]


# In[10]:


category_path = {}
for i in range(len(df_category_path)):
    category_path[df_category_path[1][i]] = [df_category_path[2][i], df_category_path[3][i], df_category_path[4][i], df_category_path[5][i]]


# In[11]:


category_id = pd.read_csv('category-ids.csv', header = None)
del category_id[0]
category1 = list(category_id[1])
category2 = list(category_id[2])

category_id = {category2[i] : category1[i] for i in range(len(category1))}
id_category = {category1[i] : category2[i] for i in range(len(category1))}


# In[12]:


for category in category_id:
    sub_category = (category_id[category]).split(".")
    if (len(sub_category)) > 1:
        cat = ""
        for s in sub_category:
            if cat != "":
                category_path[id_category[cat]] = [a + b for a, b in zip(category_path[id_category[cat]],category_path[category])]
                cat = cat + "." + s
            else:
                cat = s


# In[13]:


category_sub_path = []
for category in category_path:
    category_sub_path.append([category] + category_path[category])


# In[14]:


df_category_sub_path = pd.DataFrame(category_sub_path)
df_category_sub_path.to_csv (r'category-subtree-paths.csv',  header = ["Category_ID", "Number_of_paths_traversed", "Number_of_times_traversed", "Number_of_shortest_paths_traversed", "Number_of_times_shortest_times_traversed"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




