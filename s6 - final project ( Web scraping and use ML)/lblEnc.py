# ML :
from bs4.element import PYTHON_SPECIFIC_ENCODINGS
import numpy as np
import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import csv
from sklearn import tree
from sklearn.preprocessing import LabelEncoder


cr = pd.read_csv("E:\workplace\python\Advanced Python\s6\dataB.csv")


label_encoders = {}
categorical_columns = ["model_name" ,"model"  ,"accident","location", "year" ]

for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    cr[column] = label_encoders[column].fit_transform(cr[column]) 

x = np.split(cr.values[0] ,7 )
for line in x:
    print(int(line))
x=[]
y=[]

for line in cr.values:
    z = np.split(line ,7)
    w=[]
    for zline in z:
        w.append(int(zline))
    x.append(line[0:6])
    y.append(line[6])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

