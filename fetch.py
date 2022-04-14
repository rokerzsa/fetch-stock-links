#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import json
import mariadb
import sys
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="stock_information"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','others']

for i in range(len(alphabets)):
    url = 'https://www.moneycontrol.com/india/stockpricequote/'+alphabets[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stocks = soup.find_all('a', {'class':'bl_12'})
    stocklen = len(stocks)
    otpt = []
    for j in range(stocklen):
        try:
            cur.execute("INSERT INTO all_stocks_mc (stock_name,stock_url) VALUES (?,?)", (stocks[j].text, stocks[j]["href"]))
        except mariadb.Error as e:
            print(f"Error: {e}")
print("End")
#Close Connection
conn.commit()
conn.close()
