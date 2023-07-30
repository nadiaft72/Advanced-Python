# Program to Fetch and Store Car Prices and Mileage from Truecar Website:
# This program fetches the price and mileage of the top 20 sellers selling a desired car (car name provided as input) from the Truecar website.
# The extracted data is stored in a preferred MySQL database called 'cars'.
# It uses Python's requests and BeautifulSoup libraries for web scraping and parsing the HTML content.
# The program prompts the user for the car model, then fetches the data and stores the mileage in the 'mile' table of the database.

from bs4.element import PYTHON_SPECIFIC_ENCODINGS
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Establish connection to the MySQL database 'cars'.
cnx = mysql.connector.connect(host='localhost',
                                         database='cars',
                                         user='root',
                                         password='')
cursor = cnx.cursor()

# Get the car model as input from the user.
x =input("model : ")

# Create the URL for the Truecar website with the provided car model.
url = "https://www.truecar.com/used-cars-for-sale/listings/"+x

# Fetch the HTML content of the Truecar website for the specified car model.
res = requests.get(url)

# Parse the HTML content using BeautifulSoup.
soup = BeautifulSoup(res.text , 'html.parser')

# Find all the elements with the class "card-content vehicle-card-body order-3," which represent the car ads on the page.
res = soup.find_all("div" , attrs= {"class":"card-content vehicle-card-body order-3"})

# Loop through each car ad and extract the mileage data.
# Store the extracted mileage data in the 'mile' table of the database.
for car in res :
    x = car.find("div" , attrs= {"class":"margin-top-2_5 padding-top-2_5 border-top w-100"} )
    y = x.find("div" , attrs= {"class":"font-size-1 text-truncate"} )
    val = y.text
    val = val.split()
    if val[0]:
        mile = str(val[0])
        sql = "INSERT INTO mile VALUES (\""+mile+"\")"

        cursor.execute(sql)
      
# Commit the changes to the database.
cnx.commit()

