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
for row in table.findAll('h4', attrs = {'class': 'subtitle'}):
    athlete={}
    #strip out white space
    noSpace = row.text.strip()
    #split data at each slash
    processed = noSpace.split('/')

    #TO DO: Write code to parse athlete name/placement text
    #Right now code is only pulling last name from list
    for section in table.findAll('div', attrs = {'class': 'athlete-item'}):
        nextNode = section
        name = section.div.text.strip()
        nameOne = name.strip().split('\n')[0]
        nameTwo = section.p.text.strip().split("\n")[0]
        nameThree = section.span.text.strip().split("\n")[0]

        athlete['name'] = nameTwo
        athlete['team'] = nameThree
        athlete['place'] = nameOne
        athlete['age'] = processed[0].strip()
        athlete['sex'] = processed[1].strip()
        athlete['rank'] = processed[2].strip()
        athlete['weight'] = processed[3].strip()
        
        while True:
            nextNode = nextNode.nextSibling
            try:
                tag_name = nextNode.name
            except AttributeError:
                tag_name = ""
            if tag_name == "subtitle":
                print(nextNode.text)
            break
    
    athletes.append(athlete)

#To Do: write function for text parser

#write athlete data to csv
with open("results.csv", 'w', newline = '') as file:
    writer = csv.DictWriter(file, delimiter=",", fieldnames=['name','team','place','age','sex','rank', 'weight'])
    writer.writeheader()
    for athlete in athletes:
        writer.writerow(athlete)
