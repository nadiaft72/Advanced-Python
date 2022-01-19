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


cr = pd.read_csv("E:\workplace\python\Advanced Python\s6\dataB.csv")

# œ? «? Ãœ?œ —Ê «“ ò«—»— „?ê?—Â Ê »Â ›«?· «÷«›Â „?ò‰œ
# Ê Êﬁ ? ›«?· œ«—Â òœ „?‘Â «ÿ·«⁄«  Ãœ?œ ò«—»— Â„ »«Â«‘ òœ „?‘Â  « » Ê‰?„ »⁄œ‘ œ? «? òœ ‘œÂ —« »œ?„ »Â Å—œ?ò 

new_data = "Acura,SH-AWD,1046,2,CA,2019,0"
yOrn = input("We considered the following data : Acura,SH-AWD,1046,2,CA,2019,0 , if you wanna add another data enter y else enter n :")
if yOrn == "y" or yOrn== "Y":
    new_data = input("plz enter the current model_name,model,mile,accident,location,year,price : ")
new_data = new_data + "\n"
with open('E:\workplace\python\Advanced Python\s6\dataB.csv','a') as fd:
    fd.write(new_data)

label_encoders = {}
categorical_columns = ["model_name" ,"model"  ,"accident","location", "year" ]

#òœ ê–«—? „?ò‰?„ çÊ‰ œ”?é‰  —? «” —?‰ê ﬁ»Ê· ‰„?ò‰Â 
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    cr[column] = label_encoders[column].fit_transform(cr[column]) 

# Õ«·« òÂ òœ ê–«—? ‘œ „?«?„ Ê Ê—Êœ? Ê Œ—ÊÃ? œ?”?é‰  —? —Ê „ﬁœ«— œÂ? „?ò‰?„
x=[]
y=[]

for line in cr.values:
    z = np.split(line ,7)
    w=[]
    for zline in z:
        w.append(int(zline))
    x.append(line[0:6])
    y.append(line[6])
#¬Œ—?‰ ”ÿ— Ê«—œ ‘œÂ œ? «? Ãœ?œÂ Å” «“ Ê—Êœ? Ê Œ—ÊÃ? Â« Å«Å „?ò‰?„   
new_data = x.pop()
y.pop()

#¬Œ—?‰ ”ÿ— —Ê «“ ›«?· Â„ Å«ò „?ò‰?„ 
f = open('E:\workplace\python\Advanced Python\s6\dataB.csv', "r+")
lines = f.readlines()
lines.pop()
f = open('E:\workplace\python\Advanced Python\s6\dataB.csv', "w+")
f.writelines(lines)

#Œ» Õ«·« „?œ?„‘ »Â œ?”?é‰  —?  « „œ· »‰œ?‘Ê‰ ò‰Â
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

#«?‰Ã« Â„ »—«? «?‰òÂ »œ?„‘ »Â Å—œ?ò ?Â ¬—«?Â œ—”  „?”«“?„ Ê „?œ?„‘ »Â Å—œ?ò 
list_new_data = []
for data in new_data:
    list_new_data.append(data)

Answer = clf.predict([list_new_data])
new_price = Answer[0]
print("you can use  price for this car : "  )
print(new_price)
