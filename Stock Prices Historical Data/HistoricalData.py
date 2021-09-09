import bs4 as bs
from datetime import datetime
import urllib.request
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

def stock_prices(stock,sdate,edate):
    
    sauce = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil?hisse"
                                   "={}&startdate={}&enddate={}".format(stock,sdate,edate)).read()
    data=json.loads(sauce)
    df=pd.DataFrame(data["value"])

    df["HGDG_TARIH"] = pd.to_datetime(df["HGDG_TARIH"], format='%d-%m-%Y')
    df.set_index("HGDG_TARIH", inplace=True)
    #df["100ma"]=df["HGDG_KAPANIS"].rolling(window=100, min_periods=0).mean()
    df.dropna(inplace=True)
    df.rename(columns={"HGDG_KAPANIS":"Close","HGDG_HACIM":"Volume"}, inplace=True)





    #print(df.head())
    #df.to_excel("Mgros"+".xlsx",sheet_name="Financial Statements")
    #plt.show()
    return df[["Volume","Close"]]