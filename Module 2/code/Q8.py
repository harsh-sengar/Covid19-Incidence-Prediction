#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import collections


# In[2]:


df = pd.read_csv("paths_finished.tsv", delimiter = '\n', header = None)
df = df[15:]
df = df[0]


# In[ ]:





# In[3]:


df_path_finished = pd.read_csv("paths_finished.tsv", delimiter = '\n', header = None)
df_path_finished = df_path_finished[15:]
df_path_finished = df_path_finished[0]


# In[4]:


article_id = pd.read_csv('article-ids.csv', header = None)
del article_id[0]
article1 = list(article_id[1])
article2 = list(article_id[2])

article_id = {article1[i] : article2[i] for i in range(len(article1))}


# In[5]:


category_id = pd.read_csv('category-ids.csv', header = None)
del category_id[0]
category1 = list(category_id[1])
category2 = list(category_id[2])

category_id = {category2[i] : category1[i] for i in range(len(category1))}


# In[6]:


edge = pd.read_csv("edges.csv", header = None)
node1 = edge[1]
node2 = edge[2]

i = 0
adj_list = {}
for node in node1:
    if node not in adj_list:
                adj_list[node] = []
    if node2[i] not in adj_list:
                adj_list[node2[i]] = []
    adj_list[node].append(node2[i])
    adj_list[node2[i]].append(node)
    
    i = i + 1
    
for node in adj_list:
    adj_list[node] = list(set(adj_list[node]))


# In[7]:


df_category = pd.read_csv("article-categories.csv", header = None)
df_category = df_category.where(pd.notnull(df_category), None)


# In[8]:


article_category = {}
for row in range(len(df_category)):
    article_category[(df_category[1][row])] = [(df_category[2][row])]
    
    if (df_category[3][row]) != None:
        article_category[(df_category[1][row])].append(df_category[3][row])
    if (df_category[4][row]) != None:
        article_category[(df_category[1][row])].append(df_category[4][row])


# In[9]:


node_visited = {}
def bfs(visited, queue, graph, node, target):
    
    if node in node_visited:
        parent = node_visited[node]
        path = []
        while (target in parent) and parent[target] != target:
            path.append(target)
            target = parent[target]
             
        path.append(target)
        path = path[::-1]
        return path
        
    visited.append(node)
    queue.append(node)
    component = []
    parent = {}
    parent[node] = node
    while queue:
        s = queue.pop(0) 
        component.append(s) 

        if s in graph:
            for neighbour in graph[s]:
                  if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    parent[neighbour] = s
                    
    path = []
    while parent[target] != target:
        path.append(target)
        target = parent[target]
        
    path.append(target)
    path = path[::-1]
    node_visited[node] = parent
    
    return path


# In[ ]:





# In[10]:


def check_shortest_path(i, source, target):
    info = df_path_finished[i]
    info = info.split()
    article = info[3].replace(";", " ")
    back = (article.count('<'))
    article = article.replace("< ", "")
    article = list(article.split(" "))
    source = article[0]
    target = article[-1]

    visited = [] 
    queue = []  
    print((bfs(visited, queue, adj_list, article_id[source], article_id[target])))


# In[11]:


article_path_finished = []


# In[12]:


#for info in df_path_finished:
#    info = info.split()
#    article = info[3].replace(";", " ")
#    back = (article.count('<'))
#    article = article.replace("< ", "")
#    article = list(article.split(" "))
#    source = article[0]
#    target = article[-1]
    
#    visited = [] 
#    queue = []  
#    article_path_finished.append((bfs(visited, queue, adj_list, article_id[source], article_id[target])))


# In[ ]:





# In[ ]:





# In[13]:


#df_article_path_finished = pd.DataFrame(article_path_finished)
#df_article_path_finished.to_csv (r'article_shortest_path_finished.csv', header=False)


# In[14]:


df_article_path_finished = pd.read_csv("article_shortest_path_finished.csv", header = None)


# In[15]:


df_article_path_finished = df_article_path_finished.where(pd.notnull(df_article_path_finished), None)
del df_article_path_finished[0]
df_article_path_finished = np.array(df_article_path_finished)


# In[16]:


category_times = {}
category_path = {}


# In[17]:


i = 0
for info in df_path_finished:
    info = info.split()
    article = info[3].replace(";", " ")
    back = (article.count('<'))
    article = article.replace("< ", "")
    articles = list(article.split(" "))
    
    for article in articles:
        categories = article_category[article_id[article]]
        
        for category in categories:
            if category not in category_times:
                category_times[category] = 1
            else:
                category_times[category] = category_times[category] + 1
            
            if category not in category_path:
                category_path[category] = [i]
            else:
                category_path[category].append(i)
                
                
        i = i + 1
    
    


# In[18]:


for category in category_path:
        category_path[category] = len(list(set(category_path[category])))


# In[19]:


df_article_path_finished


# In[20]:


shortest_category_times = {}
shortest_category_path = {}


# In[21]:


for i in range(len(df_article_path_finished)):
    
    articles = (df_article_path_finished[i,:])
    for article in articles:
        if article != None:
            categories = article_category[article]

            for category in categories:
                if category not in shortest_category_times:
                    shortest_category_times[category] = 1
                else:
                    shortest_category_times[category] = shortest_category_times[category] + 1

                if category not in shortest_category_path:
                    shortest_category_path[category] = [i]
                else:
                    shortest_category_path[category].append(i)


# In[22]:


for category in shortest_category_path:
        shortest_category_path[category] = len(list(set(shortest_category_path[category])))


# In[23]:


category_times = dict(collections.OrderedDict(sorted(category_times.items())))
category_path = dict(collections.OrderedDict(sorted(category_path.items())))
shortest_category_times = dict(collections.OrderedDict(sorted(shortest_category_times.items())))
shortest_category_path = dict(collections.OrderedDict(sorted(shortest_category_path.items())))


# In[ ]:





# In[24]:


output = []
for i in range(1,147):
    category = "C"+"%04d"%i
    c_t = 0
    c_p = 0
    s_p = 0
    s_t = 0
    if category in category_times:
        c_t = category_times[category] 
    if category in category_times:
        c_p = category_path[category] 
    if category in category_times:
        s_t = shortest_category_times[category] 
    if category in category_times:
        s_p = shortest_category_path[category] 
        
    output.append([category, c_p, c_t, s_p, s_t])


# In[ ]:





# In[25]:


df_output = pd.DataFrame(output)
df_output.to_csv (r'category-paths.csv', header = ["Category_ID", "Number_of_paths_traversed", "Number_of_times_traversed", "Number_of_shortest_paths_traversed", "Number_of_times_shortest_times_traversed"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




