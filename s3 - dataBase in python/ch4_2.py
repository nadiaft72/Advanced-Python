'''
Write a program that takes an email and password as input and stores them in a database under the titles "username" and "password". Only submit your code file.
The written code should be capable of receiving input data, storing and registering the information in a preferred database file.
Ensuring the email format as input is essential.
If the input format is not in the form of an email, it should show the user an example of the correct format and prompt them to enter the input again.
The password should include a combination of numbers and strings.
The correct email pattern is as follows: 
it consists of two strings and an expression (including a string and/or a number and a string simultaneously) separated by @ and .,
making it a valid email. It should be in the following format:
expression@string.string
'''

import re
import mysql.connector

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
 
def check(email):
 
    if(re.search(regex, email)):
        return 1
 
    else:
        return 0
 
flag = 0
while flag==0 :
    email = input('ypur email : ')
    password = input('your password : ')
    if check(email) == 0 :
        print("please enter a valid email like : expression@string.string ")
    else : 
        flag =1
        cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='learn')
        cursor = cnx.cursor()
        query = 'INSERT INTO users VALUES (%s , %s)'
        cursor.execute(query , (email,password))
        cnx.commit()
