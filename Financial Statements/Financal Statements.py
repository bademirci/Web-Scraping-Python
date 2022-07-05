# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 22:02:04 2021

@author: batuhan
"""
import bs4 as bs
import urllib.request
import json
import pandas as pd
                                #Bilanco verilerini elde etmek için oluşturduğum kod.
 
hisse = "KONTR"
sauce15 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=6&year2=2021&period2=9&year3=2021&period3=12&year4=2022&period4=3&_=1620763995205".format(hisse)).read()
data15 = json.loads(sauce15)

sauce = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2020&period2=12&year3=2020&period3=9&year4=2020&period4=6&_=1620763995205".format(hisse)).read()
data = json.loads(sauce)

sauce2 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2020&period2=3&year3=2019&period3=12&year4=2019&period4=9&_=1620763995205".format(hisse)).read()
data2 = json.loads(sauce2)

sauce3 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2019&period2=6&year3=2019&period3=3&year4=2018&period4=12&_=1620763995205".format(hisse)).read()
data3 = json.loads(sauce3)

sauce4 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2018&period2=9&year3=2018&period3=6&year4=2018&period4=3&_=1620763995205".format(hisse)).read()
data4 = json.loads(sauce4)

sauce5 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2017&period2=12&year3=2017&period3=9&year4=2017&period4=6&_=1620763995205".format(hisse)).read()
data5 = json.loads(sauce5)

sauce6 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2017&period2=3&year3=2016&period3=12&year4=2016&period4=9&_=1620763995205".format(hisse)).read()
data6 = json.loads(sauce6)

sauce7 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2016&period2=6&year3=2016&period3=3&year4=2015&period4=12&_=1620763995205".format(hisse)).read()
data7 = json.loads(sauce7)

sauce8 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2015&period2=9&year3=2015&period3=6&year4=2015&period4=3&_=1620763995205".format(hisse)).read()
data8 = json.loads(sauce8)

sauce9 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2014&period2=12&year3=2014&period3=9&year4=2014&period4=6&_=1620763995205".format(hisse)).read()
data9 = json.loads(sauce9)

sauce10 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2014&period2=3&year3=2013&period3=12&year4=2013&period4=9&_=1620763995205".format(hisse)).read()
data10 = json.loads(sauce10)

sauce11 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2013&period2=6&year3=2013&period3=3&year4=2012&period4=12&_=1620763995205".format(hisse)).read()
data11 = json.loads(sauce11)

sauce12 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2012&period2=9&year3=2012&period3=6&year4=2012&period4=3&_=1620763995205".format(hisse)).read()
data12 = json.loads(sauce12)

sauce13 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2011&period2=12&year3=2011&period3=9&year4=2011&period4=6&_=1620763995205".format(hisse)).read()
data13 = json.loads(sauce13)

sauce14 = urllib.request.urlopen("https://www.isyatirim.com.tr/_layouts/15/IsYatirim.Website/Common/Data.aspx/MaliTablo?companyCode={}&exchange=TRY&financialGroup=XI_29&year1=2021&period1=3&year2=2011&period2=3&year3=2010&period3=12&year4=2010&period4=9&_=1620763995205".format(hisse)).read()
data14 = json.loads(sauce14)


cols =["Kalem",
        "2022-3","2021-12","2021-9","2021-6",
        "2021-3","2020-12","2020-9","2020-6",
        "2020-3","2019-12","2019-9","2019-6",
        "2019-3","2018-12","2018-9","2018-6",
        "2018-3","2017-12","2017-9","2017-6",
        "2017-3","2016-12","2016-9","2016-6",
        "2016-3","2015-12","2015-9","2015-6",
        "2015-3","2014-12","2014-9","2014-6",
        "2014-3","2013-12","2013-9","2013-6",
        "2013-3","2012-12","2012-9","2012-6",
        "2012-3","2011-12","2011-9","2011-6",
        "2011-3","2010-12","2010-9"

       ]
df = pd.DataFrame(columns=cols)

for x in range(len(data15["value"])):

    df2 = pd.DataFrame({"Kalem": data["value"][x]["itemDescTr"],
                    "2021-12": data15["value"][x]["value3"],
                    "2021-9": data15["value"][x]["value2"],
                    "2021-6": data15["value"][x]["value1"],
                    "2021-3":data["value"][x]["value1"],
                    "2020-12":data["value"][x]["value2"],
                    "2020-9": data["value"][x]["value3"],
                    "2020-6": data["value"][x]["value4"],
                    "2020-3":data2["value"][x]["value2"],
                    "2019-12":data2["value"][x]["value3"],
                    "2019-9": data2["value"][x]["value4"],
                    "2019-6": data3["value"][x]["value2"],
                    "2019-3": data3["value"][x]["value3"],
                    "2018-12": data3["value"][x]["value4"],
                    "2018-9": data4["value"][x]["value2"],
                    "2018-6": data4["value"][x]["value3"],
                    "2018-3": data4["value"][x]["value4"],
                    "2017-12": data5["value"][x]["value2"],
                    "2017-9": data5["value"][x]["value3"],
                    "2017-6": data5["value"][x]["value4"],
                    "2017-3": data6["value"][x]["value2"],
                    "2016-12": data6["value"][x]["value3"],
                    "2016-9": data6["value"][x]["value4"],
                    "2016-6": data7["value"][x]["value2"],
                    "2016-3": data7["value"][x]["value3"],
                    "2015-12": data7["value"][x]["value4"],
                    "2015-9": data8["value"][x]["value2"],
                    "2015-6": data8["value"][x]["value3"],
                    "2015-3": data8["value"][x]["value4"],
                    "2014-12": data9["value"][x]["value2"],
                    "2014-9": data9["value"][x]["value3"],
                    "2014-6": data9["value"][x]["value4"],
                    "2014-3": data10["value"][x]["value2"],
                    "2013-12": data10["value"][x]["value3"],
                    "2013-9": data10["value"][x]["value4"],
                    "2013-6": data11["value"][x]["value2"],
                    "2013-3": data11["value"][x]["value3"],
                    "2012-12": data11["value"][x]["value4"],
                    "2012-9": data12["value"][x]["value2"],
                    "2012-6": data12["value"][x]["value3"],
                    "2012-3": data12["value"][x]["value4"],
                    "2011-12": data13["value"][x]["value2"],
                    "2011-9": data13["value"][x]["value3"],
                    "2011-6": data13["value"][x]["value4"],
                    "2011-3": data14["value"][x]["value2"],
                    "2010-12": data14["value"][x]["value3"],
                    "2010-9": data14["value"][x]["value4"]


                    },index=[0])

    df = pd.concat([df, df2], ignore_index = True)
df[df.columns[1:]] = (df[df.columns[1:]].astype(float)/1000000)
#df[df.columns[1:]] = (df[df.columns[1:]].style.format('${0:,.2f}'))
df.to_excel(hisse+".xlsx",sheet_name=hisse)

