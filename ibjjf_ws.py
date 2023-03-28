import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
URL = "https://www.ibjjfdb.com/ChampionshipResults/1877/PublicResults"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'class':"col-xs-12 col-md-6 col-athlete"}) 

athletes = []
    
#for each division break down table to age, sex, rank, weight
for row in table.findAll('div', attrs = {'class': 'athlete-item'}):
    athlete={}

    athlete['place'] = row.div.text.strip().split('\n')[0]
    athlete['name'] = row.p.text.strip().split("\n")[0]
    athlete['team'] = row.span.text.strip().split("\n")[0]

    division = row.findPrevious('h4', attrs = {'class':'subtitle'})
    #print(newString)

    #strip out white space
    noSpace = division.text.strip()
    #split data at each slash
    processed = noSpace.split('/')  

    athlete['age'] = processed[0].strip()
    athlete['sex'] = processed[1].strip()
    athlete['rank'] = processed[2].strip()
    athlete['weight'] = processed[3].strip()

    athletes.append(athlete)
    

#To Do: write function for text parser

#write athlete data to csv
with open("results.csv", 'w', newline = '') as file:
    writer = csv.DictWriter(file, delimiter=",", fieldnames=['name','team','place','age','sex','rank', 'weight'])
    writer.writeheader()
    for athlete in athletes:
        writer.writerow(athlete)
