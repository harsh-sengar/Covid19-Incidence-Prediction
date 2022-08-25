#!/usr/bin/env python
# coding: utf-8

# In[100]:


import json
import numpy as np
import pandas as pd
from difflib import SequenceMatcher
from collections import OrderedDict 
import requests 
import csv

f = open('data-all.json') 
dataAll = json.load(f) 


# In[101]:


reader = csv.DictReader(open('district-id.csv'))

districtId = {}
for row in reader:
    key = row.pop('districtname')
    districtId[key[:key.index('/')]] = list(row.values())[0]


# In[102]:


covidDistrictId = {}
a = {}
for state in dataAll['2020-09-05']:
    covidDistrictId[state] = {}
    if "districts" in dataAll['2020-09-05'][state]:
        for district in dataAll['2020-09-05'][state]["districts"]:
            if district in districtId:
                covidDistrictId[state][districtId[district]] = district
                a[district+state] = districtId[district]


# In[103]:


del covidDistrictId['UP']['313']
del covidDistrictId['BR']['132'] 
del covidDistrictId['CT']['185']
del covidDistrictId['UP']['565']
del covidDistrictId['CT']['146']
covidDistrictId['UP']['312'] = 'Hamirpur'
covidDistrictId['BR']['131'] = 'Aurangabad'
covidDistrictId['CT']['184'] = 'Bilaspur'
covidDistrictId['UP']['564'] = 'Pratapgarh'
covidDistrictId['CT']['145'] = 'Balrampur'


# In[104]:


reader = csv.DictReader(open('district-id.csv'))
districtId = {}
for row in reader:
    key = row.pop('districtname')
    districtId[key] = list(row.values())[0]


# In[105]:


covidSate = {}
for state in covidDistrictId:
    for dId in covidDistrictId[state]:
        covidSate[dId] = state


# In[106]:


casesWeek = {}
reader = csv.DictReader(open('cases-week.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (casesWeek)):
        casesWeek[key] = {}
    casesWeek[key][list(row.values())[0]] = list(row.values())[1] 

casesMonth = {}
reader = csv.DictReader(open('cases-month.csv')) 
for row in reader:
    key = row.pop('districtid')

    if(key not in (casesMonth)):
        casesMonth[key] = {}
    casesMonth[key][list(row.values())[0]] = list(row.values())[1] 
    
casesOverall = {}
reader = csv.DictReader(open('cases-overall.csv')) 
for row in reader:
    key = row.pop('districtid')
    if(key not in (casesOverall)):
        casesOverall[key] = {}
    casesOverall[key][list(row.values())[0]] = list(row.values())[1] 
    


# In[107]:


len(districtId)


# In[108]:


districtStateWeek = []

for dId in districtId.values():
    if dId in casesWeek:
        for week in casesWeek[dId]:
            state = covidSate[dId]
            cases = []
            for district in covidDistrictId[state]:
                if district != dId:
                    if district in casesWeek:
                        if week in casesWeek[district]:
                                    cases.append(int(casesWeek[district][week]))
            mean = 0
            stdev = 0
            if(len(cases)):
                mean = sum(cases) / len(cases) 
                variance = sum([((x - mean) ** 2) for x in cases]) / len(cases) 
                stdev = variance ** 0.5
                
            districtStateWeek.append({'districtid':dId ,'timeid': week,'statemean': round(mean, 2),'statestdev': round(stdev, 2)})


# In[109]:


districtStateMonth = []

for dId in districtId.values():
    if dId in casesMonth:
        for month in casesMonth[dId]:
            state = covidSate[dId]
            cases = []
            for district in covidDistrictId[state]:
                if district != dId:
                    if district in casesMonth:
                        if month in casesMonth[district]:
                                    cases.append(int(casesMonth[district][month]))
            mean = 0
            stdev = 0
            if(len(cases)):
                mean = sum(cases) / len(cases) 
                variance = sum([((x - mean) ** 2) for x in cases]) / len(cases) 
                stdev = variance ** 0.5
                
            districtStateMonth.append({'districtid':dId ,'timeid': month,'statemean': round(mean, 2),'statestdev': round(stdev, 2)})


# In[110]:


districtStateOverall = []

for dId in districtId.values():
    if dId in casesOverall:
        for overall in casesOverall[dId]:
            state = covidSate[dId]
            cases = []
            for district in covidDistrictId[state]:
                if district != dId:
                    if district in casesOverall:
                        if overall in casesOverall[district]:
                                    cases.append(int(casesOverall[district][overall]))
            mean = 0
            stdev = 0
            if(len(cases)):
                mean = sum(cases) / len(cases) 
                variance = sum([((x - mean) ** 2) for x in cases]) / len(cases) 
                stdev = variance ** 0.5
                
            districtStateOverall.append({'districtid':dId ,'timeid': overall,'statemean': round(mean, 2),'statestdev': round(stdev, 2)})


# In[ ]:





# In[ ]:





# In[ ]:





# In[111]:


dfWeek = pd.DataFrame(districtStateWeek) 
dfWeek.to_csv (r'state-week.csv', index = False, header=True)


# In[112]:


dfMonth = pd.DataFrame(districtStateMonth) 
dfMonth.to_csv (r'state-month.csv', index = False, header=True)


# In[113]:


dfOverall = pd.DataFrame(districtStateOverall) 
dfOverall.to_csv (r'state-overall.csv', index = False, header=True)


# In[ ]:





# In[ ]:





# In[ ]:




