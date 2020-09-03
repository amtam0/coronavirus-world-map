import json
import bs4 as bs
import urllib.request
import pandas as pd
import country_converter as coco
import os
# import boto3
from git import Repo

def lambda_handler(event, context):

    #Clone Github Repo
    full_local_path = "/tmp/coronavirus-world-map"
    username = os.environ['github_name']
    password = os.environ['github_pass']
    repo = os.environ['github_repo']
    remote = f"https://{username}:{password}@github.com/{username}/{repo}"
    Repo.clone_from(remote, full_local_path)

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
    soup = bs.BeautifulSoup(source,'html.parser')
    
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

    # Export Dataframe
    lambda_path = "/tmp/coronavirus-world-map/static/data/corona.csv"
    df.to_csv(lambda_path,index=False,sep=",")
    
    # #write to S3
    # s3 = boto3.resource('s3')
    # bucket_name = ""
    # s3_path = "data/corona.csv"
    # bucket = s3.Bucket(bucket_name)
    # bucket.upload_file(lambda_path, s3_path)
    
    #Push to github
    repo = Repo(full_local_path)
    repo.git.add("{}/static/data/".format(full_local_path))
    repo.index.commit("autoupdate dataset from AWS lambda")
    origin = repo.remote(name="origin")
    origin.push()
    
    return {
        'statusCode': 200,
        'body': json.dumps('executed !')
    }

