from bs4.element import PYTHON_SPECIFIC_ENCODINGS
import requests
from bs4 import BeautifulSoup
import mysql.connector
import re
import pandas as pd
import csv
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import numpy as np

#connect to the db 
cnx = mysql.connector.connect(host='localhost',
                                         database='TCcars',
                                         user='root',
                                         password='')
cursor = cnx.cursor()

#get data from web : 

model_name = model = mile = accident = location = year = ""
dict_cars = dict()
list_cars = list()
for i in range(1,5):
    url = "https://www.truecar.com/used-cars-for-sale/listings/acura/?page="+str(i)
    res = requests.get(url)

    soup = BeautifulSoup(res.text , 'html.parser')
    res = soup.find_all("div" , attrs= {"class":"card-content vehicle-card-body order-3"})
    for car in res :
        x = car.find("div" , attrs= {"class":"vehicle-card-top"} )
        y = x.find("div" , attrs= {"class":"vehicle-card-header w-100"} ).text.split()

        year = y[0]
        model_name = y[1]

        z = x.find("div" , attrs= {"class":"font-size-1 text-truncate"} ).text.split()
        model = z[0]

        x = car.find("div" , attrs= {"class":"margin-top-2_5 padding-top-2_5 border-top w-100"} )
        y = x.find("div" , attrs= {"class":"font-size-1 text-truncate"} )
        val = y.text
        val = val.split()
        mile = str(val[0])
        mile = re.sub(r',','',mile)
        mile = int(mile)

        y = x.find("div" , attrs= {"class":"vehicle-card-location font-size-1 margin-top-1"} ).text.split()
        location =y[-1]

        x = car.find("div" , attrs= {"class":"vehicle-card-location font-size-1 margin-top-1" , "data-test":"vehicleCardCondition"} ).text.split()
        accident = x[0]

        x = car.find("div" , attrs= {"class":"vehicle-card-bottom vehicle-card-bottom-top-spacing"} )
        price = x.find("div" , attrs= {"class":"padding-left-3 padding-left-lg-2 vehicle-card-bottom-pricing-secondary vehicle-card-bottom-max-50"} ).text.split()
        price = price[0]
        price = price[1:]
        price = re.sub(r',','',price)
        price = int(price)

        dict_cars = {"model_name":model_name ,"model":model , "mile":mile ,"accident":accident,"location":location, "year":year , "price":price}
        list_cars.append(dict_cars)
#add data to db :
    
cursor.executemany("""
    INSERT INTO cars (model_name,model,mile,accident,location,year,price)
    VALUES (%(model_name)s, %(model)s ,%(mile)s,%(accident)s,%(location)s,%(year)s,%(price)s)""", list_cars)

cnx.commit()

# create csv and add data to csv file :
query = 'select * from cars'
cursor.execute(query)
with open("E:\workplace\python\Advanced Python\s6\dataB.csv","w") as outfile:
    writer = csv.writer(outfile, delimiter=',', quotechar='"' , quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(col[0] for col in cursor.description)
    for row in cursor:
        if row:
            writer.writerow(row)

df = pd.read_csv('E:\workplace\python\Advanced Python\s6\dataB.csv')
df.to_csv('E:\workplace\python\Advanced Python\s6\dataB.csv', index=False)

print("your data aded to the dataB.csv , now you can go and run MLexp.py :)")