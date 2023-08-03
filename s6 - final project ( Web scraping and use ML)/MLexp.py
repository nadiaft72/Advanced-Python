# MLexp.py - Car Price Prediction Using Machine Learning

from typing import AnyStr
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

# Read the car data from the CSV file 'dataB.csv' using pandas.
cr = pd.read_csv("E:\workplace\python\Advanced Python\s6\dataB.csv")

# Collect new car data from the user or use the default data (Acura, SH-AWD, 1046, 2, CA, 2019, 0).
new_data = "Acura,SH-AWD,1046,2,CA,2019,0"
yOrn = input("We considered the following data : Acura,SH-AWD,1046,2,CA,2019,0 , if you wanna add another data enter y else enter n :")
if yOrn == "y" or yOrn== "Y":
    new_data = input("plz enter the current model_name,model,mile,accident,location,year,price : ")
new_data = new_data + "\n"

# Append the new car data to the CSV file 'dataB.csv'.
with open('E:\workplace\python\Advanced Python\s6\dataB.csv','a') as fd:
    fd.write(new_data)


# Encode categorical columns ('model_name', 'model', 'accident', 'location', 'year') using LabelEncoder.
label_encoders = {}
categorical_columns = ["model_name" ,"model"  ,"accident","location", "year" ]
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    cr[column] = label_encoders[column].fit_transform(cr[column]) 

# Prepare features (x) and target variable (y) for the Machine Learning model.
x=[]
y=[]
for line in cr.values:
    z = np.split(line ,7)
    w=[]
    for zline in z:
        w.append(int(zline))
    x.append(line[0:6])
    y.append(line[6])
    
# Extract the new car data and prepare it for prediction.
new_data = x.pop()
y.pop()

# Remove the last line from the CSV file to remove the appended new car data.
f = open('E:\workplace\python\Advanced Python\s6\dataB.csv', "r+")
lines = f.readlines()
lines.pop()
f = open('E:\workplace\python\Advanced Python\s6\dataB.csv', "w+")
f.writelines(lines)

# Train the DecisionTreeClassifier on the dataset and make a price prediction for the new car data.
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
list_new_data = []
for data in new_data:
    list_new_data.append(data)
Answer = clf.predict([list_new_data])
new_price = Answer[0]

# Display the predicted price for the new car data.
print("you can use  price for this car : "  )
print(new_price)
