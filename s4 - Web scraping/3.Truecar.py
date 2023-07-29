'''
Write a program that fetches the price and mileage of the top 20 sellers selling a desired car 
(the car name is provided as input) from the Truecar website and stores it in a preferred database.
'''

from bs4.element import PYTHON_SPECIFIC_ENCODINGS
import requests
from bs4 import BeautifulSoup
import mysql.connector
cnx = mysql.connector.connect(host='localhost',
                                         database='cars',
                                         user='root',
                                         password='')
cursor = cnx.cursor()


x =input("model : ")
url = "https://www.truecar.com/used-cars-for-sale/listings/"+x
res = requests.get(url)
print(url)
print(res)
soup = BeautifulSoup(res.text , 'html.parser')
res = soup.find_all("div" , attrs= {"class":"card-content vehicle-card-body order-3"})
i=0
for car in res :
    x = car.find("div" , attrs= {"class":"margin-top-2_5 padding-top-2_5 border-top w-100"} )
    y = x.find("div" , attrs= {"class":"font-size-1 text-truncate"} )
    val = y.text
    val = val.split()
    if val[0]:
        mile = str(val[0])
        sql = "INSERT INTO mile VALUES (\""+mile+"\")"

        cursor.execute(sql)
    

cnx.commit()

