#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from statistics import mean


# In[12]:


df = pd.read_csv("finished-paths-back.csv", delimiter = '\n')
df.columns = [0]


# In[13]:


df = list(df[0])
#df = df.split(",")

ratio = []
for r in df:
    ratio.append(r.split(",")[3])


# In[14]:


df_path_finished = pd.read_csv("paths_finished.tsv", delimiter = '\n', header = None)
df_path_finished = df_path_finished[15:]
df_path_finished = df_path_finished[0]


# In[15]:


df_category = pd.read_csv("article-categories.csv", header = None)
df_category = df_category.where(pd.notnull(df_category), None)


# In[16]:


article_id = pd.read_csv('article-ids.csv', header = None)
del article_id[0]
article1 = list(article_id[1])
article2 = list(article_id[2])

article_id = {article1[i] : article2[i] for i in range(len(article1))}


# In[17]:


category_id = pd.read_csv('category-ids.csv', header = None)
del category_id[0]
category1 = list(category_id[1])
category2 = list(category_id[2])

category_id = {category2[i] : category1[i] for i in range(len(category1))}


# In[18]:


article_category = {}
for row in range(len(df_category)):
    article_category[(df_category[1][row])] = [(df_category[2][row])]
    
    if (df_category[3][row]) != None:
        article_category[(df_category[1][row])].append(df_category[3][row])
    if (df_category[4][row]) != None:
        article_category[(df_category[1][row])].append(df_category[4][row])


# In[19]:


i = 0
category_pair_path_finished = {}
for info in df_path_finished:
    info = info.split()
    article = info[3].replace(";", " ")
    back = (article.count('<'))
    article = article.replace("< ", "")
    article = list(article.split(" "))
    source = article[0]
    target = article[-1]
    
    for category1 in article_category[article_id[source]]:
        if target in article_id:
            for category2 in article_category[article_id[target]]:
                if (category1 + "/" + category2) in category_pair_path_finished:
                    category_pair_path_finished[category1 + "/" + category2].append(float(ratio[i]))
                else:
                    category_pair_path_finished[category1 + "/" + category2] = [float(ratio[i])]

    
    i = i + 1
                
           

for c in category_pair_path_finished:
    category_pair_path_finished[c] = (mean(category_pair_path_finished[c]))


# In[20]:


category_ratio = []
for c_p in category_pair_path_finished:
    ratio = category_pair_path_finished[c_p]
    c_p = c_p.split("/")
    category_ratio.append([c_p[0], c_p[1], ratio])
    


# In[21]:


df_category_ratio = pd.DataFrame(category_ratio)
df_category_ratio.to_csv (r'category-ratios.csv', header=["From_Category", "To_Category", "Ratio_of_human_to_shortest"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




