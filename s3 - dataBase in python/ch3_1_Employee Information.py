import mysql.connector

# Connect to the MySQL database.
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='learn')

# Create a cursor to execute MySQL queries.
cursor = cnx.cursor()

# Define the SQL query to select all rows from the 'employees' table.
query = 'SELECT * FROM employees'

# Execute the query to fetch data from the database.
cursor.execute(query)

# Create an empty list to store dictionaries of employee information.
listOfDic = list()

# Iterate through the result set and convert each row into a dictionary.
# Each dictionary represents an employee with 'name', 'weight', and 'height' keys.
for (name,weight,height) in cursor:
    dictOfEmp = dict()
    dictOfEmp['name'] = name
    dictOfEmp['weight'] = weight
    dictOfEmp['height'] = height
    listOfDic.append(dictOfEmp)

# Sort the list of dictionaries based on the 'height' in descending order and 'weight' in ascending order.
# This way, the employees will be printed in ascending order of height and, in case of a tie, lower weight will be considered first.
s = sorted(listOfDic, key = lambda x: (-x['height'], x['weight']))

# Print the employee information in the required format (name, height, weight).
for i in range(len(s)):
    print(s[i]['name'],s[i]['height'],s[i]['weight'])

# Commit any changes made to the database (not applicable in this code, as it only reads data).
cnx.commit()
