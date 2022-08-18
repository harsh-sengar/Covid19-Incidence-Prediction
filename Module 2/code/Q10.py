#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np


# In[19]:


df_path_unfinished = pd.read_csv("paths_unfinished.tsv", delimiter = '\n', header = None)


# In[20]:


df_path_unfinished = df_path_unfinished[16:]


# In[21]:


df_path_unfinished = df_path_unfinished[0]


# In[ ]:





# In[22]:


df_path_finished = pd.read_csv("paths_finished.tsv", delimiter = '\n', header = None)


# In[23]:


df_path_finished = df_path_finished[15:]
df_path_finished = df_path_finished[0]


# In[24]:


df_category = pd.read_csv("article-categories.csv", header = None)
df_category = df_category.where(pd.notnull(df_category), None)


# In[25]:


article_category = {}
for row in range(len(df_category)):
    article_category[(df_category[1][row])] = [(df_category[2][row])]
    
    if (df_category[3][row]) != None:
        article_category[(df_category[1][row])].append(df_category[3][row])
    if (df_category[4][row]) != None:
        article_category[(df_category[1][row])].append(df_category[4][row])


# In[26]:


article_id = pd.read_csv('article-ids.csv', header = None)
del article_id[0]
article1 = list(article_id[1])
article2 = list(article_id[2])

article_id = {article1[i] : article2[i] for i in range(len(article1))}


# In[27]:


category_id = pd.read_csv('category-ids.csv', header = None)
del category_id[0]
category1 = list(category_id[1])
category2 = list(category_id[2])

category_id = {category2[i] : category1[i] for i in range(len(category1))}


# In[28]:


def sub_categories(source, target):
    source = source.replace(".", " ")
    source = list(source.split(" "))
    target = target.replace(".", " ")
    target = list(target.split(" "))
    
    category_pair = []
    
    s_cat = ""
    
    for s in source:
        if s_cat != "":
            s_cat = s_cat + "." + s
        else:
            s_cat = s
        t_cat = ""
        for t in target:
            if t_cat != "":
                t_cat = t_cat + "." + t
            else:
                t_cat = t
            category_pair.append((s_cat, t_cat))
    
    return category_pair


# In[29]:


category_pair_path_unfinished = {}
for info in df_path_unfinished:
    info = info.split()
    article = info[3].replace(";", " ")
    back = (article.count('<'))
    article = article.replace("< ", "")
    article = list(article.split(" "))
    source = article[0]
    target = info[4]

    
    for category1 in article_category[article_id[source]]:
        if target in article_id:
            for category2 in article_category[article_id[target]]:
                category_pair = sub_categories(category_id[category1], category_id[category2])
                
                for cat1, cat2 in category_pair:
                    if (cat1 + "/" + cat2) in category_pair_path_unfinished:
                        category_pair_path_unfinished[cat1 + "/" + cat2] = category_pair_path_unfinished[cat1 + "/" + cat2] + 1
                    else:
                        category_pair_path_unfinished[cat1 + "/" + cat2] = 1


# In[30]:


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
                category_pair = sub_categories(category_id[category1], category_id[category2])
                
                for cat1, cat2 in category_pair:
                    if (cat1 + "/" + cat2) in category_pair_path_finished:
                        category_pair_path_finished[cat1 + "/" + cat2] = category_pair_path_finished[cat1 + "/" + cat2] + 1
                    else:
                        category_pair_path_finished[cat1 + "/" + cat2] = 1


# In[31]:


sub_categories("subject.science", "subject.Art")


# In[ ]:





# In[32]:


category_pairs = []
for cat_pair in category_pair_path_unfinished:
    c1 = 0
    c2 = 0
    if cat_pair in category_pair_path_finished:
        c1 = category_pair_path_finished[cat_pair]
    if cat_pair in category_pair_path_unfinished:
        c2 = category_pair_path_unfinished[cat_pair]
        
    c1_p = c1/(c1+c2)
    c2_p = c2/(c1+c2)
    
    cat_pair = cat_pair.split("/")
    source = cat_pair[0]
    target = cat_pair[1]
    category_pairs.append([source, target, c1_p*100, c2_p*100])


# In[ ]:





# In[33]:


df_category_pairs = pd.DataFrame(category_pairs)
df_category_pairs.to_csv (r'category-pairs.csv', header=["From_Category", "To_Category", "Percentage_of_finished_paths", "Percentage_of_unfinished_paths"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




