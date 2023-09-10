from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(URL)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table', {"class":"wikitable sortable"})

total_table = len(star_table)
print(total_table)

temporary = []


table_rows = star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.strip() for i in td]
    temporary.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temporary)

for i in range(1,len(temporary)):
    
    Star_names.append(temporary[i][0])
    Distance.append(temporary[i][5])
    Mass.append(temporary[i][7])
    Radius.append(temporary[i][8])

# Convert to CSV
headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")