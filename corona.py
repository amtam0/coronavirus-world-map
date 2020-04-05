#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import lxml.html as lh
import pandas as pd
import numpy as np
import country_converter as coco
import itertools


# ### Build df from Url

# In[7]:


url='https://www.worldometers.info/coronavirus/'

# Scraping the Url
page = requests.get(url)
doc = lh.fromstring(page.content)
todaydoc = doc.get_element_by_id("main_table_countries_today")

# Parse data
th_elements = todaydoc.xpath('//th') # header
td_elements = todaydoc.xpath('//td') # cells content

headers = [th_element.text_content() for th_element in th_elements]
headers = headers[:len(headers)//2]

content = [td_element.text_content() for td_element in td_elements]
rows_content = np.array(content).reshape(int(len(content)/len(headers)),len(headers)).tolist()[:-1] #rm Today row
rows_content = list(k for k,_ in itertools.groupby(rows_content))

df = pd.DataFrame(rows_content)
df.columns = headers
df = df.drop_duplicates(subset= 'Country,Other', keep='first')


# In[8]:


# Convert values to float
for i,col_name in enumerate(df.columns):
    print
    if i!=0:
        df[col_name] = pd.to_numeric(df[col_name].apply(lambda x:x.replace(",","")),errors='coerce')
        
# Convert country to ISO codes
countries_list = df["Country,Other"].apply(lambda x: x.strip()).replace({'UK': 'Great Britain', 'UAE': 'United Arab Emirates'}).values.tolist()
df["iso_alpha"] = pd.Series(coco.convert(names=countries_list, to='ISO3', not_found=None))

# Rename comma seperated cols
df = df.rename(columns={'Country,Other': 'Country',
                  'Serious,Critical': 'Critical'})

df = df.fillna(0)

# Create text that will be display on hover
df["text"] = df['Country'].apply(lambda x: x.strip()) + '<br>' +     'Active Cases ' + df['ActiveCases'].astype(int).astype(str) +     '<br>' + 'Total Deaths ' + df['TotalDeaths'].astype(int).astype(str)


# In[9]:


# Export Dataframe
df.to_csv("static/data/corona.csv",index=False,sep=",")


# ### Visualize df using Plotly (Optional)

# In[10]:


# import plotly.express as px
# import datetime
# today_date = datetime.datetime.today().date().strftime("%d-%m-%Y")
# fig = px.choropleth(df, locations="iso_alpha",
#                     color="TotalCases",
#                     hover_name="Country",
#                     color_continuous_scale=px.colors.diverging.Portland,
#                    title='Daily Coronavirus Cases in the Word [{}]'.format(today_date)\
#                     +' Source: <a https://www.worldometers.info/coronavirus/">Worldometers</a>',
#                    height=600,
#                    range_color=[0,1000],
#                    labels={'TotalCases':'Min Number of cases'})
# fig.show()

