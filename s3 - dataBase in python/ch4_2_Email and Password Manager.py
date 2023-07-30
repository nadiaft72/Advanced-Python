import re
import mysql.connector

# Regular expression pattern to check for a valid email format.
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
 
def check(email):

     # Function to validate email format using the provided regular expression.
    if(re.search(regex, email)):
        return 1
 
    else:
        return 0
 
flag = 0

# Loop to get user input for email and password until a valid email is provided.
while flag==0 :
    email = input('ypur email : ')
    password = input('your password : ')
    if check(email) == 0 :
        print("please enter a valid email like : expression@string.string ")
    else : 
        flag =1
        # Establish connection to the MySQL database.
        cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='learn')
        cursor = cnx.cursor()

        # Insert the email and password into the 'users' table of the database.
        query = 'INSERT INTO users VALUES (%s , %s)'
        cursor.execute(query , (email,password))
        cnx.commit()
