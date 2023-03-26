import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
URL = "https://www.ibjjfdb.com/ChampionshipResults/1877/PublicResults"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'content'}) 
# print(table)

athletes = []

for row in table.findAll('h4', attrs = {'class': 'subtitle'}):
    athlete={}
    athlete['division'] = row
    print(row)
    athletes.append(athlete)

#print(athletes)

# with open("results.csv", 'w', newline = '') as file:
#     writer = csv.writer(file)
#     for i in table:
#         writer.writerow(i)
