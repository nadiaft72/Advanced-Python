import mysql.connector 
import pandas
import csv

cnx = mysql.connector.connect(host='localhost',
                                         database='TCcars',
                                         user='root',
                                         password='')
cursor = cnx.cursor()
query = 'select * from cars'
cursor.execute(query)
with open("E:\workplace\python\Advanced Python\s6\dataB.csv","w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(col[0] for col in cursor.description)
    for row in cursor:
        if row:
            writer.writerow(row)
df = pandas.read_csv('E:\workplace\python\Advanced Python\s6\dataB.csv')
df.to_csv('E:\workplace\python\Advanced Python\s6\dataB.csv', index=False)

        