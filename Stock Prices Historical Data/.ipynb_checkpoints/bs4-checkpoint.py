import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import Request, urlopen
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import os



urlheader = {
    "authority": "www.investing.com",
    "accept": "text/plain, */*; q=0.01",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
  "x-requested-with": "XMLHttpRequest",
   "sec-fetch-dest":"empty",
    "sec-fetch-mode": "cors"
}

url = "https://www.investing.com/instruments/HistoricalDataAjax"


payload = {"curr_id":"19509" ,
           "smlID":"1167417",
           "header": "MGROS+Historical+Data",
           "st_date": "06/29/2015",
           "end_date": '07/28/2021',
           "interval_sec":"Daily",
           "sort_col": "date",
           "sort_ord":"DESC",
           "action": "historical_data"}

req = requests.post(url, data=payload, headers=urlheader)


soup = BeautifulSoup(req.content, "lxml")

print(soup.text)
#table = soup.find("table")

#for row in table.find