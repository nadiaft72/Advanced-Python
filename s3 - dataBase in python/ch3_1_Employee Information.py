'''
Employee Information:
A database containing employees' information, including their names, heights, and weights, has been designed for a design company. Write a program that reads the information from this database file and prints the employees in ascending order of height in the output, along with their names and weights. (If two individuals have the same height, print the one with the lower weight first). It is guaranteed that no two individuals have the same height and weight.

The format of the information in the database table is as follows:
Sample input: (The following information is defined in the database, and this is an example; the number of individuals may vary)

Height Weight Name
180 75 Amin
190 90 Mahdi
175 75 Mohammad
175 60 Ahmad

Sample output:
Mahdi 190 90
Amin 180 75
Ahmad 175 60
Mohammad 175 75
'''

import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='learn')

cursor = cnx.cursor()

query = 'SELECT * FROM employees'
cursor.execute(query)
listOfDic = list()
for (name,weight,height) in cursor:
    dictOfEmp = dict()
    dictOfEmp['name'] = name
    dictOfEmp['weight'] = weight
    dictOfEmp['height'] = height
    listOfDic.append(dictOfEmp)
s = sorted(listOfDic, key = lambda x: (-x['height'], x['weight']))

for i in range(len(s)):
    print(s[i]['name'],s[i]['height'],s[i]['weight'])
cnx.commit()
