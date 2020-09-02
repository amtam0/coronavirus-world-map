#!/usr/bin/env python
# coding: utf-8

# In[3]:


import bs4 as bs
import urllib.request
import pandas as pd
import country_converter as coco

ref_headers = ['Country,Other',
  'TotalCases',
  'NewCases',
  'TotalDeaths',
  'NewDeaths',
  'TotalRecovered',
  'NewRecovered',
  'ActiveCases',
  'Serious,Critical',
  'Tot\xa0Cases/1M pop',
  'Deaths/1M pop',
  'TotalTests',
  'Tests/\n1M pop\n',
  'Population']

url='https://www.worldometers.info/coronavirus/'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

source = urllib.request.urlopen(req).read()
# source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.find('table', attrs={'id':'main_table_countries_today'})
table_rows = table.find_all('tr')
# table_rows
list_rows = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    list_rows.append(row)
list_rows = [el for el in list_rows if el]

table_header = table.find_all('th')
columns = [cell.text for cell in table_header]
df = pd.DataFrame(list_rows, columns=columns)

df = df[ref_headers]

df = df.drop_duplicates(subset= 'Country,Other', keep='first')


# In[4]:


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


# In[5]:


# Export Dataframe
df.to_csv("static/data/corona.csv",index=False,sep=",")


# ### Visualize df using Plotly (Optional)

# In[6]:


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

