#!/usr/bin/env python
# coding: utf-8

# In[41]:


import json
import numpy as np
import pandas as pd
from difflib import SequenceMatcher
from collections import OrderedDict 
import requests 

f = open('neighbor-districts.json') 
neighbourData = json.load(f) 


# In[ ]:





# In[ ]:





# In[42]:


response = requests.get("https://api.covid19india.org/state_district_wise.json")


# In[ ]:





# In[ ]:





# In[43]:


def getDistrict(json_data):
    district = []
    for key, value in json_data.items():
        district = district + list(value['districtData'].keys())
    return district
       
json_data = json.loads(response.text)
districts = getDistrict(json_data)


# In[44]:


def removeOccurences(var,districts):
    i = 0
    length = len(districts)
    while(i<length):
        if(districts[i]==var):
            districts.remove(districts[i])
            length = length -1  
            continue
        i = i+1
    return districts


# In[45]:


districts = removeOccurences('Unknown',districts)
districts = removeOccurences('Other State',districts)
districts = removeOccurences('Unassigned',districts)
districts = removeOccurences('Others',districts)
districts = removeOccurences('Railway Quarantine',districts)
districts = removeOccurences('Airport Quarantine',districts)
districts = removeOccurences('Foreign Evacuees',districts)


# In[46]:


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# In[ ]:





# In[47]:


def getDistrict(districts,data):
    district_final = {}

    for district_covid in districts:
        district_new = []
        for district in data:
            district_temp = district.replace("_", " ")
            if(similar(district_temp.lower(),(district_covid.lower()))>0.24 and district_temp.lower().startswith(district_covid.lower()[0:])):
                district_new.append(district)

            elif(similar(district_temp.lower(),(district_covid.lower()))>0.5 and district_temp.lower().startswith(district_covid.lower()[0:13])):
                district_new.append(district)

        if(len(district_new)):
               district_final[district_covid + district_new[0][district_new[0].index('/'):]]=  district_new
            
    return district_final


# In[48]:


def neighbourJsonToCovidDistrict(covid_district):
    district_final = {}
    for district in covid_district:
        districts = covid_district[district]
        for d in districts:
            district_final[d] = district
    return district_final


# In[49]:


def updateNeighbourJson(neighbourData, covidDistrict, NeighbourDistrict):
    neighborDistrictsModified = {}
    for district in neighbourData:
        if district in NeighbourDistrict and len(district): # means District exits in covid portal corresponding to this district of neighbour.json file
            for neighbour in neighbourData[district]: # running through all the neighbours 
                if neighbour in NeighbourDistrict:  # checking neighbour exist in covid portal district or not 
                    if NeighbourDistrict[district] in (neighborDistrictsModified) and len(NeighbourDistrict[district]): # check district already exits or not in case of merge
                          neighborDistrictsModified[NeighbourDistrict[district]] = neighborDistrictsModified[NeighbourDistrict[district]] + [NeighbourDistrict[neighbour]]
                    elif len(NeighbourDistrict[district]):
                        neighborDistrictsModified[NeighbourDistrict[district]] = [NeighbourDistrict[neighbour]]
            
    return neighborDistrictsModified


# In[50]:


covidDistrict = getDistrict(districts,neighbourData)
NeighbourDistrict = neighbourJsonToCovidDistrict(covidDistrict)


# In[51]:


NeighbourDistrict['krishna/Q15382'] = 'Krishna/Q15382'
NeighbourDistrict['aurangabad/Q592942'] = 'Aurangabad/Q592942'
NeighbourDistrict['balrampur/Q16056268'] = 'Balrampur/Q16056268'
NeighbourDistrict['bijapur_district/Q1727570'] = ''
NeighbourDistrict['bilaspur/Q100157'] = 'Bilaspur/Q100157'
NeighbourDistrict['hamirpur/Q2019757'] = 'Hamirpur/Q2019757'
NeighbourDistrict['dharmapuri_district/Q15152'] = 'Dharmapuri/Q15152'
NeighbourDistrict['dhar/Q2299069'] = 'Dhar/Q2299069'
NeighbourDistrict['dharwad_district/Q1790904'] =  'Dharwad/Q1790904'
NeighbourDistrict['rewari/Q2301759'] = 'Rewari/Q2301759'
NeighbourDistrict['rewa/Q526862'] = 'Rewa/Q526862'
NeighbourDistrict['mahendragarh/Q684019'] =  'Mahendragarh/Q684019'
NeighbourDistrict['mahe_district/Q639279'] = 'Mahe/Q639279'
NeighbourDistrict['pratapgarh/Q1473962'] = 'Pratapgarh/Q1473962'
NeighbourDistrict['mahesana_district/Q2019694'] = ''
NeighbourDistrict['bangalore_urban/Q806463'] = 'Bengaluru Urban/Q806463'
NeighbourDistrict['bangalore_rural/Q806464'] = 'Bengaluru Rural/Q806464'
NeighbourDistrict['faizabad/Q1814132'] = 'Ayodhya/Q1814132'
NeighbourDistrict['jyotiba_phule_nagar/Q1891677'] = 'Amroha/Q1891677'
NeighbourDistrict['sant_ravidas_nagar/Q127533'] = 'Bhadohi/Q127533'
NeighbourDistrict['bijapur_district/Q1727570'] = 'Vijayapura/Q1727570'
NeighbourDistrict['palghat/Q1535742'] = 'Palakkad/Q1535742'


# In[52]:


neighborDistrictsModified = updateNeighbourJson(neighbourData, covidDistrict, NeighbourDistrict)


# In[53]:


neighborDistrictsModified = OrderedDict(sorted(neighborDistrictsModified.items())) 


# In[54]:


with open('neighbor-districts-modified.json', 'w', encoding='utf-8') as f:
    json.dump(neighborDistrictsModified, f, ensure_ascii=False, indent=4)


# In[55]:


df = pd.DataFrame(list((neighborDistrictsModified.keys())),columns = [ 'districtname'])
df.index = df.index + 101


# In[56]:


df.insert(1, "districtid", df.index, True) 


# In[57]:


df.to_csv (r'district-id.csv', index = False, header=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




