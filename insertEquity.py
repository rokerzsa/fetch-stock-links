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
file = open('data.json')
data = json.load(file)
for element in data:
    if(element['SERIES'] == 'EQ'):
        sym = element['SYMBOL']
        com_name = element['NAME OF COMPANY']
        exch = element['EXCHANGE']
        isin = element['ISIN NUMBER']
        try:
            cur.execute("INSERT INTO equity_list (symbol,company_name,exchange,isin_number) VALUES (?,?,?,?)",
                        (sym, com_name, exch, isin)
                        )
        except mariadb.Error as e:
            print(f"Error: {e}")
file.close()
conn.commit()
conn.close()
