# lblEnc.py - Label Encoding and Machine Learning

# Importing necessary librariesfrom bs4.element import PYTHON_SPECIFIC_ENCODINGS
import numpy as np
import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import csv
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

# Reading data from 'dataB.csv' using pandas
cr = pd.read_csv("E:\workplace\python\Advanced Python\s6\dataB.csv")

# Label Encoding for categorical columns
label_encoders = {}
categorical_columns = ["model_name" ,"model"  ,"accident","location", "year" ]

# Perform label encoding for each categorical column and transform the data
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    cr[column] = label_encoders[column].fit_transform(cr[column]) 

# Splitting the first row of the dataset into individual data points
x = np.split(cr.values[0] ,7 )
for line in x:
    print(int(line))

# Initializing empty lists x and y to store feature and target data
x=[]
y=[]

# Splitting the data into features (x) and target (y)
for line in cr.values:
    z = np.split(line ,7)
    w=[]
    for zline in z:
        w.append(int(zline))
    x.append(line[0:6])
    y.append(line[6])

# Creating a Decision Tree classifier and fitting the data
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

