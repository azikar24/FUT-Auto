from bs4 import BeautifulSoup
import requests
import time
import lxml.html
import requests 
import csv
import pandas
import os
   
URL = 'https://www.futwiz.com/en/settings/playstation?return=/en/fifa20/players'
page = requests.get(URL) 

start = time.time() 
cwd = os.getcwd()+"\\"  
page_num = 733 
players = {} 
print("Starting")
for indx in range(1, page_num):
    print("Working on page " + str(indx))
    URL = 'https://www.futwiz.com/en/fifa20/players?page=' + str(indx) 
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features="html.parser")
    rows = soup.find_all('tr')
    for i, row in enumerate(rows):
        col = row.findAll('td')
        if i == 0 or len(col) < 15:
            continue
        link = col[1].find('a')['href'].split()
        link = link[len(link) - 1].strip() 
        name = col[1].getText().split("\n")[3]
        price = col[4].getText().split("\n")[1] 
        if(len(price) > 1):        
            players[name] = price + ";" + link
         
    print("Done with page " + str(indx))
print("Done, Saving...")

with open(cwd+'Players.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for key in players:
        print(key + " " + players[key])
        employee_writer.writerow([key, players[key]])
print("Task Completed")
end = time.time()
print("Time Taken = " + str(end-start))

 