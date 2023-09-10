from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():
                   
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Find <table>
        bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        
        # Find <tbody>
        table_body = bright_star_table.find('tbody')

        # Find <tr>
        table_rows = table_body.find_all('tr')

        # Get data from <td>
        for row in table_rows:
            table_cols = row.find_all('td')
            print(table_cols)
            
            temp_list = []

            for col_data in table_cols:
                print(col_data.text)

                data = col_data.text.strip()
                print(data)

                temp_list.append(data)


            scraped_data.append(temp_list)


scrape()

stars_data = []

for i in range(0,len(scraped_data)):
    
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)


headers = ['Star_name','Distance','Mass','Radius','Luminosity']  

starDataFrame = pd.DataFrame(stars_data, columns=headers)

starDataFrame.to_csv('scraped_data.csv',index=True, index_label="id")