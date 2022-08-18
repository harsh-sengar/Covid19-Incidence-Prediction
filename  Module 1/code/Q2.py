#!/usr/bin/env python
# coding: utf-8

# In[61]:


import json
import numpy as np
import pandas as pd
from difflib import SequenceMatcher
from collections import OrderedDict 
import requests 

f = open('neighbor-districts-modified.json') 
neighbourData = json.load(f) 
f1 = open('data-all.json') 
dataAll = json.load(f1) 


# In[62]:


df = pd.DataFrame(list((neighbourData.keys())),columns = [ 'districtname'])
district = []
for i in  range(len(df)): 
    district.append(df['districtname'][i][:(df['districtname'][i].index('/'))])
    
df.index = df.index + 101
df.insert(1, "districtid", df.index, True) 
df.insert(1, "districtnamecovid", district , True) 


# In[63]:


districtId = pd.Series(df.districtid.values,index=df.districtnamecovid).to_dict()
districtname = pd.Series(df.districtname.values,index=df.districtid).to_dict()


# In[ ]:





# In[64]:


covidDistrictId = {}
a = {}
for state in dataAll['2020-09-05']:
    covidDistrictId[state] = {}
    if "districts" in dataAll['2020-09-05'][state]:
        for district in dataAll['2020-09-05'][state]["districts"]:
            if district in districtId:
                covidDistrictId[state][district] = districtId[district]
                a[district+state] = districtId[district]


# In[ ]:





# In[65]:


covidDistrictId['UP']['Hamirpur'] = 312
covidDistrictId['BR']['Aurangabad'] = 131
covidDistrictId['CT']['Bilaspur'] = 184
covidDistrictId['UP']['Pratapgarh'] = 564
covidDistrictId['CT']['Balrampur'] = 145


# In[ ]:





# In[66]:


dayCount = 0
week = 1
casesWeek = {}
casesMonth = {}
casesOverall = {}

for date in dataAll:
    
    day = int(date[8:11])
    month = int(date[5:7])
    overall = 1
    
    if (month == 3 and day >= 15) or (month >= 4 and month <=8) or (month == 9 and day <= 5):
        for state in dataAll[date]:
        
            if "districts" in dataAll[date][state]:
                for district in dataAll[date][state]["districts"]:
                    if district in districtId:
                        if "delta" in dataAll[date][state]["districts"][district]:
                            if "confirmed" in dataAll[date][state]["districts"][district]["delta"]:
                                if (covidDistrictId[state][district] in casesWeek) and (covidDistrictId[state][district] in casesMonth) and (covidDistrictId[state][district] in casesOverall):
                                    if (week in casesWeek[covidDistrictId[state][district]]):
                                        casesWeek[covidDistrictId[state][district]][week] = casesWeek[covidDistrictId[state][district]][week] + dataAll[date][state]["districts"][district]["delta"]['confirmed']
    
                                    else:
                                        casesWeek[covidDistrictId[state][district]][week] = dataAll[date][state]["districts"][district]["delta"]["confirmed"]
                                        
                                    if (month in casesMonth[covidDistrictId[state][district]]):
                                        casesMonth[covidDistrictId[state][district]][month-2] = casesMonth[covidDistrictId[state][district]][month] + dataAll[date][state]["districts"][district]["delta"]['confirmed']
                
                                    else:
                                        casesMonth[covidDistrictId[state][district]][month-2] = dataAll[date][state]["districts"][district]["delta"]["confirmed"]
                            
                                        
                                    if (overall in casesOverall[covidDistrictId[state][district]]):
                                        casesOverall[covidDistrictId[state][district]][overall] = casesOverall[covidDistrictId[state][district]][overall] + dataAll[date][state]["districts"][district]["delta"]["confirmed"]
                               
                                    else:
                                        casesOverall[covidDistrictId[state][district]][overall] = dataAll[date][state]["districts"][district]["delta"]["confirmed"]
                                        
                            
                                else:
                                    casesWeek[covidDistrictId[state][district]] = {}
                                    casesMonth[covidDistrictId[state][district]] = {}
                                    casesOverall[covidDistrictId[state][district]] = {}
                                    casesWeek[covidDistrictId[state][district]][week] = dataAll[date][state]["districts"][district]["delta"]["confirmed"]
                                    casesMonth[covidDistrictId[state][district]][month-2] = dataAll[date][state]["districts"][district]["delta"]["confirmed"]
                                    casesOverall[covidDistrictId[state][district]][overall] = dataAll[date][state]["districts"][district]["delta"]["confirmed"]
                               
                      
        dayCount = dayCount + 1  
        if dayCount == 7:
            dayCount = 0
            week = week + 1



# In[ ]:





# In[67]:


rows = [] 

for data in casesWeek: 
    data_row = casesWeek[data]
    districtId = data
    row = {}
    for time in data_row: 
        rows.append({'districtid':districtId, 'timeid': time, 'cases':data_row[time] }) 

dfWeek = pd.DataFrame(rows) 


# In[68]:


rows = [] 

for data in casesMonth: 
    data_row = casesMonth[data]
    districtId = data
    row = {}
    for time in data_row: 
        rows.append({'districtid':districtId, 'timeid': time, 'cases':data_row[time] }) 

dfMonth = pd.DataFrame(rows) 


# In[69]:


rows = [] 

for data in casesOverall: 
    data_row = casesOverall[data]
    districtId = data
    row = {}
    for time in data_row: 
        rows.append({'districtid':districtId, 'timeid': time, 'cases':data_row[time] }) 

dfOverall = pd.DataFrame(rows) 


# In[70]:


dfWeek.to_csv (r'cases-week.csv', index = False, header=True)


# In[71]:


dfMonth.to_csv (r'cases-month.csv', index = False, header=True)


# In[72]:


dfOverall.to_csv (r'cases-overall.csv', index = False, header=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




