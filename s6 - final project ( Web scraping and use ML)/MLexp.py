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

# Ï?ÊÇ? ÌÏ?Ï Ñæ ÇÒ ˜ÇÑÈÑ ã??Ñå æ Èå ÝÇ?á ÇÖÇÝå ã?˜äÏ
# æ æÞÊ? ÝÇ?á ÏÇÑå ˜Ï ã?Ôå ÇØáÇÚÇÊ ÌÏ?Ï ˜ÇÑÈÑ åã ÈÇåÇÔ ˜Ï ã?Ôå ÊÇ ÈÊæä?ã ÈÚÏÔ Ï?ÊÇ? ˜Ï ÔÏå ÑÇ ÈÏ?ã Èå ÑÏ?˜Ê
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

#˜Ï ÐÇÑ? ã?˜ä?ã æä ÏÓ?Žä ÊÑ? ÇÓÊÑ?ä ÞÈæá äã?˜äå 
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    cr[column] = label_encoders[column].fit_transform(cr[column]) 

# ÍÇáÇ ˜å ˜Ï ÐÇÑ? ÔÏ ã?Ç?ã æ æÑæÏ? æ ÎÑæÌ? Ï?Ó?Žä ÊÑ? Ñæ ãÞÏÇÑ Ïå? ã?˜ä?ã
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
    
#ÂÎÑ?ä ÓØÑ æÇÑÏ ÔÏå Ï?ÊÇ? ÌÏ?Ïå Ó ÇÒ æÑæÏ? æ ÎÑæÌ? åÇ Ç ã?˜ä?ã   
# Extract the new car data and prepare it for prediction.
new_data = x.pop()
y.pop()

#ÂÎÑ?ä ÓØÑ Ñæ ÇÒ ÝÇ?á åã Ç˜ ã?˜ä?ã 
f = open('E:\workplace\python\Advanced Python\s6\dataB.csv', "r+")
lines = f.readlines()
lines.pop()
f = open('E:\workplace\python\Advanced Python\s6\dataB.csv', "w+")
f.writelines(lines)

#ÎÈ ÍÇáÇ ã?Ï?ãÔ Èå Ï?Ó?Žä ÊÑ? ÊÇ ãÏá ÈäÏ?Ôæä ˜äå
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

#Ç?äÌÇ åã ÈÑÇ? Ç?ä˜å ÈÏ?ãÔ Èå ÑÏ?˜ ?å ÂÑÇ?å ÏÑÓÊ ã?ÓÇÒ?ã æ ã?Ï?ãÔ Èå ÑÏ?˜Ê
list_new_data = []
for data in new_data:
    list_new_data.append(data)

Answer = clf.predict([list_new_data])
new_price = Answer[0]
print("you can use  price for this car : "  )
print(new_price)
