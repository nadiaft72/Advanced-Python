import mysql.connector
cnx = mysql.connector.connect(host='localhost',
                                         database='cars',
                                         user='root',
                                         password='')
cursor = cnx.cursor()
val = "202020"
sql = "INSERT INTO mile VALUES (%s)" %val

cursor.execute(sql)
cnx.commit()
