from flask import Flask

import mysql.connector

mydb = mysql.connector.connect(
    port=8889,
    host="localhost",
    user="root",
    password="root",
    database="quizoo"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM question")
allQuestions = mycursor.fetchall()
print(allQuestions)


##### INFOS SUR UN SITE 
# mysql = MySQL(app)
 
# #Creating a connection cursor
# cursor = mysql.connection.cursor()
 
# #Executing SQL Statements
# cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
# #Saving the Actions performed on the DB
# mysql.connection.commit()
 
# #Closing the cursor
# cursor.close()
