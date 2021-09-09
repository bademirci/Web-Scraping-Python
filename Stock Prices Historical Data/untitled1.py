# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:18:05 2021

@author: batuhan
"""
import HistoricalData as sp
import pandas as pd
import os
import csv


first_df = pd.read_excel("Endeks.xlsx")
first_df["BIST TÜM"].dropna(inplace=True)

if not os.path.exists('stock_dfs'):
    os.makedirs('stock_dfs')

sdate="31-07-2021"
edate="07-09-2021"

# for ticker in first_df["BIST TÜM"]:
#     if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
#         df = sp.stock_prices(ticker, sdate, edate)
#         df.to_csv('stock_dfs/{}.csv'.format(ticker))
#     else:
#         print('Already have {}'.format(ticker))


for ticker in first_df["BIST TÜM"]:
    new_df = sp.stock_prices(ticker, sdate, edate)
    new_df.to_csv('stock_dfs/{}.csv'.format(ticker), mode = "a", index=True, header=False)