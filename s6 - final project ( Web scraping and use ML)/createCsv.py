# createCsv.py - Create CSV File from MySQL Database

import mysql.connector 
import pandas
import csv

# Connect to the MySQL database 'TCcars'.
cnx = mysql.connector.connect(host='localhost',
                                         database='TCcars',
                                         user='root',
                                         password='')
cursor = cnx.cursor()

# Execute a query to select all data from the 'cars' table.
query = 'select * from cars'
cursor.execute(query)

# Open the CSV file ('dataB.csv') to write data into it.
# Use the quoting option to ensure non-numeric data is quoted in the CSV.
with open("E:\workplace\python\Advanced Python\s6\dataB.csv","w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
  
    # Write the header row with column names from the database table.
    writer.writerow(col[0] for col in cursor.description)

    # Fetch each row from the 'cars' table and write it as a new row in the CSV file.
    for row in cursor:
        if row:
            writer.writerow(row)
          
# Read the data from the CSV file using pandas.
df = pandas.read_csv('E:\workplace\python\Advanced Python\s6\dataB.csv')

# Write the data back to the CSV file without the default index.
# This step ensures that the data is correctly formatted in the CSV.
df.to_csv('E:\workplace\python\Advanced Python\s6\dataB.csv', index=False)

        
