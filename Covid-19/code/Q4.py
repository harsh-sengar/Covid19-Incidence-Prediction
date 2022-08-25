#!/usr/bin/env python
# coding: utf-8

# In[51]:


import json
import numpy as np
import os
import pandas as pd
from difflib import SequenceMatcher
from collections import OrderedDict 
import requests 
import csv

f = open('neighbor-districts-modified.json') 
neighbourData = json.load(f) 


# In[ ]:





# In[52]:


reader = csv.DictReader(open('district-id.csv'))

districtId = {}
for row in reader:
    key = row.pop('districtname')
    districtId[key] = list(row.values())[0]


# In[53]:


casesWeek = {}
reader = csv.DictReader(open('cases-week.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (casesWeek)):
        casesWeek[key] = {}
    casesWeek[key][list(row.values())[0]] = list(row.values())[1] 


# In[ ]:





# In[54]:


casesMonth = {}
reader = csv.DictReader(open('cases-month.csv')) 
for row in reader:
    key = row.pop('districtid')

    if(key not in (casesMonth)):
        casesMonth[key] = {}
    casesMonth[key][list(row.values())[0]] = list(row.values())[1] 


# In[55]:


casesOverall = {}
reader = csv.DictReader(open('cases-overall.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (casesOverall)):
        casesOverall[key] = {}
    casesOverall[key][list(row.values())[0]] = list(row.values())[1] 


# In[56]:


neighborWeek = []

for district in neighbourData:
    dId = districtId[district]
    if dId in casesWeek:
        for week in casesWeek[dId]:
            cases = []
            for neighbor in neighbourData[district]:
                if neighbor in districtId:
                    if districtId[neighbor] in casesWeek:
                        if week in casesWeek[districtId[neighbor]]:
                            cases.append(int(casesWeek[districtId[neighbor]][week]))
            mean = 0
            stdev = 0
            if(len(cases)):
                mean = sum(cases) / len(cases) 
                variance = sum([((x - mean) ** 2) for x in cases]) / len(cases) 
                stdev = variance ** 0.5
                
            neighborWeek.append({'districtid':dId ,'timeid': week,'neighbormean': round(mean, 2),'neighborstdev': round(stdev, 2)})


# In[57]:


neighborMonth = []

for district in neighbourData:
    dId = districtId[district]
    if dId in casesMonth:
        for month in casesMonth[dId]:
            cases = []
            for neighbor in neighbourData[district]:
                if neighbor in districtId:
                    if districtId[neighbor] in casesMonth:
                        if month in casesMonth[districtId[neighbor]]:
                            cases.append(int(casesMonth[districtId[neighbor]][month]))
            mean = 0
            stdev = 0
            if(len(cases)):
                mean = sum(cases) / len(cases) 
                variance = sum([((x - mean) ** 2) for x in cases]) / len(cases) 
                stdev = variance ** 0.5
                
            neighborMonth.append({'districtid':dId ,'timeid': month,'neighbormean': round(mean, 2),'neighborstdev': round(stdev, 2)})


# In[ ]:





# In[58]:


neighborOverall = []

for district in neighbourData:
    dId = districtId[district]
    if dId in casesOverall:
        for overall in casesOverall[dId]:
            cases = []
            for neighbor in neighbourData[district]:
                if neighbor in districtId:
                    if districtId[neighbor] in casesOverall:
                        if overall in casesOverall[districtId[neighbor]]:
                            cases.append(int(casesOverall[districtId[neighbor]][overall]))
            mean = 0
            stdev = 0
            if(len(cases)):
                mean = sum(cases) / len(cases) 
                variance = sum([((x - mean) ** 2) for x in cases]) / len(cases) 
                stdev = variance ** 0.5
                
            neighborOverall.append({'districtid':dId ,'timeid': overall,'neighbormean': round(mean, 2),'neighborstdev': round(stdev, 2)})
            


# In[59]:


dfWeek = pd.DataFrame(neighborWeek) 
dfWeek.to_csv (r'neighbor-week.csv', index = False, header=True)


# In[60]:


dfMonth = pd.DataFrame(neighborMonth) 
dfMonth.to_csv (r'neighbor-month.csv', index = False, header=True)


# In[61]:


dfOverall = pd.DataFrame(neighborOverall) 
dfOverall.to_csv (r'neighbor-overall.csv', index = False, header=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




